from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.charity_projects import charity_project_crud
from app.schemas.charity_projects import CharityProjectsCreate
from app.core.db import get_async_session

router = APIRouter()


@router.post('/')
async def create_new_charity_projects(
    charity_projects: CharityProjectsCreate,
    session: AsyncSession = Depends(get_async_session)
):

    new_charity_project = await charity_project_crud.create(charity_projects, session)
    return new_charity_project