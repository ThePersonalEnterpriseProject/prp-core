from typing import List
from uuid import UUID, uuid4

from fastapi import APIRouter, HTTPException, Depends

from ... import database
from . import models, schemas
from .services import calculations

router = APIRouter()

# --- Goals ---
@router.post("/planning/goals/", response_model=schemas.GoalRead, status_code=201)
async def create_goal(goal: schemas.GoalCreate):
    new_id = uuid4()
    query = models.goals.insert().values(id=new_id, **goal.model_dump())
    await database.database.execute(query)
    return {**goal.model_dump(), "id": new_id}

@router.get("/planning/goals/", response_model=List[schemas.GoalRead])
async def read_goals():
    query = models.goals.select()
    return await database.database.fetch_all(query)

@router.put("/planning/goals/{goal_id}", response_model=schemas.GoalRead)
async def update_goal(goal_id: UUID, goal: schemas.GoalCreate):
    query = models.goals.update().where(models.goals.c.id == goal_id).values(**goal.model_dump())
    await database.database.execute(query)
    return {**goal.model_dump(), "id": goal_id}

@router.delete("/planning/goals/{goal_id}", status_code=204)
async def delete_goal(goal_id: UUID):
    query = models.goals.delete().where(models.goals.c.id == goal_id)
    await database.database.execute(query)
    return None

# --- Budgets ---
@router.post("/planning/budgets/", response_model=schemas.BudgetRead, status_code=201)
async def create_budget(budget: schemas.BudgetCreate):
    new_id = uuid4()
    query = models.budgets.insert().values(id=new_id, **budget.model_dump())
    await database.database.execute(query)
    return {**budget.model_dump(), "id": new_id}

@router.get("/planning/budgets/", response_model=List[schemas.BudgetRead])
async def read_budgets():
    query = models.budgets.select()
    return await database.database.fetch_all(query)

@router.delete("/planning/budgets/{budget_id}", status_code=204)
async def delete_budget(budget_id: UUID):
    query = models.budgets.delete().where(models.budgets.c.id == budget_id)
    await database.database.execute(query)
    return None

# --- Forecast Scenarios ---
@router.post("/planning/forecasts/", response_model=schemas.ForecastScenarioRead, status_code=201)
async def create_forecast_scenario(scenario: schemas.ForecastScenarioCreate):
    new_id = uuid4()
    query = models.forecast_scenarios.insert().values(id=new_id, **scenario.model_dump())
    await database.database.execute(query)
    return {**scenario.model_dump(), "id": new_id}

@router.get("/planning/forecasts/", response_model=List[schemas.ForecastScenarioRead])
async def read_forecast_scenarios():
    query = models.forecast_scenarios.select()
    return await database.database.fetch_all(query)

@router.post("/planning/forecasts/{scenario_id}/run", response_model=schemas.ForecastResult)
async def run_forecast(scenario_id: UUID):
    query = models.forecast_scenarios.select().where(models.forecast_scenarios.c.id == scenario_id)
    scenario_data = await database.database.fetch_one(query)
    if not scenario_data:
        raise HTTPException(status_code=404, detail="Scenario not found")
    
    scenario = schemas.ForecastScenarioRead(**scenario_data)
    
    # TODO: Fetch actual current net worth from Finance module
    # For now, we'll use a placeholder or 0 if not integrated yet
    current_net_worth = 10000.0 # Placeholder
    
    return calculations.calculate_forecast(scenario, current_net_worth)

# --- Retirement Plans ---
@router.post("/planning/retirement/", response_model=schemas.RetirementPlanRead, status_code=201)
async def create_retirement_plan(plan: schemas.RetirementPlanCreate):
    new_id = uuid4()
    query = models.retirement_plans.insert().values(id=new_id, **plan.model_dump())
    await database.database.execute(query)
    return {**plan.model_dump(), "id": new_id}

@router.get("/planning/retirement/", response_model=List[schemas.RetirementPlanRead])
async def read_retirement_plans():
    query = models.retirement_plans.select()
    return await database.database.fetch_all(query)

@router.post("/planning/retirement/{plan_id}/analyze", response_model=schemas.RetirementAnalysis)
async def analyze_retirement_plan(plan_id: UUID):
    query = models.retirement_plans.select().where(models.retirement_plans.c.id == plan_id)
    plan_data = await database.database.fetch_one(query)
    if not plan_data:
        raise HTTPException(status_code=404, detail="Plan not found")
    
    plan = schemas.RetirementPlanRead(**plan_data)
    return calculations.calculate_retirement(plan)

# --- Loan Scenarios ---
@router.post("/planning/loans/", response_model=schemas.LoanScenarioRead, status_code=201)
async def create_loan_scenario(scenario: schemas.LoanScenarioCreate):
    new_id = uuid4()
    query = models.loan_scenarios.insert().values(id=new_id, **scenario.model_dump())
    await database.database.execute(query)
    return {**scenario.model_dump(), "id": new_id}

@router.get("/planning/loans/", response_model=List[schemas.LoanScenarioRead])
async def read_loan_scenarios():
    query = models.loan_scenarios.select()
    return await database.database.fetch_all(query)

@router.post("/planning/loans/compare", response_model=List[schemas.LoanAnalysis])
async def compare_loans(scenario_ids: List[UUID]):
    results = []
    for scenario_id in scenario_ids:
        query = models.loan_scenarios.select().where(models.loan_scenarios.c.id == scenario_id)
        scenario_data = await database.database.fetch_one(query)
        if scenario_data:
            scenario = schemas.LoanScenarioRead(**scenario_data)
            results.append(calculations.calculate_loan(scenario))
    return results
