from fastapi import APIRouter, HTTPException
from typing import List
from uuid import UUID, uuid4
from datetime import datetime, timezone
from .. import schemas
from .. import models
from ..database import database

router = APIRouter()

# Accounts
@router.post("/accounts/", response_model=schemas.AccountRead, status_code=201)
async def create_account(account: schemas.AccountCreate):
    new_id = uuid4()
    query = models.accounts.insert().values(id=new_id, **account.model_dump())
    await database.execute(query)
    return {**account.model_dump(), "id": new_id}

@router.get("/accounts/", response_model=List[schemas.AccountRead])
async def read_accounts(skip: int = 0, limit: int = 100):
    query = models.accounts.select().offset(skip).limit(limit)
    return await database.fetch_all(query)

@router.get("/accounts/{account_id}", response_model=schemas.AccountRead)
async def read_account(account_id: UUID):
    query = models.accounts.select().where(models.accounts.c.id == account_id)
    account = await database.fetch_one(query)
    if account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    return account

@router.put("/accounts/{account_id}", response_model=schemas.AccountRead)
async def update_account(account_id: UUID, account: schemas.AccountCreate):
    query = models.accounts.update().where(models.accounts.c.id == account_id).values(**account.model_dump())
    await database.execute(query)
    return {**account.model_dump(), "id": account_id}

@router.delete("/accounts/{account_id}", status_code=204)
async def delete_account(account_id: UUID):
    query = models.accounts.delete().where(models.accounts.c.id == account_id)
    await database.execute(query)
    return None

# Transactions
@router.post("/transactions/", response_model=schemas.TransactionRead, status_code=201)
async def create_transaction(transaction: schemas.TransactionCreate):
    # Get the account
    query = models.accounts.select().where(models.accounts.c.id == transaction.account_id)
    account = await database.fetch_one(query)
    if account is None:
        raise HTTPException(status_code=404, detail="Account not found")

    # Update the account balance
    new_balance = account.balance + transaction.amount
    query = models.accounts.update().where(models.accounts.c.id == transaction.account_id).values(balance=new_balance)
    await database.execute(query)

    # Create the transaction
    new_id = uuid4()
    now = datetime.now(timezone.utc)
    query = models.transactions.insert().values(id=new_id, date=now, **transaction.model_dump())
    await database.execute(query)
    return {**transaction.model_dump(), "id": new_id, "date": now}

@router.get("/transactions/", response_model=List[schemas.TransactionRead])
async def read_transactions(skip: int = 0, limit: int = 100):
    query = models.transactions.select().offset(skip).limit(limit)
    return await database.fetch_all(query)

@router.get("/transactions/{transaction_id}", response_model=schemas.TransactionRead)
async def read_transaction(transaction_id: UUID):
    query = models.transactions.select().where(models.transactions.c.id == transaction_id)
    transaction = await database.fetch_one(query)
    if transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction

@router.put("/transactions/{transaction_id}", response_model=schemas.TransactionRead)
async def update_transaction(transaction_id: UUID, transaction: schemas.TransactionCreate):
    # Get the old transaction
    query = models.transactions.select().where(models.transactions.c.id == transaction_id)
    old_transaction = await database.fetch_one(query)
    if old_transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")

    # Get the account
    query = models.accounts.select().where(models.accounts.c.id == old_transaction.account_id)
    account = await database.fetch_one(query)
    if account is None:
        raise HTTPException(status_code=404, detail="Account not found")

    # Update the account balance
    new_balance = account.balance - old_transaction.amount + transaction.amount
    query = models.accounts.update().where(models.accounts.c.id == old_transaction.account_id).values(balance=new_balance)
    await database.execute(query)

    # Update the transaction
    now = datetime.now(timezone.utc)
    query = models.transactions.update().where(models.transactions.c.id == transaction_id).values(**transaction.model_dump())
    await database.execute(query)
    return {**transaction.model_dump(), "id": transaction_id, "date": now}

@router.delete("/transactions/{transaction_id}", status_code=204)
async def delete_transaction(transaction_id: UUID):
    # Get the transaction
    query = models.transactions.select().where(models.transactions.c.id == transaction_id)
    transaction = await database.fetch_one(query)
    if transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")

    # Get the account
    query = models.accounts.select().where(models.accounts.c.id == transaction.account_id)
    account = await database.fetch_one(query)
    if account is None:
        raise HTTPException(status_code=404, detail="Account not found")

    # Update the account balance
    new_balance = account.balance - transaction.amount
    query = models.accounts.update().where(models.accounts.c.id == transaction.account_id).values(balance=new_balance)
    await database.execute(query)

    # Delete the transaction
    query = models.transactions.delete().where(models.transactions.c.id == transaction_id)
    await database.execute(query)
    return None
