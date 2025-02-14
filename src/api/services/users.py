from typing import Any

from src.core.db.repository import UserRepository
from src.core.services import BaseUserService


class UserService(BaseUserService):
    """Сервис для работы с моделью User."""

    def __init__(
        self,
        user_repository: UserRepository,
    ) -> None:
        super().__init__(user_repository)

    async def get_users_by_page(self, page: int, limit: int) -> dict:
        return await self._user_repository.get_objects_by_page(page, limit)

    async def get_filtered_users_by_page(self, filter_by: dict[str:Any], page: int, limit: int) -> dict:
        return await self._user_repository.get_filtered_objects_by_page(filter_by, page, limit)
