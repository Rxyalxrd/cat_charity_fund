from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable

from app.core.db import Base


class Users(SQLAlchemyBaseUserTable[int], Base):
    """Модель пользователей, используется стандартная модель"""
    pass