import random
import uuid
from datetime import datetime, timedelta

from faker import Faker
from prp_core.database import database
from prp_core.models import accounts, transactions

fake = Faker()

async def clear_data():
    """Wipes finance data from the database."""
    await database.execute("TRUNCATE TABLE transactions CASCADE")
    await database.execute("TRUNCATE TABLE accounts CASCADE")

async def _create_transactions(account_id: uuid.UUID, num_transactions: int = 20):
    """Generates random transactions for a given account."""
    for _ in range(num_transactions):
        # Randomize date within last 90 days
        date = fake.date_between(start_date='-90d', end_date='today')
        
        # Randomize amount (mostly negative for expenses, occasional positive for income)
        if random.random() < 0.2:
            amount = random.uniform(1000.0, 5000.0) # Income
            description = fake.company() + " Payroll"
        else:
            amount = random.uniform(-200.0, -10.0) # Expense
            description = fake.company()
            
        query = transactions.insert().values(
            id=uuid.uuid4(),
            account_id=account_id,
            date=date,
            amount=round(amount, 2),
            description=description,
        )
        await database.execute(query)

async def seed(scenario: str):
    await clear_data()

    accounts_data = []
    
    if scenario == "young_professional":
        accounts_data = [
            {"id": uuid.uuid4(), "name": "Chase Checking", "account_type": "Asset", "balance": 3500.00},
            {"id": uuid.uuid4(), "name": "Ally Savings", "account_type": "Asset", "balance": 10000.00},
            {"id": uuid.uuid4(), "name": "Chase Sapphire", "account_type": "Liability", "balance": 450.00},
            {"id": uuid.uuid4(), "name": "Navient Student Loan", "account_type": "Liability", "balance": 25000.00},
        ]
    elif scenario == "family":
        accounts_data = [
            {"id": uuid.uuid4(), "name": "Joint Checking", "account_type": "Asset", "balance": 8000.00},
            {"id": uuid.uuid4(), "name": "High Yield Savings", "account_type": "Asset", "balance": 45000.00},
            {"id": uuid.uuid4(), "name": "Vanguard 401k", "account_type": "Asset", "balance": 150000.00},
            {"id": uuid.uuid4(), "name": "Wells Fargo Mortgage", "account_type": "Liability", "balance": 350000.00},
            {"id": uuid.uuid4(), "name": "Toyota Financial", "account_type": "Liability", "balance": 18000.00},
        ]
    elif scenario == "small_business":
        accounts_data = [
            {"id": uuid.uuid4(), "name": "Business Checking", "account_type": "Asset", "balance": 25000.00},
            {"id": uuid.uuid4(), "name": "Personal Checking", "account_type": "Asset", "balance": 5000.00},
            {"id": uuid.uuid4(), "name": "Amex Business", "account_type": "Liability", "balance": 3200.00},
            {"id": uuid.uuid4(), "name": "SBA Loan", "account_type": "Liability", "balance": 50000.00},
        ]

    for acc in accounts_data:
        query = accounts.insert().values(**acc)
        await database.execute(query)
        
        # Generate transactions based on account name (simplified logic from original)
        if "Checking" in acc["name"] or "Sapphire" in acc["name"] or "Amex" in acc["name"] or "Toyota" in acc["name"]:
             num = 40 if scenario == "family" else 25
             await _create_transactions(acc["id"], num_transactions=num)
