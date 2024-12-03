from fastapi import FastAPI
# import sqlmodel

# from app.db import base, session
from app.db import session  # noqa


import contextlib


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    # XXX: if you want the DB to be updated automatically, uncomment one of the lines below
    # base.Base.metadata.create_all(bind=session.engine)  # this is used for SQLite
    # sqlmodel.SQLModel.metadata.create_all(session.engine)  # this is used for Postgres
    yield
