import sqlalchemy
import databases
from sqlalchemy import Table
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os
from pathlib import Path

from src.utils.my_logger import logger


load_dotenv()


BASE_PATH = Path(__file__).resolve().parent


DATABASE_URL = "postgresql://{0}:{1}@{2}:{3}/{4}".format(
    os.getenv("DB_USER"),
    os.getenv("DB_PWD"),
    os.getenv("DB_HOST"),
    os.getenv("DB_PORT"),
    os.getenv("DB_NAME"),
)

Base = declarative_base()

db = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()


def get_engine():
    try:

        engine = sqlalchemy.create_engine(DATABASE_URL)

    except Exception as e:
        logger.error(
            "Cannot connect to the database, please provide all the information"
        )

    except:
        logger.error("Cannot connect to database %s", os.getenv("DB_NAME"))

    return engine


def get_session():
    return Session(get_engine())
