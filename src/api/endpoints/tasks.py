from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, status

from src.api.auth import check_header_contains_token
from src.api.schemas import TaskResponse, TasksRequest
from src.api.schemas.tasks import TaskRequest
from src.api.services import TaskService
from src.api.services.messages import TelegramNotificationService
from src.bot.keyboards import get_task_info_keyboard
from src.core.db.models import Task
from src.core.depends import Container
from src.core.messages import display_task

tasks_router = APIRouter(dependencies=[Depends(check_header_contains_token)])
task_read_router = APIRouter()
task_write_router = APIRouter(dependencies=[Depends(check_header_contains_token)])


@tasks_router.post("", description="Актуализирует список задач.")
@inject
async def actualize_tasks(
    tasks: TasksRequest,
    task_service: TaskService = Depends(Provide[Container.api_services_container.task_service]),
    telegram_notification_service: TelegramNotificationService = Depends(
        Provide[Container.api_services_container.message_service]
    ),
    trigger_mailing_fields: str = Depends(Provide[Container.settings.provided.TRIGGER_MAILING_FIELDS]),
) -> None:
    new_tasks_ids, updated_tasks_ids = await task_service.actualize_objects(tasks.root, Task, trigger_mailing_fields)
    updated_tasks_ids_set = set(updated_tasks_ids)
    mailing_category_tasks = await task_service.get_user_tasks_ids(new_tasks_ids + updated_tasks_ids)
    for task in mailing_category_tasks:
        message = display_task(task, task.id in updated_tasks_ids_set)
        await telegram_notification_service.send_messages_to_subscribed_users(
            message, task.category_id, reply_markup=get_task_info_keyboard(task)
        )


@tasks_router.get(
    "/{user_id}",
    response_model=list[TaskResponse],
    response_model_exclude_none=True,
    description="Получает список всех задач из категорий, на которые подписан пользователь.",
)
@inject
async def get_tasks_for_user(
    user_id: int,
    task_service: TaskService = Depends(Provide[Container.api_services_container.task_service]),
) -> list[TaskResponse]:
    return await task_service.get_tasks_for_user(user_id)


@tasks_router.get(
    "",
    response_model=list[TaskResponse],
    response_model_exclude_none=True,
    description="Получает список всех задач.",
)
@inject
async def get_all_tasks(
    task_service: TaskService = Depends(Provide[Container.api_services_container.task_service]),
) -> list[TaskResponse]:
    return await task_service.get_all()


@task_read_router.get(
    "/{task_id}",
    response_model=TaskResponse,
    response_model_exclude_none=True,
    description="Получает данные по указанной задаче.",
)
@inject
async def get_task_detail(
    task_id: int,
    task_service: TaskService = Depends(Provide[Container.api_services_container.task_service]),
) -> TaskResponse:
    return await task_service.get(task_id)


@task_write_router.post(
    "",
    status_code=status.HTTP_200_OK,
    description="Добавление новой или обновление существующей задачи.",
)
@inject
async def create_update_task(
    task: TaskRequest,
    task_service: TaskService = Depends(Provide[Container.api_services_container.task_service]),
    telegram_notification_service: TelegramNotificationService = Depends(
        Provide[Container.api_services_container.message_service]
    ),
    trigger_mailing_fields: str = Depends(Provide[Container.settings.provided.TRIGGER_MAILING_FIELDS]),
):
    task_obj = await task_service.get_user_task_id(task.id)
    trigger_fields_changed, new_task = False, False
    if task_obj:
        # обновление существующей задачи
        trigger_fields_changed = await task_service.update(task_obj, trigger_mailing_fields, **task.model_dump())
    else:
        # создание новой задачи
        await task_service.create(**task.model_dump())
        new_task = True
    # рассылка уведомлений, при необходимости
    if trigger_fields_changed or new_task:
        task_with_category = await task_service.get_user_task_id(task.id)
        if task_with_category:
            message = display_task(task_with_category, updated_task=not new_task)
            await telegram_notification_service.send_messages_to_subscribed_users(
                message,
                task_with_category.category_id,
                reply_markup=get_task_info_keyboard(task_with_category),
            )


@task_write_router.delete(
    "/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    description="Удаляет указанную задачу из БД бота.",
)
@inject
async def delete_task(
    task_id: int,
    task_service: TaskService = Depends(Provide[Container.api_services_container.task_service]),
) -> None:
    await task_service.archive(task_id)
