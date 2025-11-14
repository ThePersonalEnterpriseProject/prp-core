from pydantic import BaseModel, ConfigDict
from uuid import UUID, uuid4
from datetime import datetime
from enum import Enum

class AccountType(str, Enum):
    ASSET = "Asset"
    LIABILITY = "Liability"

class AccountBase(BaseModel):
    name: str
    account_type: AccountType
    balance: float = 0.0

class AccountCreate(AccountBase):
    pass

class AccountRead(AccountBase):
    id: UUID
    model_config = ConfigDict(from_attributes=True)

class TransactionBase(BaseModel):
    description: str
    amount: float
    account_id: UUID

class TransactionCreate(TransactionBase):
    pass

class TransactionRead(TransactionBase):
    id: UUID
    date: datetime
    model_config = ConfigDict(from_attributes=True)
