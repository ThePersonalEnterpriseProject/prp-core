from fastapi import APIRouter, Depends

from ...dependencies import require_module
from .routers import accounts, transactions

router = APIRouter(dependencies=[Depends(require_module("finance"))])

router.include_router(accounts.router, tags=["accounts"])
router.include_router(transactions.router, tags=["transactions"])
