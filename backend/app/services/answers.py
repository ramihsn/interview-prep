from sqlmodel import Session

from ..schemas.answers import AnswerCreate, AnswerRead
from ..models.questions import Question as QuestionModel
from ..models.answers import Answer as AnswerModel
from . import helpers


async def get_answers(db: Session, skip: int = 0, limit: int = 100) -> list[AnswerRead]:
    return await helpers.get_items(db, AnswerModel, AnswerRead, skip, limit)


async def get_answer(db: Session, answer_id: int) -> AnswerRead | None:
    return await helpers.get_item(db, AnswerModel, AnswerRead, answer_id)


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
    return await helpers.delete_item(db, AnswerModel, AnswerRead, answer_id)
