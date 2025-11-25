import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .modules.finance import router as finance_router
from .modules.assets import router as assets_router
from .routers import debug, modules
from .database import database, engine
from .models import metadata, modules as modules_model


@asynccontextmanager
async def lifespan(app: FastAPI):
    if not os.getenv("TESTING"):
        async with engine.begin() as conn:
            await conn.run_sync(metadata.create_all)
    await database.connect()

    # Seed modules
    for module_name in ["finance", "assets"]:
        query = modules_model.select().where(modules_model.c.name == module_name)
        module = await database.fetch_one(query)
        if not module:
            insert_query = modules_model.insert().values(name=module_name, is_enabled=True)
            await database.execute(insert_query)

    yield
    await database.disconnect()

app = FastAPI(
    title="PRP-core API",
    description="API for The Personal Enterprise Project",
    version="0.1.0",
    openapi_url="/api/v1/openapi.json",
    docs_url="/api/v1/docs",
    redoc_url="/api/v1/redoc",
    lifespan=lifespan
)

@app.get("/health")
async def health_check():
    return {"status": "ok"}

# CORS
origins = [
    "http://localhost:5173",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(finance_router.router, prefix="/api/v1")
app.include_router(assets_router.router, prefix="/api/v1")
app.include_router(modules.router, prefix="/api/v1", tags=["modules"])
app.include_router(debug.router, prefix="/api/v1", tags=["debug"])
