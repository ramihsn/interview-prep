from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import orm as sa_orm
import sqlalchemy as sa

from app.db.base import Base


class Answer(Base):
    __tablename__ = "answers"

    id = sa.Column(sa.Integer, primary_key=True, index=True)

    answer = sa.Column(sa.String)
    review = sa.Column(sa.String)
    rating = sa.Column(sa.Integer)

    # Relationship to Question
    question_id = sa.Column(sa.Integer, sa.ForeignKey("questions.id"))  # Add ForeignKey constraint
    question = sa_orm.relationship("Question", back_populates="answer")

    def __repr__(self: DeclarativeBase) -> str:
        columns = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        return f"{self.__class__.__name__}({', '.join(f'{k}={v!r}' for k, v in columns.items())})"
