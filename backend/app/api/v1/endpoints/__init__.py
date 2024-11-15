from fastapi import APIRouter

# Import the routers from the endpoints modules here.
from . import questions

router = APIRouter()

# TODO: Add the routers from the imported modules here.
router.include_router(questions.router, prefix="/questions", tags=["questions"])
