from fastapi import FastAPI

from app.core.cfg import settings


app = FastAPI(title=settings.app_title)
