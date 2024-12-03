from sqlmodel import SQLModel
from typing import Optional


def make_optional(model: SQLModel) -> SQLModel:
    annotations = {
        key: Optional[typ] for key, typ in model.__annotations__.items()
    }
    return type(f"{model.__name__}Optional", (SQLModel,), {
        "__annotations__": annotations,
        **{key: None for key in annotations},  # Set default values
    })
