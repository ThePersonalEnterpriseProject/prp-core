import os

import databases
from sqlalchemy.ext.asyncio import create_async_engine

DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_HOST = os.getenv("POSTGRES_HOST", "db")
DB_NAME = os.getenv("POSTGRES_DB")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")



print(f"DEBUG: database.py loaded from {__file__}")
print(f"DEBUG: TESTING={os.getenv('TESTING')}")
if os.getenv("USE_SQLITE") or os.getenv("PRP_DESKTOP_MODE"):
    print("DEBUG: Using SQLite for TESTING/DESKTOP")
    if os.getenv("PRP_DESKTOP_MODE"):
        # Store DB in user data directory or local folder for now
        DATABASE_URL = "sqlite+aiosqlite:///./prp_core.db"
    else:
        DATABASE_URL = "sqlite+aiosqlite:///./test.db"
    engine_args = {"connect_args": {"check_same_thread": False}}
elif all([DB_USER, DB_PASSWORD, DB_NAME]):
    DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    engine_args = {}
else:
    DATABASE_URL = "sqlite+aiosqlite:///./test.db"
    engine_args = {"connect_args": {"check_same_thread": False}}

engine = create_async_engine(DATABASE_URL, **engine_args)
database = databases.Database(DATABASE_URL, **engine_args)
