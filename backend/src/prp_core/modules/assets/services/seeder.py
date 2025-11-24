import random
import uuid
from datetime import datetime

from faker import Faker
from prp_core.database import database
from prp_core.modules.assets.models import assets

fake = Faker()

async def clear_data():
    """Wipes assets data from the database."""
    await database.execute("TRUNCATE TABLE assets CASCADE")

async def seed(scenario: str):
    await clear_data()

    assets_data = []
    
    if scenario == "young_professional":
        assets_data = [
            {"name": "MacBook Pro", "type": "Electronics", "value": 2500.00, "location": "Home Office"},
            {"name": "Honda Civic", "type": "Vehicle", "value": 18000.00, "location": "Parking Lot"},
            {"name": "IKEA Desk", "type": "Furniture", "value": 200.00, "location": "Home Office"},
        ]
    elif scenario == "family":
        assets_data = [
            {"name": "Toyota Highlander", "type": "Vehicle", "value": 35000.00, "location": "Garage"},
            {"name": "Samsung TV", "type": "Electronics", "value": 1200.00, "location": "Living Room"},
            {"name": "Washer/Dryer", "type": "Appliance", "value": 1500.00, "location": "Laundry Room"},
            {"name": "Lawn Mower", "type": "Tools", "value": 400.00, "location": "Shed"},
        ]
    elif scenario == "small_business":
        assets_data = [
            {"name": "Ford F-150", "type": "Vehicle", "value": 45000.00, "location": "Job Site"},
            {"name": "Dell Server", "type": "Electronics", "value": 5000.00, "location": "Server Room"},
            {"name": "Office Furniture Set", "type": "Furniture", "value": 3000.00, "location": "Office"},
            {"name": "Inventory Stock", "type": "Inventory", "value": 15000.00, "location": "Warehouse"},
        ]

    for asset in assets_data:
        query = assets.insert().values(
            id=uuid.uuid4(),
            created_at=datetime.utcnow(),
            **asset
        )
        await database.execute(query)
