import sqlalchemy as sa
import sqlalchemy.orm as orm
from dotenv import load_dotenv
import os
from pathlib import Path

from src.utils.my_logger import logger
from src.models.model import Base


load_dotenv()

factory = None


BASE_PATH = Path(__file__).resolve().parent


DATABASE_URL = "postgresql://{0}:{1}@{2}:{3}/{4}".format(
    os.getenv("DB_USER"),
    os.getenv("DB_PWD"),
    os.getenv("DB_HOST"),
    os.getenv("DB_PORT"),
    os.getenv("DB_NAME"),
)

def global_init():
    global factory

    if factory:
        return
    engine = sa.create_engine(DATABASE_URL, echo=False)
    factory = orm.sessionmaker(bind=engine)

    Base.metadata.create_all(engine)
