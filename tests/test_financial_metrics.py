
import pandas as pd
from src.financial_metrics import calculate_profit_margin


def test_calculate_profit_margin():
    companies = pd.DataFrame({
        "Company": ["Alpha Bank", "Beta Foods"],
        "Revenue": [1000, 2000],
        "Net_Profit": [150, 300]
    })

    results = calculate_profit_margin(companies)

    assert results.loc[0, "Net_Profit_Margin"] == 15.0
    assert results.loc[1, "Net_Profit_Margin"] == 15.0


def test_zero_revenue():
    companies = pd.DataFrame({
        "Company": ["Zero Revenue Co"],
        "Revenue": [0],
        "Net_Profit": [50]
    })

    results = calculate_profit_margin(companies)

    assert pd.isna(results.loc[0, "Net_Profit_Margin"])


def test_missing_profit():
    companies = pd.DataFrame({
        "Company": ["Unknown Profit Co"],
        "Revenue": [1000],
        "Net_Profit": [None]
    })

    results = calculate_profit_margin(companies)

    assert pd.isna(results.loc[0, "Net_Profit_Margin"])


def test_original_data_is_unchanged():
    companies = pd.DataFrame({
        "Company": ["Alpha Bank"],
        "Revenue": [1000],
        "Net_Profit": [150]
    })

    original_columns = list(companies.columns)
    calculate_profit_margin(companies)

    assert list(companies.columns) == original_columns


if __name__ == "__main__":
    test_calculate_profit_margin()
    test_zero_revenue()
    test_missing_profit()
    test_original_data_is_unchanged()

    print("All financial metric tests passed!")
