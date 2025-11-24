from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel

class AssetBase(BaseModel):
    name: str
    description: Optional[str] = None
    type: str
    value: float = 0.0
    location: Optional[str] = None
    purchase_date: Optional[datetime] = None

class AssetCreate(AssetBase):
    pass

class AssetRead(AssetBase):
    id: UUID
    created_at: datetime

    class Config:
        from_attributes = True
