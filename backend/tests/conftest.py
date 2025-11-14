
import asyncio
import os
from typing import Generator

import pytest
from fastapi.testclient import TestClient

from prp_core.database import database, engine
from prp_core.main import app
from prp_core.models import metadata

# Set up the test database
TEST_DATABASE_URL = "sqlite+aiosqlite:///./test.db"

@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for each test session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope="session", autouse=True)
async def test_db_setup():
    """Set up and tear down the test database."""
    # Use a separate test database
    os.environ["DATABASE_URL"] = TEST_DATABASE_URL

    # Create tables
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)

    await database.connect()
    yield
    await database.disconnect()

    # Drop tables
    async with engine.begin() as conn:
        await conn.run_sync(metadata.drop_all)

    if os.path.exists("./test.db"):
        os.remove("./test.db")


@pytest.fixture
def client() -> Generator:
    """Get a TestClient instance that reads/writes to the test database."""
    with TestClient(app) as client:
        yield client
