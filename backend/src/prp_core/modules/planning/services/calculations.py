from datetime import datetime, timedelta, timezone
from typing import List
import math

from .. import schemas

def calculate_forecast(scenario: schemas.ForecastScenarioRead, current_net_worth: float) -> schemas.ForecastResult:
    data = []
    net_worth = current_net_worth
    
    # Simple compound interest formula: A = P(1 + r)^t
    # We apply it year by year to generate the data points
    
    for year in range(1, scenario.years_to_project + 1):
        # Apply growth
        net_worth = net_worth * (1 + scenario.annual_growth_rate)
        
        # Calculate inflation adjusted value: Real Value = Nominal Value / (1 + i)^t
        inflation_adjusted = net_worth / ((1 + scenario.inflation_rate) ** year)
        
        data.append(schemas.ForecastResultPoint(
            year=year,
            projected_net_worth=round(net_worth, 2),
            inflation_adjusted_net_worth=round(inflation_adjusted, 2)
        ))
        
    return schemas.ForecastResult(scenario_id=scenario.id, data=data)

def calculate_retirement(plan: schemas.RetirementPlanRead) -> schemas.RetirementAnalysis:
    years_to_retirement = plan.retirement_age - plan.current_age
    years_in_retirement = plan.life_expectancy - plan.retirement_age
    
    if years_to_retirement <= 0:
        # Already retired logic (simplified)
        projected_savings = plan.current_savings
    else:
        # Future Value of a Series (Annual Contributions) + Future Value of Lump Sum (Current Savings)
        # FV = P * (1 + r)^t + PMT * (((1 + r)^t - 1) / r)
        r = plan.expected_return_rate
        t = years_to_retirement
        pmt = plan.annual_contribution
        p = plan.current_savings
        
        if r == 0:
             projected_savings = p + (pmt * t)
        else:
            fv_lump_sum = p * ((1 + r) ** t)
            fv_contributions = pmt * (((1 + r) ** t - 1) / r)
            projected_savings = fv_lump_sum + fv_contributions

    # Required Nest Egg using the 4% rule (or inverse of withdrawal rate)
    # Ideally, we'd use a more complex calculation, but for now:
    # Required = Annual Income / Safe Withdrawal Rate (assumed 4%)
    safe_withdrawal_rate = 0.04
    required_savings = plan.desired_annual_income / safe_withdrawal_rate
    
    shortfall_surplus = projected_savings - required_savings
    is_on_track = shortfall_surplus >= 0
    
    # Calculate sustainable withdrawal rate based on projected savings
    if projected_savings > 0:
        sustainable_withdrawal_rate = plan.desired_annual_income / projected_savings
    else:
        sustainable_withdrawal_rate = 0.0

    return schemas.RetirementAnalysis(
        plan_id=plan.id,
        is_on_track=is_on_track,
        projected_savings_at_retirement=round(projected_savings, 2),
        required_savings_at_retirement=round(required_savings, 2),
        shortfall_surplus=round(shortfall_surplus, 2),
        sustainable_withdrawal_rate=round(sustainable_withdrawal_rate, 4)
    )

def calculate_loan(scenario: schemas.LoanScenarioRead) -> schemas.LoanAnalysis:
    # Monthly Payment Calculation: M = P [ i(1 + i)^n ] / [ (1 + i)^n - 1 ]
    # P = Principal - Down Payment
    # i = Monthly Interest Rate (Annual / 12)
    # n = Number of Payments (Years * 12)
    
    principal = scenario.principal - scenario.down_payment
    if principal <= 0:
        return schemas.LoanAnalysis(
            scenario_id=scenario.id,
            monthly_payment=0.0,
            total_interest_paid=0.0,
            total_cost=0.0,
            payoff_date=datetime.now(timezone.utc)
        )

    annual_rate = scenario.interest_rate
    monthly_rate = annual_rate / 12
    num_payments = scenario.term_years * 12
    
    if monthly_rate == 0:
        monthly_payment = principal / num_payments
    else:
        monthly_payment = principal * (monthly_rate * ((1 + monthly_rate) ** num_payments)) / (((1 + monthly_rate) ** num_payments) - 1)
    
    # Add extra payment
    actual_monthly_payment = monthly_payment + scenario.extra_monthly_payment
    
    # Calculate total interest and actual payoff time
    remaining_balance = principal
    total_interest = 0.0
    months_passed = 0
    
    while remaining_balance > 0:
        interest_for_month = remaining_balance * monthly_rate
        principal_for_month = actual_monthly_payment - interest_for_month
        
        if principal_for_month > remaining_balance:
            principal_for_month = remaining_balance
            actual_monthly_payment = interest_for_month + principal_for_month
            
        total_interest += interest_for_month
        remaining_balance -= principal_for_month
        months_passed += 1
        
        # Safety break for infinite loops
        if months_passed > 1000: 
            break
            
    payoff_date = datetime.now(timezone.utc) + timedelta(days=30 * months_passed)
    total_cost = principal + total_interest
    
    return schemas.LoanAnalysis(
        scenario_id=scenario.id,
        monthly_payment=round(monthly_payment, 2), # Base monthly payment
        total_interest_paid=round(total_interest, 2),
        total_cost=round(total_cost, 2),
        payoff_date=payoff_date
    )
