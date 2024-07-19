from sqlalchemy import Column

from .base_model import BaseModel


class Donations(BaseModel):
    """Модель пожертвований, доп. поля наследуются от BaseModel"""

    user_id = Column(...)
    comment = Column(...)