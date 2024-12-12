import sqlmodel

from ..models.positions import Position as PositionRead  # noqa: F401
from . import helpers


class _BasePosition(sqlmodel.SQLModel):
    company: str
    title: str
    description: str


class PositionCreate(_BasePosition):
    pass


PositionUpdate = helpers.make_optional(_BasePosition)
