
import pandas as pd
from src.financial_metrics import (
    calculate_profit_margin,
    calculate_roe,
    calculate_roa,
    calculate_debt_to_equity,
    calculate_current_ratio,
    calculate_quick_ratio,
    calculate_interest_coverage
)

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


def test_calculate_roe():
    companies = pd.DataFrame({
        "Company": ["Alpha Bank", "Beta Foods"],
        "Net_Profit": [150, 200],
        "Shareholders_Equity": [1000, 2000]
    })

    results = calculate_roe(companies)

    assert results.loc[0, "ROE"] == 15.0
    assert results.loc[1, "ROE"] == 10.0


def test_roe_with_zero_equity():
    companies = pd.DataFrame({
        "Company": ["Zero Equity Co"],
        "Net_Profit": [100],
        "Shareholders_Equity": [0]
    })

    results = calculate_roe(companies)

    assert pd.isna(results.loc[0, "ROE"])


def test_roe_with_missing_profit():
    companies = pd.DataFrame({
        "Company": ["Unknown Profit Co"],
        "Net_Profit": [None],
        "Shareholders_Equity": [1000]
    })

    results = calculate_roe(companies)

    assert pd.isna(results.loc[0, "ROE"])


def test_calculate_roa():
    companies = pd.DataFrame({
        "Company": ["Alpha Bank", "Beta Foods"],
        "Net_Profit": [200, 300],
        "Average_Total_Assets": [2000, 3000]
    })

    results = calculate_roa(companies)

    assert results.loc[0, "ROA"] == 10.0
    assert results.loc[1, "ROA"] == 10.0


def test_roa_with_zero_assets():
    companies = pd.DataFrame({
        "Company": ["Zero Assets Co"],
        "Net_Profit": [100],
        "Average_Total_Assets": [0]
    })

    results = calculate_roa(companies)

    assert pd.isna(results.loc[0, "ROA"])


def test_roa_with_missing_profit():
    companies = pd.DataFrame({
        "Company": ["Unknown Profit Co"],
        "Net_Profit": [None],
        "Average_Total_Assets": [1000]
    })

    results = calculate_roa(companies)

    assert pd.isna(results.loc[0, "ROA"])


def test_calculate_debt_to_equity():
    companies = pd.DataFrame({
        "Company": ["Alpha Bank", "Beta Foods"],
        "Total_Debt": [500, 300],
        "Shareholders_Equity": [1000, 2000]
    })

    results = calculate_debt_to_equity(companies)

    assert results.loc[0, "Debt_to_Equity"] == 0.5
    assert results.loc[1, "Debt_to_Equity"] == 0.15


def test_debt_to_equity_with_zero_equity():
    companies = pd.DataFrame({
        "Company": ["Zero Equity Co"],
        "Total_Debt": [500],
        "Shareholders_Equity": [0]
    })

    results = calculate_debt_to_equity(companies)

    assert pd.isna(results.loc[0, "Debt_to_Equity"])


def test_debt_to_equity_with_negative_equity():
    companies = pd.DataFrame({
        "Company": ["Negative Equity Co"],
        "Total_Debt": [500],
        "Shareholders_Equity": [-100]
    })

    results = calculate_debt_to_equity(companies)

    assert pd.isna(results.loc[0, "Debt_to_Equity"])


def test_calculate_current_ratio():
    companies = pd.DataFrame({
        "Company": ["Alpha Bank", "Beta Foods"],
        "Current_Assets": [900, 600],
        "Current_Liabilities": [450, 300]
    })

    results = calculate_current_ratio(companies)

    assert results.loc[0, "Current_Ratio"] == 2.0
    assert results.loc[1, "Current_Ratio"] == 2.0


def test_current_ratio_with_zero_liabilities():
    companies = pd.DataFrame({
        "Company": ["Zero Liability Co"],
        "Current_Assets": [500],
        "Current_Liabilities": [0]
    })

    results = calculate_current_ratio(companies)

    assert pd.isna(results.loc[0, "Current_Ratio"])


def test_current_ratio_with_missing_assets():
    companies = pd.DataFrame({
        "Company": ["Unknown Assets Co"],
        "Current_Assets": [None],
        "Current_Liabilities": [500]
    })

    results = calculate_current_ratio(companies)

    assert pd.isna(results.loc[0, "Current_Ratio"])


def test_calculate_quick_ratio():
    companies = pd.DataFrame({
        "Company": ["Alpha Foods", "Beta Foods"],
        "Current_Assets": [2000, 900],
        "Inventory": [700, 300],
        "Prepaid_Expenses": [100, 0],
        "Current_Liabilities": [600, 300]
    })

    results = calculate_quick_ratio(companies)

    assert results.loc[0, "Quick_Ratio"] == 2.0
    assert results.loc[1, "Quick_Ratio"] == 2.0


def test_quick_ratio_with_zero_liabilities():
    companies = pd.DataFrame({
        "Company": ["Zero Liability Co"],
        "Current_Assets": [1000],
        "Inventory": [200],
        "Prepaid_Expenses": [100],
        "Current_Liabilities": [0]
    })

    results = calculate_quick_ratio(companies)

    assert pd.isna(results.loc[0, "Quick_Ratio"])


def test_quick_ratio_with_missing_inventory():
    companies = pd.DataFrame({
        "Company": ["Unknown Inventory Co"],
        "Current_Assets": [1000],
        "Inventory": [None],
        "Prepaid_Expenses": [100],
        "Current_Liabilities": [500]
    })

    results = calculate_quick_ratio(companies)

    assert pd.isna(results.loc[0, "Quick_Ratio"])


def test_calculate_interest_coverage():
    companies = pd.DataFrame({
        "Company": ["Alpha Foods", "Beta Foods"],
        "Operating_Income": [500, 600],
        "Interest_Expense": [100, 200]
    })

    results = calculate_interest_coverage(companies)

    assert results.loc[0, "Interest_Coverage"] == 5.0
    assert results.loc[1, "Interest_Coverage"] == 3.0


def test_interest_coverage_with_zero_interest():
    companies = pd.DataFrame({
        "Company": ["Zero Interest Co"],
        "Operating_Income": [500],
        "Interest_Expense": [0]
    })

    results = calculate_interest_coverage(companies)

    assert pd.isna(results.loc[0, "Interest_Coverage"])


def test_interest_coverage_with_missing_income():
    companies = pd.DataFrame({
        "Company": ["Unknown Income Co"],
        "Operating_Income": [None],
        "Interest_Expense": [100]
    })

    results = calculate_interest_coverage(companies)

    assert pd.isna(results.loc[0, "Interest_Coverage"])


def test_interest_coverage_with_operating_loss():
    companies = pd.DataFrame({
        "Company": ["Loss Making Co"],
        "Operating_Income": [-200],
        "Interest_Expense": [100]
    })

    results = calculate_interest_coverage(companies)

    assert results.loc[0, "Interest_Coverage"] == -2.0
