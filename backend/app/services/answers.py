from sqlmodel import Session, select

from ..schemas.answers import AnswerCreate, AnswerRead
from ..models.questions import Question as QuestionModel
from ..models.answers import Answer as AnswerModel


async def get_answers(db: Session, skip: int = 0, limit: int = 100) -> list[AnswerRead]:
    q = select(AnswerRead)

    if skip and skip > 0:
        q = q.offset(skip)

    if limit and limit > 0:
        q = q.limit(limit)

    return [AnswerRead.model_validate(i) for i in db.exec(q).all()]


async def get_answer(db: Session, answer_id: int) -> AnswerRead | None:
    return AnswerRead.model_validate(db.get(AnswerRead, answer_id))


async def answer_question(db: Session, answer: AnswerCreate) -> AnswerRead:
    if not (question := db.get(QuestionModel, answer.question_id)):
        raise ValueError("Question does not exist")

    answer_module = AnswerModel(**answer.model_dump())
    if question.answer:
        # the question already has an answer, change the answer instead of creating a new one
        question.answer = answer_module
        db.commit()
        db.refresh(question)
    else:
        db.add(answer_module)
        db.commit()
        db.refresh(answer_module)

    return AnswerRead.model_validate(answer_module)


async def delete_answer(db: Session, answer_id: int) -> None:
    if not (answer := db.get(AnswerRead, answer_id)):
        raise ValueError("Answer does not exist")

    question = db.get(QuestionModel, answer.question_id)

    question.answer = None
    db.delete(answer)
    db.commit()
    db.refresh(question)
    db.refresh(answer)
