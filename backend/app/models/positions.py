import sqlmodel


class Position(sqlmodel.SQLModel, table=True):
    __tablename__ = "positions"  # if not set, table name will be the class name

    id: int = sqlmodel.Field(primary_key=True, index=True)
    company: str
    title: str
    description: str
