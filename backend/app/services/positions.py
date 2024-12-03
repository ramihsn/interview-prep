from sqlmodel import Session
import logging

from ..models.positions import Position as PositionModel
from ..schemas.positions import PositionRead, PositionCreate, PositionUpdate
from . import helpers

logger = logging.getLogger(__name__)


async def get_positions(db: Session, skip: int = 0, limit: int = 100) -> list[PositionRead]:
    logger.info("Getting positions")
    return await helpers.get_items(db, PositionModel, PositionRead, skip, limit)


async def get_position(db: Session, position_id: int) -> PositionRead | None:
    logger.info(f"Getting position with ID {position_id}")
    return await helpers.get_item(db, PositionModel, PositionRead, position_id)


async def create_position(db: Session, position: PositionCreate) -> PositionRead:
    logger.info(f"Creating a new position {position}")
    return await helpers.create_item(db, PositionModel, PositionRead, position)


async def update_position(db: Session, position_id: int, position: PositionUpdate  # type: ignore
                          ) -> PositionRead | None:
    logger.info(f"Updating position with ID {position_id} to {position}")
    return await helpers.update_item(db, PositionModel, PositionRead, position_id, position)


async def delete_position(db: Session, position_id: int) -> PositionRead | None:
    logger.info(f"Deleting position with ID {position_id}")
    if await helpers.delete_item(db, PositionModel, PositionRead, position_id):
        return

    logger.error("Position does not exist")
    raise ValueError("Position does not exist")
