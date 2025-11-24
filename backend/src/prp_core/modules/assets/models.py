import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, Float, String, Table
from sqlalchemy.dialects.postgresql import UUID

from ...models import metadata

assets = Table(
    "assets",
    metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    Column("name", String, nullable=False),
    Column("description", String, nullable=True),
    Column("type", String, nullable=False),  # e.g., Vehicle, Electronics
    Column("value", Float, default=0.0, nullable=False),
    Column("location", String, nullable=True),
    Column("purchase_date", DateTime, nullable=True),
    Column("created_at", DateTime, default=datetime.utcnow, nullable=False),
)
