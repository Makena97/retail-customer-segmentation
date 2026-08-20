"""
Feature engineering module for BrightCart.

Creates customer-level RFM features from transaction data.
"""

from pathlib import Path
import pandas as pd


INPUT_PATH = Path("data/processed/anonymized_data.csv")
OUTPUT_PATH = Path(
    "data/validated/brightcart_customer_rfm.csv"
)


def create_rfm_features():
    """
    Create Recency, Frequency and Monetary features
    at customer level.
    """

    if not INPUT_PATH.exists():
        raise FileNotFoundError(
            f"Input file not found: {INPUT_PATH}"
        )

    df = pd.read_csv(INPUT_PATH)

    required_columns = [
        "CustomerID",
        "InvoiceDate",
        "TransactionValue"
    ]

    missing_columns = [
        column
        for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    df["InvoiceDate"] = pd.to_datetime(
        df["InvoiceDate"],
        errors="coerce"
    )

    df = df.dropna(
        subset=["InvoiceDate"]
    )

    # ---------------------------------------------------------
    # Define analysis/reference date
    # ---------------------------------------------------------

    analysis_date = (
        df["InvoiceDate"].max()
        + pd.Timedelta(days=1)
    )

    # ---------------------------------------------------------
    # RFM calculation
    # ---------------------------------------------------------

    rfm = (
        df.groupby("CustomerID")
        .agg(
            LastPurchaseDate=("InvoiceDate", "max"),
            Frequency=("InvoiceDate", "count"),
            Monetary=("TransactionValue", "sum")
        )
        .reset_index()
    )

    # ---------------------------------------------------------
    # Calculate Recency
    # ---------------------------------------------------------

    rfm["Recency"] = (
        analysis_date - rfm["LastPurchaseDate"]
    ).dt.days

    # ---------------------------------------------------------
    # Additional customer features
    # ---------------------------------------------------------

    rfm["AverageOrderValue"] = (
        rfm["Monetary"] / rfm["Frequency"]
    )

    # ---------------------------------------------------------
    # Reorder columns
    # ---------------------------------------------------------

    rfm = rfm[
        [
            "CustomerID",
            "Recency",
            "Frequency",
            "Monetary",
            "AverageOrderValue",
            "LastPurchaseDate"
        ]
    ]

    # ---------------------------------------------------------
    # Save final analytical dataset
    # ---------------------------------------------------------

    OUTPUT_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    rfm.to_csv(
        OUTPUT_PATH,
        index=False
    )

    print(
        f"RFM transformation completed.\n"
        f"Customers generated: {len(rfm):,}"
    )

    return rfm


if __name__ == "__main__":
    create_rfm_features()
