import sqlmodel

from app.models.answers import Answer


class Question(sqlmodel.SQLModel, table=True):
    __tablename__ = "questions"  # if not set, table name will be the class name

    id: int = sqlmodel.Field(primary_key=True, index=True)

    topic: str = sqlmodel.Field()
    difficulty: str = sqlmodel.Field()
    question: str = sqlmodel.Field()
    answered: bool = sqlmodel.Field(default=False)

    position_id: int = sqlmodel.Field(foreign_key="positions.id")
    answer: Answer | None = sqlmodel.Relationship(back_populates="question", cascade_delete=True)
