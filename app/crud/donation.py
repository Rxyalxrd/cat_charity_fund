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

    def donate_in_charity_project(self, charity_project, donation, session):
        if charity_project.close_date is None:
            # Рассчитываем оставшиеся суммы для проекта и пожертвования
            remaining_funds = donation.full_amount - donation.invested_amount
            remaining_project_need = charity_project.full_amount - charity_project.invested_amount

            # Обновляем суммы инвестиций
            amount_to_invest = min(remaining_funds, remaining_project_need)
            charity_project.invested_amount += amount_to_invest
            donation.invested_amount += amount_to_invest

            # Закрываем проект, если он полностью профинансирован
            if charity_project.invested_amount >= charity_project.full_amount:
                self.close_invested(charity_project)

            # Закрываем пожертвование, если оно полностью израсходовано
            if donation.invested_amount >= donation.full_amount:
                self.close_invested(donation)

            # Сохраняем изменения в базе данных
            session.add(charity_project)
            session.add(donation)
            session.commit()
            session.refresh(charity_project)
            session.refresh(donation)

        return charity_project

    def close_invested(self, item):
        item.fully_invested = True
        item.close_date = datetime.now()
        return item

    async def get_invested_charity_project(self, charity_project, session: AsyncSession):
        invested_project = await session.execute(
            select(charity_project).where(
                charity_project.fully_invested == 0
            ).order_by(charity_project.create_date)
        )
        return invested_project.scalars().first()


donation_crud = CRUDDonation(Donation)
