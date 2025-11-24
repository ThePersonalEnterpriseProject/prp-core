from typing import List
from uuid import UUID, uuid4

from fastapi import APIRouter, HTTPException

from .... import models, schemas
from ....database import database

router = APIRouter()

@router.post("/accounts/", response_model=schemas.AccountRead, status_code=201)
async def create_account(account: schemas.AccountCreate):
    new_id = uuid4()
    insert_query = models.accounts.insert().values(id=new_id, **account.model_dump())
    await database.execute(insert_query)
    return {**account.model_dump(), "id": new_id}


@router.get("/accounts/", response_model=List[schemas.AccountRead])
async def read_accounts(skip: int = 0, limit: int = 100):
    select_query = models.accounts.select().offset(skip).limit(limit)
    return await database.fetch_all(select_query)


@router.get("/accounts/{account_id}", response_model=schemas.AccountRead)
async def read_account(account_id: UUID):
    select_query = models.accounts.select().where(models.accounts.c.id == account_id)
    account = await database.fetch_one(select_query)
    if account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    return account


@router.put("/accounts/{account_id}", response_model=schemas.AccountRead)
async def update_account(account_id: UUID, account: schemas.AccountCreate):
    update_query = (
        models.accounts.update()
        .where(models.accounts.c.id == account_id)
        .values(**account.model_dump())
    )
    await database.execute(update_query)
    return {**account.model_dump(), "id": account_id}


@router.delete("/accounts/{account_id}", status_code=204)
async def delete_account(account_id: UUID):
    delete_query = models.accounts.delete().where(models.accounts.c.id == account_id)
    await database.execute(delete_query)
    return None
