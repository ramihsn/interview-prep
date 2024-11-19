from sqlmodel import Session, create_engine

# TODO: change to environment variable
DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})


def get_db():
    with Session(engine) as session:
        yield session
