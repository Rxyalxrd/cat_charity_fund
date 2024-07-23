from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .base_crud import CRUD
from app.models.donation import Donation
# from app.models.user import User


class CRUDDonation(CRUD):
    """Расширенный CRUD класс для пожертвований."""

    async def get_user_donations(
        self,
        user_id: int,
        session: AsyncSession
    ):
        """Поиск пожертвований по id пользователя"""

        donations = await session.execute(
            select(Donation).where(Donation.user_id == user_id)
        )

        return donations.scalars().all()


donation_crud = CRUDDonation(Donation)
