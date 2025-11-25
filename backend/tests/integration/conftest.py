
import asyncio
import os
from typing import Generator

import pytest
from fastapi.testclient import TestClient

from prp_core.database import database, engine
from prp_core.main import app
from prp_core.models import metadata

# Set up the test database
@pytest.fixture(scope="function", autouse=True)
async def test_db_setup():
    """Set up and tear down the test database."""

    # Create tables
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)
    
    yield

    # Drop tables
    async with engine.begin() as conn:
        await conn.run_sync(metadata.drop_all)
    
    await engine.dispose()




@pytest.fixture
def client() -> Generator:
    """Get a TestClient instance that reads/writes to the test database."""
    with TestClient(app) as client:
        yield client
