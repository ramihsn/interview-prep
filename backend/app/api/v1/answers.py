import logging

from app.services import answers as services
from app.schemas import answers as schemas
from . import _api_factory

logger = logging.getLogger(__name__)
router = _api_factory.factory('answer', logger, services, schemas)
