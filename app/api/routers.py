from fastapi import APIRouter

from app.api.endpoints import charity_project, donation, user

main_router = APIRouter()

main_router.include_router(
    charity_project,
    prefix='/charity_project',
    tags=('Charity project'),
)
main_router.include_router(
    donation,
    prefix='/donation',
    tags=('Donation'),
)
main_router.include_router(user)
