import sqlmodel
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.answers import Answer


class Question(sqlmodel.SQLModel, table=True):
    __tablename__ = "questions"  # if not set, table name will be the class name

    id: int = sqlmodel.Field(primary_key=True, index=True)

    topic: str = sqlmodel.Field()
    difficulty: str = sqlmodel.Field()
    question: str = sqlmodel.Field()
    answered: bool = sqlmodel.Field(default=False)

    # Relationship to Answer with nullable=True
    answer: "Answer" = sqlmodel.Relationship(back_populates="question")
