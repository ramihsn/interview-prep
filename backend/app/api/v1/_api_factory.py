from fastapi import APIRouter, HTTPException, status, Depends, Path
from sqlmodel import SQLModel
from types import ModuleType
from logging import Logger
import functools

from ...db.session import get_db


class Service:
    def __init__(self, name: str, service_module: ModuleType):
        self.name = name
        self.service_module = service_module

    def get_item(self, *args, **kwargs):
        return getattr(self.service_module, f'get_{self.name}')(*args, **kwargs)

    def get_items(self, *args, **kwargs):
        return getattr(self.service_module, f'get_{self.name}s')(*args, **kwargs)

    def create_item(self, *args, **kwargs):
        return getattr(self.service_module, f'create_{self.name}')(*args, **kwargs)

    def update_item(self, *args, **kwargs):
        return getattr(self.service_module, f'update_{self.name}')(*args, **kwargs)

    def delete_item(self, *args, **kwargs):
        return getattr(self.service_module, f'delete_{self.name}')(*args, **kwargs)


class SchemaModule:
    read: SQLModel
    create: SQLModel
    update: SQLModel

    def __init__(self, name: str, schema_module: ModuleType):
        self.name = name.capitalize()
        self.schema_module = schema_module

        # Access the schema classes
        self.read = getattr(self.schema_module, f'{self.name}Read')
        self.create = getattr(self.schema_module, f'{self.name}Create')
        self.update = getattr(self.schema_module, f'{self.name}Update', self.create)


def _wrap_factory(func):
    @functools.wraps(func)
    def wrapper(name: str, logger: Logger, service: ModuleType, schema_module: ModuleType):
        _service = Service(name, service)
        _schema_module = SchemaModule(name, schema_module)
        return func(name, logger, _service, _schema_module)
    return wrapper


@_wrap_factory
def factory(name: str, logger: Logger, service: Service, schema_module: SchemaModule) -> APIRouter:
    if name.endswith('s'):
        router = APIRouter(prefix=f'/{name}')
    else:
        router = APIRouter(prefix=f'/{name}s')

    # Dependency to get item by ID
    async def get_item_or_404(
        id: int = Path(..., description=f"The ID of the {name}"),
        db=Depends(get_db),
    ):
        logger.info(f"Fetching {name} with id {id}")
        try:
            item = await service.get_item(db, id)
            if item is None:
                raise HTTPException(status_code=404, detail=f"{name.capitalize()} not found")
            return item
        except Exception as e:
            logger.error(f"Error fetching {name} with id {id}: {e}")
            raise HTTPException(status_code=500, detail="Internal Server Error")

    # Get All Items
    @router.get(
        path='/',
        response_model=list[schema_module.read],
        name=f"get_{name}s",
    )
    async def get_items(db=Depends(get_db)):
        items = await service.get_items(db)
        return items

    # Get Item by ID
    @router.get(
        path='/{id}',
        response_model=schema_module.read,
        name=f"get_{name}",
    )
    async def get_item(item=Depends(get_item_or_404)):
        return item

    # Create Item
    @router.post(
        path='/',
        response_model=schema_module.read,
        status_code=status.HTTP_201_CREATED,
        name=f"create_{name}",
    )
    async def create_item(
        item_in: schema_module.create,  # type: ignore
        db=Depends(get_db),
    ):
        item = await service.create_item(db, item_in)
        return item

    # Update Item
    @router.put(
        path='/{id}',
        response_model=schema_module.read,
        name=f"update_{name}",
    )
    async def update_item(
        id: int,
        item_update: schema_module.update,  # type: ignore
        db=Depends(get_db),
    ):
        updated_item = await service.update_item(db, id, item_update)
        return updated_item

    # Delete Item
    @router.delete(
        path='/{id}',
        status_code=status.HTTP_204_NO_CONTENT,
        name=f"delete_{name}",
    )
    async def delete_item(
        item=Depends(get_item_or_404),
        db=Depends(get_db),
    ):
        await service.delete_item(db, item.id)
        return None

    return router
