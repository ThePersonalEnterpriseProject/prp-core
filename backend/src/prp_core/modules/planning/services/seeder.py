import uuid
from datetime import datetime, timedelta, timezone

from prp_core.database import database
from prp_core.modules.planning.models import goals, budgets, forecast_scenarios, retirement_plans, loan_scenarios

async def clear_data():
    """Wipes planning data from the database."""
    await database.execute("TRUNCATE TABLE planning_goals CASCADE")
    await database.execute("TRUNCATE TABLE planning_budgets CASCADE")
    await database.execute("TRUNCATE TABLE planning_forecast_scenarios CASCADE")
    await database.execute("TRUNCATE TABLE planning_retirement_plans CASCADE")
    await database.execute("TRUNCATE TABLE planning_loan_scenarios CASCADE")

async def seed(scenario: str):
    await clear_data()

    # --- Goals ---
    goals_data = []
    if scenario == "young_professional":
        goals_data = [
            {"id": uuid.uuid4(), "name": "Emergency Fund", "target_amount": 15000.0, "current_amount": 5000.0, "deadline": datetime.now(timezone.utc) + timedelta(days=365), "is_achieved": False},
            {"id": uuid.uuid4(), "name": "Europe Trip", "target_amount": 5000.0, "current_amount": 1200.0, "deadline": datetime.now(timezone.utc) + timedelta(days=180), "is_achieved": False},
        ]
    elif scenario == "family":
        goals_data = [
            {"id": uuid.uuid4(), "name": "Kids College Fund", "target_amount": 100000.0, "current_amount": 25000.0, "deadline": datetime.now(timezone.utc) + timedelta(days=365*10), "is_achieved": False},
            {"id": uuid.uuid4(), "name": "Kitchen Renovation", "target_amount": 30000.0, "current_amount": 15000.0, "deadline": datetime.now(timezone.utc) + timedelta(days=365*2), "is_achieved": False},
        ]
    elif scenario == "small_business":
        goals_data = [
            {"id": uuid.uuid4(), "name": "Business Expansion", "target_amount": 50000.0, "current_amount": 10000.0, "deadline": datetime.now(timezone.utc) + timedelta(days=365*3), "is_achieved": False},
            {"id": uuid.uuid4(), "name": "New Equipment", "target_amount": 15000.0, "current_amount": 15000.0, "deadline": datetime.now(timezone.utc), "is_achieved": True},
        ]

    for goal in goals_data:
        query = goals.insert().values(**goal)
        await database.execute(query)

    # --- Budgets ---
    budgets_data = []
    if scenario == "young_professional":
        budgets_data = [
            {"id": uuid.uuid4(), "category": "Groceries", "limit_amount": 400.0, "period": "monthly"},
            {"id": uuid.uuid4(), "category": "Dining Out", "limit_amount": 200.0, "period": "monthly"},
            {"id": uuid.uuid4(), "category": "Entertainment", "limit_amount": 150.0, "period": "monthly"},
        ]
    elif scenario == "family":
        budgets_data = [
            {"id": uuid.uuid4(), "category": "Groceries", "limit_amount": 1200.0, "period": "monthly"},
            {"id": uuid.uuid4(), "category": "Utilities", "limit_amount": 300.0, "period": "monthly"},
            {"id": uuid.uuid4(), "category": "Kids Activities", "limit_amount": 500.0, "period": "monthly"},
        ]
    elif scenario == "small_business":
        budgets_data = [
            {"id": uuid.uuid4(), "category": "Office Supplies", "limit_amount": 500.0, "period": "monthly"},
            {"id": uuid.uuid4(), "category": "Marketing", "limit_amount": 2000.0, "period": "monthly"},
            {"id": uuid.uuid4(), "category": "Software Subscriptions", "limit_amount": 300.0, "period": "monthly"},
        ]

    for budget in budgets_data:
        query = budgets.insert().values(**budget)
        await database.execute(query)

    # --- Forecast Scenarios ---
    # Common scenarios for all
    forecasts_data = [
        {"id": uuid.uuid4(), "name": "Conservative", "annual_growth_rate": 0.05, "inflation_rate": 0.03, "years_to_project": 20},
        {"id": uuid.uuid4(), "name": "Moderate", "annual_growth_rate": 0.07, "inflation_rate": 0.03, "years_to_project": 20},
        {"id": uuid.uuid4(), "name": "Aggressive", "annual_growth_rate": 0.10, "inflation_rate": 0.03, "years_to_project": 20},
    ]
    
    for forecast in forecasts_data:
        query = forecast_scenarios.insert().values(**forecast)
        await database.execute(query)

    # --- Retirement Plans ---
    retirement_data = []
    if scenario == "young_professional":
        retirement_data = [
            {"id": uuid.uuid4(), "name": "Early Retirement", "current_age": 25, "retirement_age": 55, "life_expectancy": 90, "desired_annual_income": 60000.0, "expected_return_rate": 0.07, "current_savings": 20000.0, "annual_contribution": 15000.0},
        ]
    elif scenario == "family":
        retirement_data = [
            {"id": uuid.uuid4(), "name": "Standard Retirement", "current_age": 40, "retirement_age": 65, "life_expectancy": 90, "desired_annual_income": 80000.0, "expected_return_rate": 0.06, "current_savings": 200000.0, "annual_contribution": 20000.0},
        ]
    elif scenario == "small_business":
        retirement_data = [
            {"id": uuid.uuid4(), "name": "Business Exit", "current_age": 45, "retirement_age": 60, "life_expectancy": 90, "desired_annual_income": 100000.0, "expected_return_rate": 0.08, "current_savings": 150000.0, "annual_contribution": 30000.0},
        ]

    for plan in retirement_data:
        query = retirement_plans.insert().values(**plan)
        await database.execute(query)

    # --- Loan Scenarios ---
    loan_data = []
    if scenario == "young_professional":
        loan_data = [
            {"id": uuid.uuid4(), "name": "Student Loan Refinance", "principal": 30000.0, "interest_rate": 0.05, "term_years": 10, "down_payment": 0.0, "extra_monthly_payment": 100.0},
        ]
    elif scenario == "family":
        loan_data = [
            {"id": uuid.uuid4(), "name": "30-Year Fixed Mortgage", "principal": 400000.0, "interest_rate": 0.065, "term_years": 30, "down_payment": 80000.0, "extra_monthly_payment": 0.0},
            {"id": uuid.uuid4(), "name": "15-Year Fixed Mortgage", "principal": 400000.0, "interest_rate": 0.055, "term_years": 15, "down_payment": 80000.0, "extra_monthly_payment": 0.0},
        ]
    elif scenario == "small_business":
        loan_data = [
            {"id": uuid.uuid4(), "name": "Commercial Real Estate", "principal": 500000.0, "interest_rate": 0.07, "term_years": 20, "down_payment": 100000.0, "extra_monthly_payment": 500.0},
        ]

    for loan in loan_data:
        query = loan_scenarios.insert().values(**loan)
        await database.execute(query)
