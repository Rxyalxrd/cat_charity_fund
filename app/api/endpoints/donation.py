from fastapi import APIRouter, Depends

from app.crud.donation import donation_crud
from app.core.db import get_async_session
from app.core.user import current_superuser, current_user
from app.schemas.donation import (
    DonationCreate, UserDonationsRead, SuperUserDonationRead
)
from app.models import User, Donation


router = APIRouter()


@router.get()
async def get_all_donations():
    """
    Только для суперюзеров.
    Возвращает список всех пожертвований.
    """

    pass


@router.get()
async def get_user_donations():
    """Вернуть список пожертвований пользователя, выполняющего запрос."""

    pass


@router.post()
async def create_donation():
    """Create Donation"""

    pass
