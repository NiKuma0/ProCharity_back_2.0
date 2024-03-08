from dependency_injector.wiring import Provide, inject
from telegram import Update
from telegram.ext import Application, ChatMemberHandler, CommandHandler, ContextTypes

from src.bot.constants import commands
from src.bot.keyboards import get_start_keyboard
from src.bot.services.external_site_user import ExternalSiteUserService
from src.bot.services.user import UserService
from src.core.depends import Container
from src.core.logging.utils import logger_decor


@logger_decor
@inject
async def start_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    user_service: UserService = Provide[Container.bot_services_container.bot_user_service],
):
    telegram_user = update.effective_user
    ext_user = await user_service.determine_ext_user(
        context.args[0] if len(context.args) == 1 else None, telegram_user.id
    )
    if not ext_user:
        return

    user = await user_service.register_user(
        telegram_id=telegram_user.id,
        username=telegram_user.username,
        first_name=ext_user.first_name,
        last_name=ext_user.last_name,
        email=ext_user.email,
        external_id=ext_user.id,
    )
    await user_service.set_categories_to_user(user.id, ext_user.specializations)
    keyboard = await get_start_keyboard()
    await context.bot.send_message(
        chat_id=telegram_user.id,
        text="Авторизация прошла успешно!\n\n"
        "Теперь оповещения будут приходить сюда. "
        "Изменить настройку уведомлений можно в личном кабинете.\n\n",
        reply_markup=keyboard,
    )


@logger_decor
@inject
async def on_chat_member_update(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    ext_user_service: ExternalSiteUserService = Provide[Container.bot_services_container.bot_site_user_service],
    user_service: UserService = Provide[Container.bot_services_container.bot_user_service],
):
    user = await user_service.get_by_telegram_id(update.effective_user.id)

    if user is None:
        return None

    if (
        update.my_chat_member.new_chat_member.status == update.my_chat_member.new_chat_member.BANNED
        and update.my_chat_member.old_chat_member.status == update.my_chat_member.old_chat_member.MEMBER
    ):
        return await user_service.bot_banned(user)
    if (
        update.my_chat_member.new_chat_member.status == update.my_chat_member.new_chat_member.MEMBER
        and update.my_chat_member.old_chat_member.status == update.my_chat_member.old_chat_member.BANNED
    ):
        return await user_service.bot_unbanned(user)

    return None


def registration_handlers(app: Application):
    app.add_handler(CommandHandler(commands.START, start_command))
    app.add_handler(ChatMemberHandler(on_chat_member_update, chat_member_types=ChatMemberHandler.MY_CHAT_MEMBER))
