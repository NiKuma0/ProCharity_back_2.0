from contextlib import asynccontextmanager

from sqlalchemy import select
from structlog import get_logger

from src.api.services.admin_token_request import AdminTokenRequestService
from src.core.db import get_session
from src.core.db.models import AdminTokenRequest, AdminUser
from src.core.db.repository.admin_token_request import AdminTokenRequestRepository
from src.core.services.email import EmailProvider
from src.settings import settings

logger = get_logger()


async def create_token_for_super_user() -> None:
    """Создаёт токен и отправляет его на почту администратора"""
    session_manager = asynccontextmanager(get_session)
    async with session_manager() as session:
        admin = await session.scalar(select(AdminUser).where(AdminUser.email == settings.EMAIL_ADMIN))
        admin_token_request = await session.scalar(
            select(AdminTokenRequest).where(AdminTokenRequest.email == settings.EMAIL_ADMIN)
        )

        if admin is None and admin_token_request is None:
            admin_token_service = AdminTokenRequestService(AdminTokenRequestRepository(session))
            token = await admin_token_service.create_invitation_token(settings.EMAIL_ADMIN, True)

            email_provider = EmailProvider(session, settings)
            await email_provider.send_invitation_link(settings.EMAIL_ADMIN, token)

            await logger.ainfo(
                f'Super user registration: The invitation "{token}" generated for {settings.EMAIL_ADMIN}.'
            )
