from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from src.api.services.base import ContentService
from src.core.db.models import Task
from src.core.db.repository.task import TaskRepository


class TaskService(ContentService):
    """Сервис для работы с моделью Task."""

    def __init__(self, task_repository: TaskRepository, session: AsyncSession) -> None:
        super().__init__(task_repository, session)

    async def get(self, id: int) -> Task:
        """Получает задачу по её ID.
        В случае отсутствия задачи с таким ID возбуждает NotFoundException.
        """
        return await self._repository.get(id)

    async def get_tasks_for_user(self, user_id: int) -> list[Task]:
        return await self._repository.get_tasks_for_user(user_id)

    async def get_user_task_id(self, task_id: int) -> Optional[Task]:
        return await self._repository.get_user_task_id(task_id)

    async def get_user_tasks_ids(self, ids: list[int]) -> list[Task]:
        return await self._repository.get_user_tasks_ids(ids)

    async def get_tasks_by_filter(self, **filter_by) -> list[Task]:
        return await self._repository.get_tasks_by_filter(**filter_by)

    async def create(self, **attrs):
        """Создание новой задачи."""
        return await self._repository.create(Task(**attrs))

    async def update(self, task: Task, trigger_fields: list[str] | None = None, **attrs) -> bool:
        """Обновление задачи значениями attrs.
        Returns:
            True, если изменилось хотя бы одно из полей, указанных в trigger_fields
        """
        old_task_dict = task.to_dict()
        changed = any(attrs.get(name) and attrs.get(name) != old_task_dict.get(name) for name in trigger_fields)
        await self._repository.update(task.id, Task(**attrs))
        return changed
