from datetime import datetime

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

    def funds_distribution(
            self,
            opened_items,
            funds,
    ):
        if opened_items:
            for item in opened_items:
                funds_diff = funds.full_amount - funds.invested_amount
                item_diff = item.full_amount - item.invested_amount
                if funds_diff >= item_diff:
                    funds.invested_amount += item_diff
                    item.invested_amount = item.full_amount
                    self.close_invested(item)
                    if funds_diff == item_diff:
                        self.close_invested(funds)
                else:
                    item.invested_amount += funds_diff
                    funds.invested_amount = funds.full_amount
                    self.close_invested(funds)
                    break
        return funds

    def close_invested(self, item):
        item.fully_invested = True
        item.close_date = datetime.now()
        return item

    async def get_invested_charity_project(self, charity_project, session: AsyncSession):
        invested_projects = await session.execute(
            select(charity_project).where(
                charity_project.fully_invested == 0
            ).order_by(charity_project.create_date)
        )
        return invested_projects.scalars().all()


donation_crud = CRUDDonation(Donation)
