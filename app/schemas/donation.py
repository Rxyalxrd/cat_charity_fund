from datetime import datetime
from typing import Optional

from pydantic import Field

from .base_schemas import BaseDonationsSchemas


class DonationCreate(BaseDonationsSchemas):
    """Схема пожертвования для создания."""

    class Config:
        title = 'Схема пожертвования для создания'
        schema_extra = {
            'example': {
                'comment': 'От всей души',
                'full_amount': 450
            }
        }


class UserDonationsRead(BaseDonationsSchemas):
    """
    Схема для получения списка пожертвований пользователя, выполняющего запрос.
    """

    id: int = Field(..., title='id пожертвования')
    create_date: datetime = Field(..., title='Дата внесения пожертвования')

    class Config:
        title = 'Схема пожертвования для получения'
        orm_mode = True
        schema_extra = {
            'example': {
                'comment': 'От всей души',
                'full_amount': 450,
                'id': 2,
                'create_date': '2023-07-21T23:54:05.177Z'
            }
        }


class SuperUserDonationRead(BaseDonationsSchemas):
    """
    Только для суперюзеров.
    Схема для возврата списока всех пожертвований.
    """

    user_id: Optional[int] = Field(None, title='ID пользователя')
    invested_amount: int = Field(..., title='Сколько вложено')
    fully_invested: bool = Field(False, title='Вложена полная сумма')
    close_date: Optional[datetime] = Field(None, title='Дата вложения')

    class Config:
        title = 'Схема пожертвования для получения (advanced)'
        orm_mode = True
        schema_extra = {
            'example': {
                'comment': 'От всей души',
                'full_amount': 450,
                'id': 2,
                'create_date': '2023-07-21T23:54:05.177Z',
                'user_id': 1,
                'invested_amount': 200,
                'fully_invested': 0
            }
        }
