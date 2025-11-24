from datetime import datetime, timezone
from typing import List
from uuid import UUID, uuid4

from fastapi import APIRouter, HTTPException

from .... import models, schemas
from ....database import database

router = APIRouter()

@router.post("/transactions/", response_model=schemas.TransactionRead, status_code=201)
async def create_transaction(transaction: schemas.TransactionCreate):
    # Get the account
    select_query = models.accounts.select().where(
        models.accounts.c.id == transaction.account_id
    )
    account = await database.fetch_one(select_query)
    if account is None:
        raise HTTPException(status_code=404, detail="Account not found")

    # Update the account balance
    new_balance = account["balance"] + transaction.amount
    update_query = (
        models.accounts.update()
        .where(models.accounts.c.id == transaction.account_id)
        .values(balance=new_balance)
    )
    await database.execute(update_query)

    # Create the transaction
    new_id = uuid4()
    now = datetime.now(timezone.utc)
    insert_query = models.transactions.insert().values(
        id=new_id, date=now, **transaction.model_dump()
    )
    await database.execute(insert_query)
    return {**transaction.model_dump(), "id": new_id, "date": now}


@router.get("/transactions/", response_model=List[schemas.TransactionRead])
async def read_transactions(skip: int = 0, limit: int = 100):
    select_query = models.transactions.select().offset(skip).limit(limit)
    return await database.fetch_all(select_query)


@router.get("/transactions/{transaction_id}", response_model=schemas.TransactionRead)
async def read_transaction(transaction_id: UUID):
    select_query = models.transactions.select().where(
        models.transactions.c.id == transaction_id
    )
    transaction = await database.fetch_one(select_query)
    if transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction


@router.put("/transactions/{transaction_id}", response_model=schemas.TransactionRead)
async def update_transaction(
    transaction_id: UUID, transaction: schemas.TransactionCreate
):
    # Get the old transaction
    select_query = models.transactions.select().where(
        models.transactions.c.id == transaction_id
    )
    old_transaction = await database.fetch_one(select_query)
    if old_transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")

    # Get the account
    select_account_query = models.accounts.select().where(
        models.accounts.c.id == old_transaction["account_id"]
    )
    account = await database.fetch_one(select_account_query)
    if account is None:
        raise HTTPException(status_code=404, detail="Account not found")

    # Update the account balance
    new_balance = (
        account["balance"] - old_transaction["amount"] + transaction.amount
    )
    update_account_query = (
        models.accounts.update()
        .where(models.accounts.c.id == old_transaction["account_id"])
        .values(balance=new_balance)
    )
    await database.execute(update_account_query)

    # Update the transaction
    now = datetime.now(timezone.utc)
    update_transaction_query = (
        models.transactions.update()
        .where(models.transactions.c.id == transaction_id)
        .values(**transaction.model_dump())
    )
    await database.execute(update_transaction_query)
    return {**transaction.model_dump(), "id": transaction_id, "date": now}


@router.delete("/transactions/{transaction_id}", status_code=204)
async def delete_transaction(transaction_id: UUID):
    # Get the transaction
    select_query = models.transactions.select().where(
        models.transactions.c.id == transaction_id
    )
    transaction = await database.fetch_one(select_query)
    if transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")

    # Get the account
    select_account_query = models.accounts.select().where(
        models.accounts.c.id == transaction["account_id"]
    )
    account = await database.fetch_one(select_account_query)
    if account is None:
        raise HTTPException(status_code=404, detail="Account not found")

    # Update the account balance
    new_balance = account["balance"] - transaction["amount"]
    update_query = (
        models.accounts.update()
        .where(models.accounts.c.id == transaction["account_id"])
        .values(balance=new_balance)
    )
    await database.execute(update_query)

    # Delete the transaction
    delete_query = models.transactions.delete().where(
        models.transactions.c.id == transaction_id
    )
    await database.execute(delete_query)
    return None
