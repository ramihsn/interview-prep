from sqlmodel import SQLModel, Session, select
from typing import Type


async def get_items(db: Session, model: Type[SQLModel], read_schema: Type[SQLModel], skip: int = 0, limit: int = 100
                    ) -> list[SQLModel]:
    q = select(model)

    if skip and skip > 0:
        q = q.offset(skip)

    if limit and limit > 0:
        q = q.limit(limit)

    return [read_schema.model_validate(i) for i in db.exec(q).all()]


async def get_item(db: Session, model: Type[SQLModel], read_schema: Type[SQLModel], item_id: int) -> SQLModel | None:
    if item := db.get(model, item_id):
        return read_schema.model_validate(item)


async def create_item(db: Session, model: Type[SQLModel], read_schema: Type[SQLModel], item: SQLModel) -> SQLModel:
    item_obj = model(**item.model_dump())
    db.add(item_obj)
    db.commit()
    db.refresh(item_obj)
    return read_schema.model_validate(item_obj)


async def update_item(db: Session, model: Type[SQLModel], read_schema: Type[SQLModel], item_id: int, item: SQLModel
                      ) -> SQLModel | None:
    if old_item := db.get(model, item_id):
        for field, value in item.model_dump().items():
            if value is not None:
                setattr(old_item, field, value)

        db.commit()
        db.refresh(old_item)
        return read_schema.model_validate(old_item)


async def delete_item(db: Session, model: Type[SQLModel], read_schema: Type[SQLModel], item_id: int) -> SQLModel | None:
    if not (item := db.get(model, item_id)):
        raise ValueError(f"{model.__name__} does not exist")

    db.delete(item)
    db.commit()
    return read_schema.model_validate(item)
