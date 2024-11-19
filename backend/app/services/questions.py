from sqlmodel import Session, select

from ..schemas.questions import QuestionCreate, QuestionRead
from ..models.questions import Question as QuestionModel


async def add_question(db: Session, question: QuestionCreate) -> QuestionRead:
    question_module = QuestionModel(**question.model_dump())
    db.add(question_module)
    db.commit()
    db.refresh(question_module)
    return QuestionRead.model_validate(question_module)


async def get_question(db: Session, question_id: int) -> QuestionRead | None:
    return QuestionRead.model_validate(db.get(QuestionModel, question_id))


async def get_questions(db: Session, skip: int = 0, limit: int = 100) -> list[QuestionRead]:
    q = select(QuestionModel)

    if skip and skip > 0:
        q = q.offset(skip)

    if limit and limit > 0:
        q = q.limit(limit)

    return [QuestionRead.model_validate(i) for i in db.exec(q).all()]


async def update_question(db: Session, question_id: int, question: QuestionCreate
                          ) -> QuestionRead | None:
    if old_question := db.get(QuestionModel, question_id):
        for field, value in question.model_dump().items():
            setattr(old_question, field, value)

        db.commit()
        db.refresh(old_question)
        return QuestionRead.model_validate(old_question)


async def delete_question(db: Session, question_id: int) -> QuestionRead | None:
    if question := db.get(QuestionModel, question_id):
        db.delete(question)
        db.commit()
        return QuestionRead.model_validate(question)


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
