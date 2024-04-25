import aiohttp
from structlog import get_logger

from src.core.schemas.procharity_api import SiteUserCategoriesRequest
from src.settings import Settings

logger = get_logger(module=__name__)


class ProcharityAPI:
    """Класс для отправки сообщений на API сайта."""

    def __init__(self, settings: Settings):
        self._settings = settings

    @property
    def token_header_dict(self) -> dict[str, str]:
        """Возвращает заголовок с токеном авторизации в виде словаря."""
        return {"token": self._settings.ACCESS_TOKEN_SEND_DATA_TO_PROCHARITY}

    async def send_user_categories(self, user_id: int, user_categories: list[int]):
        """Отправляет запрос на сайт с обновленными категориями пользователя.

        Args:
            user_id: идентификатор пользователя на сайте.
            user_categories: список идентификаторов выбранных категорий.
        """
        specializations = ", ".join(map(str, user_categories))
        body_schema = SiteUserCategoriesRequest(user_id=user_id, specializations=specializations)
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    url=self._settings.procharity_send_user_categories_api_url,
                    data=body_schema.model_dump_json(),
                    headers=self.token_header_dict,
                ) as response:
                    if response.status != 200:
                        await logger.ainfo(
                            f"Ошибка обновления категорий пользователя {user_id}: status = {response.status}"
                        )
                    else:
                        data = await response.json()
                        await logger.adebug(f"Отправлены обновленные категории пользователя {user_id}. Ответ: {data}")
        except Exception as e:
            await logger.aexception(e)
