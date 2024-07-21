from typing import Union, Optional

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.encoders import jsonable_encoder
from sqlalchemy import select

from models import CharityProjects, Donations, Users


class CRUD:
    """Реализация работы с БД: Create, Read, Update, Delete"""

    def __init__(
        self,
        model: Union[CharityProjects, Donations, Users]
    ) -> None:

        self.model = model

    async def create(
        self,
        request: Union[CharityProjects, Donations, Users],
        session: AsyncSession
    ) -> Union[CharityProjects, Donations, Users]:
        """Создание новой записи в БД"""

        data_in_request = request.dict()
        data_to_db = self.model(**data_in_request)
        session.add(data_to_db)
        await session.commit()
        await session.refresh(data_to_db)

        return data_to_db

    async def read(
        self,
        record_id: int,
        session: AsyncSession
    ) -> Optional[Union[CharityProjects, Donations, Users]]:
        """Чтение записи из БД по ID"""

        response = await session.get(self.model, record_id)

        return response

    async def read_all(
        self,
        session: AsyncSession
    ) -> Optional[Union[CharityProjects, Donations, Users]]:
        """Чтение всех записей из БД"""

        all_records = await session.execute(select(self.model))

        return all_records.scalars().all()

    async def update(
        self,
        db_record: Union[CharityProjects, Donations, Users],
        request: Union[CharityProjects, Donations, Users],
        session: AsyncSession
    ) -> Union[CharityProjects, Donations, Users]:
        """Обновление записи в БД"""

        db_record_data = jsonable_encoder(db_record)
        update_data = request.dict(exclude_unset=True)

        for field in db_record_data:
            if field in update_data:
                setattr(db_record, field, update_data[field])

        session.add(db_record)
        await session.commit()
        await session.refresh(db_record)
        return db_record

    async def delete(
        self,
        model_in_db: Union[CharityProjects, Donations, Users],
        session: AsyncSession
    ) -> Union[CharityProjects, Donations, Users]:
        """Удаление записи из БД"""

        await session.delete(model_in_db)
        await session.commit()
        return model_in_db
