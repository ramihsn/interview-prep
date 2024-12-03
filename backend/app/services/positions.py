from sqlmodel import Session

from ..models.positions import Position as PositionModel
from ..schemas.positions import PositionRead, PositionCreate
from . import helpers


async def get_positions(db: Session, skip: int = 0, limit: int = 100) -> list[PositionRead]:
    return await helpers.get_items(db, PositionModel, PositionRead, skip, limit)


async def get_position(db: Session, position_id: int) -> PositionRead | None:
    return await helpers.get_item(db, PositionModel, PositionRead, position_id)


async def create_position(db: Session, position: PositionCreate) -> PositionRead:
    return await helpers.create_item(db, PositionModel, PositionRead, position)


async def update_position(db: Session, position_id: int, position: PositionCreate
                          ) -> PositionRead | None:
    return await helpers.update_item(db, PositionModel, PositionRead, position_id, position)


async def delete_position(db: Session, position_id: int) -> PositionRead | None:
    return await helpers.delete_item(db, PositionModel, PositionRead, position_id)
