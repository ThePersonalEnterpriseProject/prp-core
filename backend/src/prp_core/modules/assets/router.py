from datetime import datetime
from typing import List
from uuid import UUID, uuid4

from fastapi import APIRouter, Depends, HTTPException

from ...dependencies import require_module
from ...database import database
from . import models, schemas

router = APIRouter(
    prefix="/assets",
    tags=["assets"],
    dependencies=[Depends(require_module("assets"))]
)

@router.post("/", response_model=schemas.AssetRead, status_code=201)
async def create_asset(asset: schemas.AssetCreate):
    new_id = uuid4()
    now = datetime.utcnow()
    insert_query = models.assets.insert().values(
        id=new_id, 
        created_at=now, 
        **asset.model_dump()
    )
    await database.execute(insert_query)
    return {**asset.model_dump(), "id": new_id, "created_at": now}

@router.get("/", response_model=List[schemas.AssetRead])
async def read_assets(skip: int = 0, limit: int = 100):
    select_query = models.assets.select().offset(skip).limit(limit)
    return await database.fetch_all(select_query)

@router.get("/{asset_id}", response_model=schemas.AssetRead)
async def read_asset(asset_id: UUID):
    select_query = models.assets.select().where(models.assets.c.id == asset_id)
    asset = await database.fetch_one(select_query)
    if asset is None:
        raise HTTPException(status_code=404, detail="Asset not found")
    return asset

@router.put("/{asset_id}", response_model=schemas.AssetRead)
async def update_asset(asset_id: UUID, asset: schemas.AssetCreate):
    # Check if exists
    select_query = models.assets.select().where(models.assets.c.id == asset_id)
    existing = await database.fetch_one(select_query)
    if existing is None:
        raise HTTPException(status_code=404, detail="Asset not found")

    update_query = (
        models.assets.update()
        .where(models.assets.c.id == asset_id)
        .values(**asset.model_dump())
    )
    await database.execute(update_query)
    return {**asset.model_dump(), "id": asset_id, "created_at": existing["created_at"]}

@router.delete("/{asset_id}", status_code=204)
async def delete_asset(asset_id: UUID):
    delete_query = models.assets.delete().where(models.assets.c.id == asset_id)
    await database.execute(delete_query)
    return None
