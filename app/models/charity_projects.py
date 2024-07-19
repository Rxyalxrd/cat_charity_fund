from sqlalchemy import Column

from .base_model import BaseModel


class CharityProjects(BaseModel):
    """Модель проектов, доп. поля наследуются от BaseModel"""

    name = Column(...)
    description = Column(...)