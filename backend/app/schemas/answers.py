import sqlmodel

from ..models.answers import Answer as AnswerRead  # noqa: F401
from . import helpers


class AnswerBase(sqlmodel.SQLModel):
    answer: str
    review: str
    rating: float
    question_id: int


class AnswerCreate(AnswerBase):
    pass


AnswerUpdate = helpers.make_optional(AnswerBase)
