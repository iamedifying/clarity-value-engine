
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
