from fastapi import FastAPI

from app.core.config import settings
from app.api.endpoints import router
from app.core.init_db import create_first_superuser

app = FastAPI(title=settings.app_title)
app.include_router(router)


@app.on_event('startup')
async def startup():
    await create_first_superuser()
