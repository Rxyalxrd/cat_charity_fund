from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .base_crud import CRUD
from app.models.charity_projects import CharityProjects


class CRUDCharityProject(CRUD):
    """Расширенный CRUD класс для проектов."""

    async def get_project_id_by_name(
            self,
            project_name: str,
            session: AsyncSession,
    ) -> Optional[int]:
        """Поиск id проекта по имени."""

        db_project_id = await session.execute(
            select(CharityProjects.id).where(
                CharityProjects.name == project_name
            )
        )

        return db_project_id.scalars().first()


charity_project_crud = CRUDCharityProject(CharityProjects)
