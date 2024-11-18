from fastapi import FastAPI

from app.db import base, session

import contextlib


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    base.Base.metadata.create_all(bind=session.engine)
    yield
