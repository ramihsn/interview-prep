from sqlmodel import Session

from ..schemas.answers import AnswerCreate, AnswerRead
from ..models.answers import Answer as AnswerModel
from ..models.questions import Question as QuestionModel


async def answer_question(db: Session, answer: AnswerCreate) -> AnswerRead:
    if (question := db.query(QuestionModel).filter(QuestionModel.id == answer.question_id).first()) is None:
        raise ValueError("Question does not exist")

    if db_item := question.answer:
        # the question already has an answer, change the answer instead of creating a new one
        for key, value in answer.model_dump().items():
            setattr(db_item, key, value)
        db.commit()
    else:
        db_item = AnswerModel(**answer.model_dump())
        db.add(db_item)
        db.commit()

    return AnswerRead.model_validate(db_item)
