from typing import Optional
from datetime import datetime
from pydantic import Field, validator, PositiveInt, Extra
from .base_schemas import BaseCharityProjectsSchemas
from app.constants import MAX_LENGTH_FOR_NAME, MIN_LENGTH_FOR_NAME


class CharityProjectsCreate(BaseCharityProjectsSchemas):
    """Схема для создания проекта"""

    class Config:
        title = 'Схема проектов для POST запросов'
        extra = Extra.forbid
        schema_extra = {
            'example': {
                'name': 'Котику на курсы',
                'description': 'Курс для обучения на yandex practicum',
                'full_amount': 1000
            }
        }

    @validator('name')
    def name_cannot_be_null(cls, value: str):

        if not value:
            raise ValueError('Название проекта не может быть пустым!')

        return value

    @validator('description')
    def description_can_not_be_null(cls, value: str):

        if not value:
            raise ValueError('Описание проекта не может быть пустым!')

        return value

    @validator('full_amount')
    def full_amount_can_not_be_lt_zero(cls, value: str):

        if int(value) < 0:
            raise ValueError('Сумма пожертвования должна быть > 0')

        return value


class CharityProjectsUpdate(BaseCharityProjectsSchemas):
    """Схема для обновления проекта"""

    name: str = Field(
        None,
        title='Название проекта',
        min_length=MIN_LENGTH_FOR_NAME,
        max_length=MAX_LENGTH_FOR_NAME
    )
    description: str = Field(None, title='Описание проекта')
    full_amount: PositiveInt = Field(None, title='Сумма пожертвования')

    class Config:
        title = 'Схема проектов для POST запросов'
        orm_mode = True
        extra = Extra.forbid
        schema_extra = {
            'example': {
                'name': '2 котикам на курсы',
                'description': 'Курс для обучения на yandex practicum',
                'full_amount': 100000
            }
        }

    @validator('name')
    def name_cannot_be_null(cls, value: str):

        if not value:
            raise ValueError('Название проекта не может быть пустым!')

        return value

    @validator('description')
    def description_can_not_be_null(cls, value: str):

        if not value:
            raise ValueError('Описание проекта не может быть пустым!')

        return value


class CharityProjectsRead(BaseCharityProjectsSchemas):
    """Схема для чтения проекта"""

    id: int = Field(..., title='id пользователя')
    invested_amount: int = Field(..., title='Отправленная сумма')
    fully_invested: bool = Field(False, title='Собрана ли сумма')
    create_date: datetime = Field(..., title='Время создания')
    close_date: Optional[datetime] = Field(None, title='Время завершения')

    class Config:
        title = 'Схема проекта для получения'
        orm_mode = True
        schema_extra = {
            'example': {
                'name': 'Песики - наше все',
                'description': 'очень хочу им помочь',
                'full_amount': 1500,
                'id': 19,
                'invested_amount': 360,
                'fully_invested': 0,
                'create_date': '2023-07-22T02:18:40.662286'
            }
        }
