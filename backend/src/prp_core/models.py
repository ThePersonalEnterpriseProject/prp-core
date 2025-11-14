import uuid
from datetime import datetime

import sqlalchemy
from sqlalchemy import Column, DateTime, Enum, Float, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID

from .schemas import AccountType

metadata = sqlalchemy.MetaData()

accounts = sqlalchemy.Table(
    "accounts",
    metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    Column("name", String, nullable=False),
    Column("account_type", Enum(AccountType), nullable=False),
    Column("balance", Float, default=0.0, nullable=False),
)

transactions = sqlalchemy.Table(
    "transactions",
    metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    Column("date", DateTime, default=datetime.utcnow, nullable=False),
    Column("description", String, nullable=False),
    Column("amount", Float, nullable=False),
    Column("account_id", UUID(as_uuid=True), ForeignKey("accounts.id"), nullable=False),
)
