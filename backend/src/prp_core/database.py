import os
import databases
import sqlalchemy
from sqlalchemy.ext.asyncio import create_async_engine

DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_HOST = os.getenv("POSTGRES_HOST", "db")
DB_NAME = os.getenv("POSTGRES_DB")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")

if all([DB_USER, DB_PASSWORD, DB_NAME]):
    DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    engine_args = {}
else:
    DATABASE_URL = "sqlite+aiosqlite:///./test.db"
    engine_args = {"connect_args": {"check_same_thread": False}}

engine = create_async_engine(DATABASE_URL, **engine_args)
database = databases.Database(DATABASE_URL)
