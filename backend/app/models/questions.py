from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import orm as sa_orm
import sqlalchemy as sa

from app.db.base import Base


class Question(Base):
    __tablename__ = "questions"

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    topic = sa.Column(sa.String)
    difficulty = sa.Column(sa.String)
    question = sa.Column(sa.String)
    answered = sa.Column(sa.Boolean, default=False)

    # Relationship to Answer with nullable=True
    answer = sa_orm.relationship("Answer", back_populates="question", uselist=False, cascade="all, delete-orphan")

    def __repr__(self: DeclarativeBase) -> str:
        columns = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        repr_str = f"{self.__class__.__name__}({', '.join(f'{k}={v!r}' for k, v in columns.items())}"
        return repr_str
