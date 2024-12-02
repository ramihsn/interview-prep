import sqlmodel


class UserSettings(sqlmodel.SQLModel, table=True):
    __tablename__ = "user_settings"

    id: int = sqlmodel.Field(primary_key=True, index=True)
    theme: str = sqlmodel.Field(nullable=True)
    questions_group_by: str = sqlmodel.Field(nullable=True)
