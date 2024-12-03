from sqlmodel import Session, select

from ..schemas.questions import QuestionCreate, QuestionRead
from ..models.questions import Question as QuestionModel
from . import helpers


async def get_questions(db: Session, skip: int = 0, limit: int = 100) -> list[QuestionRead]:
    return await helpers.get_items(db, QuestionModel, QuestionRead, skip, limit)


async def get_question(db: Session, question_id: int) -> QuestionRead | None:
    return await helpers.get_item(db, QuestionModel, QuestionRead, question_id)


async def create_question(db: Session, question: QuestionCreate) -> QuestionRead:
    return await helpers.create_item(db, QuestionModel, QuestionRead, question)


async def update_question(db: Session, question_id: int, question: QuestionCreate
                          ) -> QuestionRead | None:
    return await helpers.update_item(db, QuestionModel, QuestionRead, question_id, question)


async def delete_question(db: Session, question_id: int) -> QuestionRead | None:
    return await helpers.delete_item(db, QuestionModel, QuestionRead, question_id)


async def _set_question_answered(db: Session, question_id: int, answered: bool) -> QuestionRead | None:
    if question := db.get(QuestionModel, question_id):
        question.answered = answered
        db.commit()
        db.refresh(question)
        return QuestionRead.model_validate(question)


async def answer_question(db: Session, question_id: int) -> QuestionRead | None:
    return await _set_question_answered(db, question_id, True)


async def unanswered_question(db: Session, question_id: int) -> QuestionRead | None:
    return await _set_question_answered(db, question_id, False)


async def get_answered_questions(db: Session, skip: int = 0, limit: int = 100) -> list[QuestionRead]:
    q = select(QuestionModel).where(QuestionModel.answered == True)  # noqa:E712

    if skip and skip > 0:
        q = q.offset(skip)

    if limit and limit > 0:
        q = q.limit(limit)

    return [QuestionRead.model_validate(i) for i in db.exec(q).all()]
