from fastapi import HTTPException, status
from .database import database
from .models import modules

def require_module(module_name: str):
    async def dependency():
        query = modules.select().where(modules.c.name == module_name)
        module = await database.fetch_one(query)
        if not module or not module["is_enabled"]:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Module '{module_name}' is disabled"
            )
        return True
    return dependency
