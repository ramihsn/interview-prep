import logging

from app.services import positions as services
from app.schemas import positions as schemas
from . import _api_factory

logger = logging.getLogger(__name__)
router = _api_factory.factory('position', logger, services, schemas)
