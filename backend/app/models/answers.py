import sqlmodel
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.questions import Question


class Answer(sqlmodel.SQLModel, table=True):
    __tablename__ = "answers"  # if not set, table name will be the class name

    id: int = sqlmodel.Field(primary_key=True, index=True)

    answer: str = sqlmodel.Field()
    review: str = sqlmodel.Field()
    rating: str = sqlmodel.Field()

    # Relationship to Question
    question_id: int = sqlmodel.Field(foreign_key="questions.id")
    question: "Question" = sqlmodel.Relationship(back_populates="answer")
