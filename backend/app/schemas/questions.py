from pydantic import BaseModel, ConfigDict


class QuestionBase(BaseModel):
    topic: str
    difficulty: str
    question: str
    answered: bool = False


class QuestionCreate(QuestionBase):
    pass


class QuestionRead(QuestionBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class QuestionUpdate(QuestionBase):
    pass
