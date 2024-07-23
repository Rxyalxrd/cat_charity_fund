from datetime import datetime
from pydantic import Field, validator

from .base_schemas import BaseCharityProjectsSchemas


class CharityProjectsCreate(BaseCharityProjectsSchemas):
    """Схема для создания проекта"""

    class Config:
        title = 'Схема проектов для POST запросов'
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

    class Config:
        title = 'Схема проектов для POST запросов'
        orm_mode = True
        schema_extra = {
            'example': {
                'name': '2 котикам на курсы',
                'description': 'Курс для обучения на yandex practicum',
                'full_amount': 100000
            }
        }


class CharityProjectsRead(BaseCharityProjectsSchemas):
    """Схема для чтения проекта"""

    id: int = Field(..., title='id пользователя')
    invested_amount: int = Field(..., title='Отправленная сумма')
    fully_invested: bool = Field(..., title='Собрана ли сумма')
    create_date: datetime = Field(..., title='Время создания')
    close_date: datetime = Field(None, title='Время завершения')

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
