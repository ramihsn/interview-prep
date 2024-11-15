from pydantic import BaseModel, ConfigDict
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .questions import QuestionRead


class AnswerBase(BaseModel):
    answer: str
    review: str
    rating: float
    question_id: int


class AnswerCreate(AnswerBase):
    pass


class AnswerRead(AnswerBase):
    id: int
    answer: 'QuestionRead'

    model_config = ConfigDict(from_attributes=True)


class AnswerUpdate(AnswerBase):
    pass
