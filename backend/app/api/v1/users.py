from fastapi import APIRouter, Depends
import logging

from app.services import users as users_service
from app import db

logger = logging.getLogger(__name__)
router = APIRouter(prefix='/users')


@router.get('/settings')
async def get_user_settings(db=Depends(db.session.get_db)):
    logger.info('Getting user settings')
    return await users_service.get_user_settings(db)


@router.put('/settings/theme')
async def set_user_theme(theme: str, db=Depends(db.session.get_db)):
    logger.info(f'Setting user theme to {theme}')
    return await users_service.set_user_theme(db, theme)


@router.put('/settings/group_by')
async def set_user_group_by(group_by: str, db=Depends(db.session.get_db)):
    logger.info(f'Setting user group by to {group_by}')
    return await users_service.set_user_group_by(db, group_by)
