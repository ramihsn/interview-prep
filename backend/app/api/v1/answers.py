from fastapi import APIRouter, HTTPException, Depends, status, Response  # noqa
import logging

from app import schemas, services, db

logger = logging.getLogger(__name__)
router = APIRouter(prefix='/answers')


@router.get('/', response_model=list[schemas.answers.AnswerRead])
async def get_answers(db=Depends(db.session.get_db)):
    logger.info('Getting all answers')
    return await services.answers.get_answers(db)


@router.get('/{answer_id}', response_model=schemas.answers.AnswerRead)
async def get_answer(answer_id: int, db=Depends(db.session.get_db)):
    logger.info(f'Getting answer with id {answer_id}')
    if answer := await services.answers.get_answer(db, answer_id):
        return answer

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Answer not found")


@router.post('/', response_model=schemas.answers.AnswerRead, status_code=status.HTTP_201_CREATED)
async def answer_question(answer: schemas.answers.AnswerCreate, db=Depends(db.session.get_db)):
    logger.info(f'Answering question with id {answer.question_id}')
    return await services.answers.answer_question(db, answer)


@router.delete('/{answer_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_answer(answer_id: int, db=Depends(db.session.get_db)):
    logger.info(f'Deleting answer with id {answer_id}')
    if not await services.answers.delete_answer(db, answer_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Answer not found")
