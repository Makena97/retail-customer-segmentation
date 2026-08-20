"""
Data validation module for BrightCart.

Performs automated quality checks on the customer-level
RFM analytical dataset.
"""

from pathlib import Path
import pandas as pd


INPUT_PATH = Path(
    "data/validated/brightcart_customer_rfm.csv"
)


def validate_data():
    """
    Validate the final customer-level RFM dataset.
    """

    if not INPUT_PATH.exists():
        raise FileNotFoundError(
            f"Validation input not found: {INPUT_PATH}"
        )

    df = pd.read_csv(INPUT_PATH)

    # ---------------------------------------------------------
    # Required columns
    # ---------------------------------------------------------

    required_columns = [
        "CustomerID",
        "Recency",
        "Frequency",
        "Monetary",
        "AverageOrderValue"
    ]

    missing_columns = [
        column
        for column in required_columns
        if column not in df.columns
    ]

    assert not missing_columns, (
        f"Missing columns: {missing_columns}"
    )

    # ---------------------------------------------------------
    # CustomerID checks
    # ---------------------------------------------------------

    assert df["CustomerID"].notna().all(), (
        "CustomerID contains missing values."
    )

    assert df["CustomerID"].is_unique, (
        "CustomerID must be unique at customer level."
    )

    # ---------------------------------------------------------
    # RFM checks
    # ---------------------------------------------------------

    assert (df["Recency"] >= 0).all(), (
        "Recency contains negative values."
    )

    assert (df["Frequency"] > 0).all(), (
        "Frequency contains invalid values."
    )

    assert (df["Monetary"] >= 0).all(), (
        "Monetary contains negative values."
    )

    assert (
        df["AverageOrderValue"] >= 0
    ).all(), (
        "AverageOrderValue contains negative values."
    )

    # ---------------------------------------------------------
    # Missing-value check
    # ---------------------------------------------------------

    assert not df[required_columns].isnull().any().any(), (
        "Required fields contain missing values."
    )

    print(
        "Data validation PASSED successfully.\n"
        f"Validated customers: {len(df):,}"
    )

    return True


if __name__ == "__main__":
    validate_data()
