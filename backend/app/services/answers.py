from sqlmodel import Session

from ..schemas.answers import AnswerCreate, AnswerRead
from ..models.questions import Question as QuestionModel


async def answer_question(db: Session, answer: AnswerCreate) -> AnswerRead:
    if not (question := db.get(QuestionModel, answer.question_id)):
        raise ValueError("Question does not exist")

    if answer := question.answer:
        # the question already has an answer, change the answer instead of creating a new one
        for field, value in question.model_dump().items():
            setattr(answer, field, value)

        db.commit()
        db.refresh(answer)
    else:
        db.add(answer)
        db.commit()
        db.refresh(answer)

    return answer
