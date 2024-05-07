from src.core.db.models import User


def format_user(user: User) -> dict:
    return {
        "telegram_id": user.telegram_id,
        "external_id": user.external_id,
        "username": user.username,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "has_mailing": user.has_mailing,
        "created_at": user.created_at.strftime("%Y-%m-%d"),
        "banned": user.banned,
    }
