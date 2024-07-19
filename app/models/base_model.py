from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer

from app.core.db import Base


class BaseModel(Base):
    """Базовая модель для projects.py и donations.py"""

    full_amount = Column(...)
    invested_amount = Column(...)
    fully_invested = Column(...)
    create_date = Column(...)
    close_date = Column(...)
