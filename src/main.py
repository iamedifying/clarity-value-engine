
import pandas as pd

from financial_metrics import (
    calculate_profit_margin,
    calculate_roe,
    calculate_roa,
    calculate_debt_to_equity,
    calculate_current_ratio,
    calculate_quick_ratio,
    calculate_interest_coverage,
    calculate_operating_cash_flow_ratio
)

# Create our sample company dataset
companies = pd.DataFrame({
    "Company": ["Alpha Bank", "Beta Foods", "Gamma Cement"],
    "Industry": ["Banking", "Consumer Goods", "Cement"],
    "Revenue": [1000, 1500, 1200],
    "Net_Profit": [150, 180, 240],
    "Shareholders_Equity": [1000, 1200, 2000],
    "Average_Total_Assets": [2000, 3000, 4000],
    "Total_Debt": [500, 300, 1000],
    "Current_Assets": [2000, 900, 1200],
    "Inventory": [500, 200, 400],
    "Prepaid_Expenses": [100, 100, 200],
    "Current_Liabilities": [1000, 600, 800],
    "Operating_Income": [200, 300, 400],
    "Interest_Expense": [50, 30, 100],
    "Operating_Cash_Flow": [700, 200, 600],

})

# Calculate financial metrics
results = calculate_profit_margin(companies)
results = calculate_roe(results)
results = calculate_roa(results)
results = calculate_debt_to_equity(results)
results = calculate_current_ratio(results)
results = calculate_quick_ratio(results)
results = calculate_interest_coverage(results)
results = calculate_operating_cash_flow_ratio(results)

# Display results
print("CLARITY VALUE ENGINE")
print("=" * 40)
print(results.to_string(index=False))
