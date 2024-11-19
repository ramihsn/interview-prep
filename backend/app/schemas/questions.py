import sqlmodel

from ..models.questions import Question as QuestionRead  # noqa: F401


class QuestionBase(sqlmodel.SQLModel):
    topic: str
    difficulty: str
    question: str
    answered: bool = False


class QuestionCreate(QuestionBase):
    pass


class QuestionUpdate(QuestionBase):
    pass
