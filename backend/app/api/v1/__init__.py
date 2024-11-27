from fastapi import APIRouter

from . import questions, answers, user

router = APIRouter(prefix='/v1')
router.include_router(questions.router, tags=["questions"])
router.include_router(answers.router, tags=["answers"])
router.include_router(user.router, tags=["user"])
