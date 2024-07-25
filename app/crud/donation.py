from typing import Optional, Union, Type
from datetime import datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .base_crud import CRUD
from app.models import CharityProject, Donation


class CRUDDonation(CRUD):
    """Расширенный CRUD класс для пожертвований."""

    async def get_user_donations(
        self,
        user_id: int,
        session: AsyncSession
    ):
        """Поиск пожертвований по id пользователя."""

        donations = await session.execute(
            select(Donation).where(Donation.user_id == user_id)
        )

        return donations.scalars().all()

    def distribution_of_resources(
            self,
            project_or_donation: Optional[Union[CharityProject, Donation]],
            funds: Union[CharityProject, Donation],
    ) -> Union[CharityProject, Donation]:
        """Распределине средств."""

        if project_or_donation:
            for item in project_or_donation:
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

    def close_invested(
            self,
            project_or_donation: Union[CharityProject, Donation]
    ) -> Union[CharityProject, Donation]:
        """Завершение сбора средств или транзакции."""

        project_or_donation.fully_invested = True
        project_or_donation.close_date = datetime.now()
        return project_or_donation

    async def get_invested_charity_projects(
            self,
            charity_project: Type[Union[CharityProject, Donation]],
            session: AsyncSession
    ) -> Optional[list[Union[CharityProject, Donation]]]:
        """
        Получение всех проектов, в которые нужно инвестировать
        или средств, которые не были проинвестированны."""

        invested_projects = await session.execute(
            select(charity_project).where(
                charity_project.fully_invested == 0
            ).order_by(charity_project.create_date)
        )
        return invested_projects.scalars().all()


donation_crud = CRUDDonation(Donation)
