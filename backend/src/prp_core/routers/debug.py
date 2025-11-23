from fastapi import APIRouter, HTTPException
from prp_core.services import fake_data

router = APIRouter(
    prefix="/debug",
    tags=["debug"],
    responses={404: {"description": "Not found"}},
)

@router.post("/seed")
async def seed_data(scenario: str):
    """
    Seeds the database with fake data based on the chosen scenario.
    WARNING: This will wipe all existing data!
    """
    if scenario == "young_professional":
        await fake_data.seed_young_professional()
    elif scenario == "family":
        await fake_data.seed_family()
    elif scenario == "small_business":
        await fake_data.seed_small_business()
    else:
        raise HTTPException(status_code=400, detail="Invalid scenario")
    
    return {"message": f"Database seeded with {scenario} scenario"}
