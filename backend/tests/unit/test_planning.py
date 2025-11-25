import pytest
from uuid import uuid4
from datetime import datetime, timezone
from prp_core.modules.planning import schemas
from prp_core.modules.planning.services import calculations

def test_calculate_forecast():
    scenario = schemas.ForecastScenarioRead(
        id=uuid4(),
        name="Test Scenario",
        annual_growth_rate=0.10, # 10%
        inflation_rate=0.03, # 3%
        years_to_project=5
    )
    current_net_worth = 1000.0
    
    result = calculations.calculate_forecast(scenario, current_net_worth)
    
    assert result.scenario_id == scenario.id
    assert len(result.data) == 5
    
    # Year 1: 1000 * 1.1 = 1100
    assert result.data[0].projected_net_worth == 1100.0
    # Inflation adjusted: 1100 / 1.03 = 1067.96
    assert result.data[0].inflation_adjusted_net_worth == 1067.96

def test_calculate_retirement():
    plan = schemas.RetirementPlanRead(
        id=uuid4(),
        name="Test Plan",
        current_age=30,
        retirement_age=60,
        life_expectancy=90,
        desired_annual_income=50000.0,
        expected_return_rate=0.05,
        current_savings=10000.0,
        annual_contribution=10000.0
    )
    
    result = calculations.calculate_retirement(plan)
    
    assert result.plan_id == plan.id
    # Just checking it runs and returns logical values
    assert result.projected_savings_at_retirement > 0
    assert result.required_savings_at_retirement == 50000.0 / 0.04 # 1,250,000

def test_calculate_loan():
    scenario = schemas.LoanScenarioRead(
        id=uuid4(),
        name="Test Loan",
        principal=100000.0,
        interest_rate=0.05,
        term_years=30,
        down_payment=20000.0,
        extra_monthly_payment=0.0
    )
    
    result = calculations.calculate_loan(scenario)
    
    assert result.scenario_id == scenario.id
    # Principal to finance = 80,000
    # Monthly payment approx 429.46
    assert 429.0 < result.monthly_payment < 430.0
    assert result.total_cost > 80000.0
