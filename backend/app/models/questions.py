import sqlalchemy as sa
from sqlalchemy.orm import DeclarativeBase

from app.db.base import Base


class Question(Base):
    __tablename__ = "questions"

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    topic = sa.Column(sa.String)
    difficulty = sa.Column(sa.String)
    question = sa.Column(sa.String)
    answered = sa.Column(sa.Boolean, default=False)

    def __repr__(self: DeclarativeBase):
        columns = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        repr_str = f"{self.__class__.__name__}({', '.join(f'{k}={v!r}' for k, v in columns.items())}"
        return repr_str
