import sqlmodel

from .questions import Question


class Position(sqlmodel.SQLModel, table=True):
    __tablename__ = "positions"  # if not set, table name will be the class name

    id: int = sqlmodel.Field(primary_key=True, index=True)
    company: str
    title: str
    description: str

    questions: list[Question] = sqlmodel.Relationship(back_populates="position", cascade_delete=True)
