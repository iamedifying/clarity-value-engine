
import pandas as pd
from financial_metrics import calculate_profit_margin


companies = pd.DataFrame({
    "Company": ["Alpha Bank", "Beta Foods", "Gamma Cement"],
    "Industry": ["Banking", "Consumer Goods", "Cement"],
    "Revenue": [1000, 1500, 1200],
    "Net_Profit": [150, 180, 240]
})

results = calculate_profit_margin(companies)

print("CLARITY VALUE ENGINE")
print("=" * 40)
print(results.to_string(index=False))
