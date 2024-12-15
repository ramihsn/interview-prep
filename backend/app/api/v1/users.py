from fastapi import APIRouter, Depends
import logging

from app.services import users as users_service
from app.models import users as users_models
from app import db

logger = logging.getLogger(__name__)
router = APIRouter(prefix='/users')


@router.get('/settings', response_model=users_models.UserSettings)
async def get_user_settings(db=Depends(db.session.get_db)):
    logger.info('Getting user settings')
    return await users_service.get_user_settings(db)


@router.put('/settings/theme', response_model=users_models.UserSettings)
async def set_user_theme(theme: str, db=Depends(db.session.get_db)):
    logger.info(f'Setting user theme to {theme}')
    return await users_service.set_user_theme(db, theme)


@router.put('/settings/group_by', response_model=users_models.UserSettings)
async def set_user_group_by(group_by: str, db=Depends(db.session.get_db)):
    logger.info(f'Setting user group by to {group_by}')
    return await users_service.set_user_group_by(db, group_by)


@router.put('/settings/position', response_model=users_models.UserSettings)
async def set_user_position(position_id: int, db=Depends(db.session.get_db)):
    logger.info(f'Setting user position to {position_id}')
    return await users_service.set_user_position(db, position_id)
