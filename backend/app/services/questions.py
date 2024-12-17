from sqlmodel import Session, select, func
import logging

from ..schemas.questions import QuestionCreate, QuestionRead, QuestionUpdate
from ..models.questions import Question as QuestionModel
from . import helpers

logger = logging.getLogger(__name__)


async def get_questions(db: Session, skip: int = 0, limit: int = 100) -> list[QuestionRead]:
    logger.info("Getting questions")
    return await helpers.get_items(db, QuestionModel, QuestionRead, skip, limit)


async def get_question(db: Session, question_id: int) -> QuestionRead | None:
    logger.info(f"Getting question with ID {question_id}")
    return await helpers.get_item(db, QuestionModel, QuestionRead, question_id)


async def create_question(db: Session, question: QuestionCreate) -> QuestionRead:
    logger.info(f"Creating a new question {question}")
    return await helpers.create_item(db, QuestionModel, QuestionRead, question)


async def update_question(db: Session, question_id: int, question: QuestionUpdate  # type: ignore
                          ) -> QuestionRead | None:
    logger.info(f"Updating question with ID {question_id} to {question}")
    return await helpers.update_item(db, QuestionModel, QuestionRead, question_id, question)


async def delete_question(db: Session, question_id: int) -> QuestionRead | None:
    logger.info(f"Deleting question with ID {question_id}")
    if await helpers.delete_item(db, QuestionModel, QuestionRead, question_id):
        return

    logger.error("Question does not exist")
    raise ValueError("Question does not exist")


async def _set_question_answered(db: Session, question_id: int, answered: bool) -> QuestionRead | None:
    if question := db.get(QuestionModel, question_id):
        question.answered = answered
        db.commit()
        db.refresh(question)
        return QuestionRead.model_validate(question)


async def answer_question(db: Session, question_id: int) -> QuestionRead | None:
    logger.info(f"Answering question with ID {question_id}")
    return await _set_question_answered(db, question_id, True)


async def unanswered_question(db: Session, question_id: int) -> QuestionRead | None:
    logger.info(f"Unanswering question with ID {question_id}")
    return await _set_question_answered(db, question_id, False)


async def get_answered_questions(db: Session, skip: int = 0, limit: int = 100) -> list[QuestionRead]:
    logger.info("Getting answered questions")
    q = select(QuestionModel).where(QuestionModel.answered == True)  # noqa:E712

    if skip and skip > 0:
        q = q.offset(skip)

    if limit and limit > 0:
        q = q.limit(limit)

    return [QuestionRead.model_validate(i) for i in db.exec(q).all()]


async def delete_questions_by_position(db: Session, position_id: int) -> None:
    logger.info(f"Deleting all questions for position with ID {position_id}")
    q = select(QuestionModel).where(QuestionModel.position_id == position_id)  # noqa:E712
    for question in db.exec(q).all():
        logger.info(f"Deleting question: {question}")
        db.delete(question)
    db.commit()


async def get_question_count_by_position(db: Session, position_id: int) -> int:
    logger.info(f"Getting question count for position with ID {position_id}")
    q = select(func.count()).select_from(QuestionModel).where(QuestionModel.position_id == position_id)  # noqa:E712
    return db.exec(q).one()
