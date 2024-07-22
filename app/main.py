from fastapi import FastAPI

from app.core.cfg import settings
from app.api.endpoints import router

app = FastAPI(title=settings.app_title)
app.include_router(router)