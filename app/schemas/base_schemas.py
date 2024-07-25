from typing import Optional

from pydantic import BaseModel, Field, PositiveInt

from app.constants import MAX_LENGTH_FOR_NAME


class BaseDonationsSchemas(BaseModel):

    full_amount: PositiveInt = Field(..., title='Сумма пожертвования')
    comment: Optional[str] = Field(None, title='Комментарий к пожертвоанию')

    class Config:

        title = 'Базовая схема для пожертвований'


class BaseCharityProjectsSchemas(BaseModel):

    name: str = Field(
        ..., title='Название проекта', min_length=1, max_length=MAX_LENGTH_FOR_NAME
    )
    description: str = Field(..., title='Описание проекта')
    full_amount: PositiveInt = Field(..., title='Сумма пожертвования')

    class Config:

        title = 'Базовая схема для проектов'
