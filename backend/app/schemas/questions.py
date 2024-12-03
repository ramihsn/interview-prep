import sqlmodel

from .answers import AnswerRead
from . import helpers


class QuestionBase(sqlmodel.SQLModel):
    topic: str
    difficulty: str
    question: str
    answered: bool = False

    answer: AnswerRead | None = None


class QuestionRead(QuestionBase):
    id: int


class QuestionCreate(QuestionBase):
    pass


QuestionUpdate = helpers.make_optional(QuestionBase)
