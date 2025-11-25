import uuid
from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, Float, Integer, String, Table, Boolean, Enum
from sqlalchemy.dialects.postgresql import UUID

from ...models import metadata

# Goals
goals = Table(
    "planning_goals",
    metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    Column("name", String, nullable=False),
    Column("target_amount", Float, nullable=False),
    Column("current_amount", Float, default=0.0, nullable=False),
    Column("deadline", DateTime(timezone=True), nullable=True),
    Column("is_achieved", Boolean, default=False, nullable=False),
)

# Budgets
budgets = Table(
    "planning_budgets",
    metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    Column("category", String, nullable=False),
    Column("limit_amount", Float, nullable=False),
    Column("period", String, nullable=False), # 'monthly', 'yearly'
)

# Forecast Scenarios
forecast_scenarios = Table(
    "planning_forecast_scenarios",
    metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    Column("name", String, nullable=False),
    Column("annual_growth_rate", Float, nullable=False), # e.g., 0.07 for 7%
    Column("inflation_rate", Float, nullable=False), # e.g., 0.03 for 3%
    Column("years_to_project", Integer, nullable=False),
)

# Retirement Plans
retirement_plans = Table(
    "planning_retirement_plans",
    metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    Column("name", String, nullable=False),
    Column("current_age", Integer, nullable=False),
    Column("retirement_age", Integer, nullable=False),
    Column("life_expectancy", Integer, nullable=False),
    Column("desired_annual_income", Float, nullable=False),
    Column("expected_return_rate", Float, nullable=False),
    Column("current_savings", Float, default=0.0, nullable=False),
    Column("annual_contribution", Float, default=0.0, nullable=False),
)

# Loan Scenarios
loan_scenarios = Table(
    "planning_loan_scenarios",
    metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    Column("name", String, nullable=False),
    Column("principal", Float, nullable=False),
    Column("interest_rate", Float, nullable=False), # e.g., 0.05 for 5%
    Column("term_years", Integer, nullable=False),
    Column("down_payment", Float, default=0.0, nullable=False),
    Column("extra_monthly_payment", Float, default=0.0, nullable=False),
)
