from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.donation import donation_crud
from app.core.db import get_async_session
from app.core.user import current_superuser, current_user
from app.schemas.donation import (
    DonationCreate, UserDonationsRead, SuperUserDonationRead
)
from app.models import User, Donation

router = APIRouter()


@router.get(
    '/',
    response_model=list[SuperUserDonationRead],
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)]
)
async def get_all_donations(
    session: AsyncSession = Depends(get_async_session)
):
    """
    Только для суперюзеров.
    Возвращает список всех пожертвований.
    """

    all_donations = await donation_crud.read_all(session)

    return all_donations


@router.get(
    '/me',
    response_model=list[UserDonationsRead],
    response_model_exclude_none=True,
)
async def get_my_donations(
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session)
):
    """Вернуть список пожертвований пользователя, выполняющего запрос."""

    my_donations = await donation_crud.get_user_donations(user.id, session)

    return my_donations


@router.post(
    '/',
    response_model=UserDonationsRead,
    response_model_exclude_none=True
)
async def create_donation(
    donation: DonationCreate,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    """Создание пожертвования."""

    new_donation = await donation_crud.create(donation, session, user)

    return new_donation
