from pydantic import BaseModel, ConfigDict
from typing import Optional

from .answers import AnswerRead


class QuestionBase(BaseModel):
    topic: str
    difficulty: str
    question: str
    answered: bool = False


class QuestionCreate(QuestionBase):
    pass


class QuestionRead(QuestionBase):
    id: int

    answer: Optional[AnswerRead] = None
    model_config = ConfigDict(from_attributes=True)


class QuestionUpdate(QuestionBase):
    pass
