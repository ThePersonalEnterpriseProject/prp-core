from typing import List

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from .. import models
from ..database import database

router = APIRouter()

class ModuleRead(BaseModel):
    name: str
    is_enabled: bool

class ModuleUpdate(BaseModel):
    is_enabled: bool

@router.get("/modules/", response_model=List[ModuleRead])
async def read_modules():
    query = models.modules.select()
    return await database.fetch_all(query)

@router.put("/modules/{name}", response_model=ModuleRead)
async def update_module(name: str, module_update: ModuleUpdate):
    # Check if module exists
    query = models.modules.select().where(models.modules.c.name == name)
    module = await database.fetch_one(query)
    if not module:
        raise HTTPException(status_code=404, detail="Module not found")

    # Update module
    update_query = (
        models.modules.update()
        .where(models.modules.c.name == name)
        .values(is_enabled=module_update.is_enabled)
    )
    await database.execute(update_query)
    return {"name": name, "is_enabled": module_update.is_enabled}
