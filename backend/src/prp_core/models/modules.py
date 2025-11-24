from sqlalchemy import Column, Boolean, String, Table
from . import metadata

modules = Table(
    "modules",
    metadata,
    Column("name", String, primary_key=True),
    Column("is_enabled", Boolean, default=True, nullable=False),
)
