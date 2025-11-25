from datetime import datetime
from enum import Enum
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict

# --- Enums ---
class BudgetPeriod(str, Enum):
    MONTHLY = "monthly"
    YEARLY = "yearly"

# --- Goals ---
class GoalBase(BaseModel):
    name: str
    target_amount: float
    current_amount: float = 0.0
    deadline: Optional[datetime] = None
    is_achieved: bool = False

class GoalCreate(GoalBase):
    pass

class GoalRead(GoalBase):
    id: UUID
    model_config = ConfigDict(from_attributes=True)

# --- Budgets ---
class BudgetBase(BaseModel):
    category: str
    limit_amount: float
    period: BudgetPeriod

class BudgetCreate(BudgetBase):
    pass

class BudgetRead(BudgetBase):
    id: UUID
    model_config = ConfigDict(from_attributes=True)

# --- Forecast Scenarios ---
class ForecastScenarioBase(BaseModel):
    name: str
    annual_growth_rate: float
    inflation_rate: float
    years_to_project: int

class ForecastScenarioCreate(ForecastScenarioBase):
    pass

class ForecastScenarioRead(ForecastScenarioBase):
    id: UUID
    model_config = ConfigDict(from_attributes=True)

class ForecastResultPoint(BaseModel):
    year: int
    projected_net_worth: float
    inflation_adjusted_net_worth: float

class ForecastResult(BaseModel):
    scenario_id: UUID
    data: List[ForecastResultPoint]

# --- Retirement Plans ---
class RetirementPlanBase(BaseModel):
    name: str
    current_age: int
    retirement_age: int
    life_expectancy: int
    desired_annual_income: float
    expected_return_rate: float
    current_savings: float
    annual_contribution: float

class RetirementPlanCreate(RetirementPlanBase):
    pass

class RetirementPlanRead(RetirementPlanBase):
    id: UUID
    model_config = ConfigDict(from_attributes=True)

class RetirementAnalysis(BaseModel):
    plan_id: UUID
    is_on_track: bool
    projected_savings_at_retirement: float
    required_savings_at_retirement: float
    shortfall_surplus: float
    sustainable_withdrawal_rate: float

# --- Loan Scenarios ---
class LoanScenarioBase(BaseModel):
    name: str
    principal: float
    interest_rate: float
    term_years: int
    down_payment: float = 0.0
    extra_monthly_payment: float = 0.0

class LoanScenarioCreate(LoanScenarioBase):
    pass

class LoanScenarioRead(LoanScenarioBase):
    id: UUID
    model_config = ConfigDict(from_attributes=True)

class LoanAnalysis(BaseModel):
    scenario_id: UUID
    monthly_payment: float
    total_interest_paid: float
    total_cost: float
    payoff_date: datetime
