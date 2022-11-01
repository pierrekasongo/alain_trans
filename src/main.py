from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from src.routes.api import router as api_router

from src.utils.my_logger import logger

import src.database.db_session as db_session

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)


# Application events
@app.on_event("startup")
async def startup():

    try:
        logger.info("Connecting to database ...")
        db_session.global_init()
        logger.info("You are connected to database")
    except Exception as e:
        logger.error("connecting to database")(
            "error", e.__cause__
        )