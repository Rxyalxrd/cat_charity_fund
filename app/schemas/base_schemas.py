from typing import Optional

from pydantic import BaseModel, Field, PositiveInt

from app.constants import MAX_LENGTH_FOR_NAME


class PreBaseSchemasMixin(BaseModel):

    full_amount: PositiveInt = Field(..., title='Сумма пожертвования')


class BaseDonationsSchemas(PreBaseSchemasMixin):

    comment: Optional[str] = Field(None, title='Комментарий к пожертвоанию')

    class Config:

        title = 'Базовая схема для пожертвований'


class BaseCharityProjectsSchemas(PreBaseSchemasMixin):

    name: str = Field(
        ..., title='Название проекта', max_length=MAX_LENGTH_FOR_NAME
    )
    description: str = Field(..., title='Описание проекта')

    class Config:

        title = 'Базовая схема для проектов'
