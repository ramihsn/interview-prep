from sqlmodel import Session

from ..schemas.questions import QuestionCreate, QuestionRead
from ..models.questions import Question as QuestionModel


async def add_question(db: Session, question: QuestionCreate) -> QuestionRead:
    db_item = QuestionModel(**question.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return QuestionRead.model_validate(db_item)


async def get_question(db: Session, question_id: int) -> QuestionRead | None:
    if db_item := db.query(QuestionModel).filter(QuestionModel.id == question_id).first():
        return QuestionRead.model_validate(db_item)


async def get_questions(db: Session, skip: int = 0, limit: int = 100) -> list[QuestionRead]:
    q = db.query(QuestionModel)

    if skip and skip > 0:
        q = q.offset(skip)

    if limit and limit > 0:
        q = q.limit(limit)

    return [QuestionRead.model_validate(db_item) for db_item in q.all()]


async def update_question(db: Session, question_id: int, question: QuestionCreate
                          ) -> QuestionRead | None:
    if db_item := db.query(QuestionModel).filter(QuestionModel.id == question_id).first():
        for key, value in question.model_dump().items():
            setattr(db_item, key, value)
        db.commit()
        db.refresh(db_item)
        return QuestionRead.model_validate(db_item)


async def delete_question(db: Session, question_id: int) -> QuestionRead | None:
    if db_item := db.query(QuestionModel).filter(QuestionModel.id == question_id).first():
        db.delete(db_item)
        db.commit()
        return QuestionRead.model_validate(db_item)


async def answer_question(db: Session, question_id: int) -> QuestionRead | None:
    if db_item := db.query(QuestionModel).filter(QuestionModel.id == question_id).first():
        db_item.answered = True
        db.commit()
        db.refresh(db_item)
        return QuestionRead.model_validate(db_item)


async def unanswered_question(db: Session, question_id: int) -> QuestionRead | None:
    if db_item := db.query(QuestionModel).filter(QuestionModel.id == question_id).first():
        db_item.answered = False
        db.commit()
        db.refresh(db_item)
        return QuestionRead.model_validate(db_item)


async def get_answered_questions(db: Session, skip: int = 0, limit: int = 100) -> list[QuestionRead]:
    return [
        QuestionRead.model_validate(db_item) for db_item in
        db.query(QuestionModel).filter(QuestionModel.answered == True).offset(skip).limit(limit).all()  # noqa:E712
    ]
