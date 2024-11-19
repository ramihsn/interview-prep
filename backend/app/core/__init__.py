from fastapi import FastAPI
import sqlmodel

# from app.db import base, session
from app.db import session


import contextlib


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    # base.Base.metadata.create_all(bind=session.engine)
    sqlmodel.SQLModel.metadata.create_all(session.engine)
    yield
