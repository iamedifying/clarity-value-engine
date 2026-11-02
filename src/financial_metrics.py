
import pandas as pd


def calculate_profit_margin(companies):
    """Calculate net profit margin safely."""

    companies = companies.copy()

    companies["Revenue"] = pd.to_numeric(
        companies["Revenue"], errors="coerce"
    )

    companies["Net_Profit"] = pd.to_numeric(
        companies["Net_Profit"], errors="coerce"
    )

    valid_revenue = companies["Revenue"].where(
        companies["Revenue"] != 0
    )

    companies["Net_Profit_Margin"] = (
        companies["Net_Profit"] / valid_revenue
    ) * 100

    return companies


def calculate_roe(companies):
    """Calculate Return on Equity (ROE) safely."""

    companies = companies.copy()

    companies["Net_Profit"] = pd.to_numeric(
        companies["Net_Profit"], errors="coerce"
    )

    companies["Shareholders_Equity"] = pd.to_numeric(
        companies["Shareholders_Equity"], errors="coerce"
    )

    valid_equity = companies["Shareholders_Equity"].where(
        companies["Shareholders_Equity"] != 0
    )

    companies["ROE"] = (
        companies["Net_Profit"] / valid_equity
    ) * 100

    return companies


def calculate_roa(companies):
    """Calculate Return on Assets (ROA) safely."""

    companies = companies.copy()

    companies["Net_Profit"] = pd.to_numeric(
        companies["Net_Profit"], errors="coerce"
    )

    companies["Average_Total_Assets"] = pd.to_numeric(
        companies["Average_Total_Assets"], errors="coerce"
    )

    valid_assets = companies["Average_Total_Assets"].where(
        companies["Average_Total_Assets"] != 0
    )

    companies["ROA"] = (
        companies["Net_Profit"] / valid_assets
    ) * 100

    return companies


def calculate_debt_to_equity(companies):
    """Calculate Debt-to-Equity ratio safely."""

    companies = companies.copy()

    companies["Total_Debt"] = pd.to_numeric(
        companies["Total_Debt"], errors="coerce"
    )

    companies["Shareholders_Equity"] = pd.to_numeric(
        companies["Shareholders_Equity"], errors="coerce"
    )

    valid_equity = companies["Shareholders_Equity"].where(
        companies["Shareholders_Equity"] > 0
    )

    companies["Debt_to_Equity"] = (
        companies["Total_Debt"] / valid_equity
    )

    return companies


def calculate_current_ratio(companies):
    """Calculate Current Ratio safely."""

    companies = companies.copy()

    companies["Current_Assets"] = pd.to_numeric(
        companies["Current_Assets"], errors="coerce"
    )

    companies["Current_Liabilities"] = pd.to_numeric(
        companies["Current_Liabilities"], errors="coerce"
    )

    valid_liabilities = companies["Current_Liabilities"].where(
        companies["Current_Liabilities"] > 0
    )

    companies["Current_Ratio"] = (
        companies["Current_Assets"] / valid_liabilities
    )

    return companies

def calculate_quick_ratio(companies):
    """Calculate Quick Ratio safely."""

    companies = companies.copy()

    numeric_columns = [
        "Current_Assets",
        "Inventory",
        "Prepaid_Expenses",
        "Current_Liabilities"
    ]

    for column in numeric_columns:
        companies[column] = pd.to_numeric(
            companies[column], errors="coerce"
        )

    quick_assets = (
        companies["Current_Assets"]
        - companies["Inventory"]
        - companies["Prepaid_Expenses"]
    )

    valid_liabilities = companies["Current_Liabilities"].where(
        companies["Current_Liabilities"] > 0
    )

    companies["Quick_Ratio"] = quick_assets / valid_liabilities

    return companies

def calculate_interest_coverage(companies):
    """Calculate Interest Coverage Ratio safely."""

    companies = companies.copy()

    companies["Operating_Income"] = pd.to_numeric(
        companies["Operating_Income"], errors="coerce"
    )

    companies["Interest_Expense"] = pd.to_numeric(
        companies["Interest_Expense"], errors="coerce"
    )

    valid_interest = companies["Interest_Expense"].where(
        companies["Interest_Expense"] > 0
    )

    companies["Interest_Coverage"] = (
        companies["Operating_Income"] / valid_interest
    )

    return companies

def calculate_operating_cash_flow_ratio(companies):
    """Calculate Operating Cash Flow Ratio safely."""

    companies = companies.copy()

    companies["Operating_Cash_Flow"] = pd.to_numeric(
        companies["Operating_Cash_Flow"], errors="coerce"
    )

    companies["Current_Liabilities"] = pd.to_numeric(
        companies["Current_Liabilities"], errors="coerce"
    )

    valid_liabilities = companies["Current_Liabilities"].where(
        companies["Current_Liabilities"] > 0
    )

    companies["Operating_Cash_Flow_Ratio"] = (
        companies["Operating_Cash_Flow"] / valid_liabilities
    )

    return companies

def calculate_free_cash_flow(companies):
    """Calculate Free Cash Flow safely."""

    companies = companies.copy()

    companies["Operating_Cash_Flow"] = pd.to_numeric(
        companies["Operating_Cash_Flow"], errors="coerce"
    )

    companies["Capital_Expenditure"] = pd.to_numeric(
        companies["Capital_Expenditure"], errors="coerce"
    )

    companies["Free_Cash_Flow"] = (
        companies["Operating_Cash_Flow"]
        - companies["Capital_Expenditure"]
    )

    return companies

def calculate_revenue_growth(companies):
    """Calculate Revenue Growth Percentage safely."""

    companies = companies.copy()

    companies["Revenue"] = pd.to_numeric(
        companies["Revenue"], errors="coerce"
    )

    companies["Previous_Revenue"] = pd.to_numeric(
        companies["Previous_Revenue"], errors="coerce"
    )

    valid_previous_revenue = companies["Previous_Revenue"].where(
        companies["Previous_Revenue"] > 0
    )

    valid_current_revenue = companies["Revenue"].where(
        companies["Revenue"] >= 0
    )

    companies["Revenue_Growth_Percent"] = (
        (valid_current_revenue - valid_previous_revenue)
        / valid_previous_revenue
    ) * 100

    return companies