from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.schemas import ExternalSiteUserRequest
from src.core.db import get_session
from src.core.db.repository.external_site_user import ExternalSiteUserRepository


class ExternalSiteUserService:
    """Сервис для работы с моделью ExternalSiteUser."""

    def __init__(
        self, site_user_repository: ExternalSiteUserRepository = Depends(), session: AsyncSession = Depends(get_session)
    ) -> None:
        self._repository: ExternalSiteUserRepository = site_user_repository
        self._session: AsyncSession = session

    async def register(self, site_user_schema: ExternalSiteUserRequest) -> None:
        site_user = await self._repository.get_by_external_id(site_user_schema.external_id)
        if site_user:
            await self._repository.update(None, site_user_schema.to_orm(site_user))
        else:
            await self._repository.create(site_user_schema.to_orm())
