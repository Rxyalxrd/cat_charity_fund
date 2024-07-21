from fastapi import APIRouter

from app.crud.crud import CRUD
from app.schemas.charity_projects import CharityProjectsCreate

router = APIRouter()


@router.post('/')
async def create_new_charity_projects(charity_projects: CharityProjectsCreate):

    new_charity_project = await CRUD.create(charity_projects)
    return new_charity_project