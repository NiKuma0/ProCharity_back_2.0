from fastapi import APIRouter

from src.api.schemas.admin import AdminUserCreate, AdminUserRead
from src.core.admin_auth.fastapi_users import auth_backend, auth_cookie_backend, fastapi_admin_users

admin_user_router = APIRouter()


admin_user_router.include_router(fastapi_admin_users.get_auth_router(auth_backend))
admin_user_router.include_router(fastapi_admin_users.get_register_router(AdminUserRead, AdminUserCreate))
admin_user_router.include_router(
    fastapi_admin_users.get_auth_router(auth_cookie_backend),
    prefix="/cookies",
)
