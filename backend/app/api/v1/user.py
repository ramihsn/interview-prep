from fastapi import APIRouter, Depends

from app.services import user as user_service
from app import db

router = APIRouter(prefix='/user')


@router.get('/settings')
async def get_user_settings(db=Depends(db.session.get_db)):
    return await user_service.get_user_settings(db)


@router.put('/settings/theme')
async def set_user_theme(theme: str, db=Depends(db.session.get_db)):
    return await user_service.set_user_theme(db, theme)


@router.put('/settings/group_by')
async def set_user_group_by(group_by: str, db=Depends(db.session.get_db)):
    return await user_service.set_user_group_by(db, group_by)
