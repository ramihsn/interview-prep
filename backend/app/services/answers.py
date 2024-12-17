from sqlmodel import Session
import logging

from ..schemas.answers import AnswerCreate, AnswerRead, AnswerUpdate
from ..models.questions import Question as QuestionModel
from ..models.answers import Answer as AnswerModel
from . import helpers

logger = logging.getLogger(__name__)


async def get_answers(db: Session, skip: int = 0, limit: int = 100) -> list[AnswerRead]:
    logger.info("Getting answers")
    return await helpers.get_items(db, AnswerModel, AnswerRead, skip, limit)


async def get_answer(db: Session, answer_id: int) -> AnswerRead | None:
    logger.info(f"Getting answer with ID {answer_id}")
    return await helpers.get_item(db, AnswerModel, AnswerRead, answer_id)


async def create_answer(db: Session, answer: AnswerCreate) -> AnswerRead:
    logger.info(f"Answering question with ID {answer.question_id}")
    if not (question := db.get(QuestionModel, answer.question_id)):
        logger.error("Question does not exist")
        raise ValueError("Question does not exist")

    logger.debug(f"Answering the question: {question} with the following answer: {answer}")
    answer_module = AnswerModel(**answer.model_dump())
    if question.answer:
        logger.debug("Question already has an answer, updating the answer")
        logger.debug(f"Old answer: {question.answer}")
        logger.debug(f"New answer: {answer_module}")
        # the question already has an answer, change the answer instead of creating a new one
        question.answer = answer_module
        db.commit()
        db.refresh(question)
    else:
        logger.debug("Question does not have an answer, creating a new answer")
        logger.debug(f"New answer: {answer_module}")
        db.add(answer_module)
        db.commit()
        db.refresh(answer_module)

    return AnswerRead.model_validate(answer_module)


async def update_position(db: Session, answer_id: int, answer: AnswerUpdate) -> AnswerRead | None:  # type: ignore
    logger.info(f"Updating answer with ID {answer_id} to {answer}")
    return await helpers.update_item(db, AnswerModel, AnswerRead, answer_id, answer)


async def delete_answer(db: Session, answer_id: int) -> None:
    logger.info(f"Deleting answer with ID {answer_id}")
    if await helpers.delete_item(db, AnswerModel, AnswerRead, answer_id):
        return

    logger.error("Answer does not exist")
    raise ValueError("Answer does not exist")
