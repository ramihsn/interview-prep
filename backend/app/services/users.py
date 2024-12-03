from sqlmodel import Session
import logging

from ..models.users import UserSettings

logger = logging.getLogger(__name__)


async def _get_or_create_user(db: Session) -> UserSettings:
    if user_settings := db.get(UserSettings, 1):
        return user_settings

    user_settings = UserSettings()
    db.add(user_settings)
    db.commit()
    db.refresh(user_settings)
    return user_settings


async def get_user_settings(db: Session) -> UserSettings:
    logger.info("Getting user settings")
    return await _get_or_create_user(db)


async def set_user_theme(db: Session, theme: str) -> UserSettings:
    logger.info(f"Setting user theme to {theme}")
    user_settings = await _get_or_create_user(db)
    user_settings.theme = theme
    db.commit()
    db.refresh(user_settings)
    return user_settings


async def set_user_group_by(db: Session, group_by: str) -> UserSettings:
    logger.info(f"Setting user questions group by to {group_by}")
    user_settings = await _get_or_create_user(db)
    user_settings.questions_group_by = group_by
    db.commit()
    db.refresh(user_settings)
    return user_settings
