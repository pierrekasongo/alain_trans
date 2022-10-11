from fastapi import FastAPI

from src.routes.api import router as api_router

from src.utils.my_logger import logger

app = FastAPI()

app.include_router(api_router)