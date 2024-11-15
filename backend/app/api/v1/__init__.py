from fastapi import APIRouter

from . import endpoints

router = APIRouter(prefix='/v1')
router.include_router(endpoints.router)
