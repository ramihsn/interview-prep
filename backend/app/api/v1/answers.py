from fastapi import APIRouter, HTTPException, Depends, status, Response  # noqa

from app import schemas, services, db

router = APIRouter(prefix='/answers')


@router.post('/', response_model=schemas.answers.AnswerRead, status_code=status.HTTP_201_CREATED)
async def answer_question(answer: schemas.answers.AnswerCreate, db=Depends(db.session.get_db)):
    return await services.answers.answer_question(db, answer)
