from fastapi import APIRouter

from . import questions, answers, users, positions

router = APIRouter(prefix='/v1')
router.include_router(questions.router, tags=["questions"])
router.include_router(answers.router, tags=["answers"])
router.include_router(positions.router, tags=["position"])
router.include_router(users.router, tags=["users"])
