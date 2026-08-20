"""
Data cleaning module for the BrightCart pipeline.
"""

from pathlib import Path
import pandas as pd


INPUT_PATH = Path("data/processed/ingested_data.csv")
OUTPUT_PATH = Path("data/processed/cleaned_data.csv")


def clean_data():
    """
    Clean the ingested Online Retail II transaction data.
    """

    if not INPUT_PATH.exists():
        raise FileNotFoundError(
            f"Input file not found: {INPUT_PATH}"
        )

    df = pd.read_csv(INPUT_PATH)

    initial_records = len(df)

    # ---------------------------------------------------------
    # Standardize column names
    # ---------------------------------------------------------

    df.columns = (
        df.columns
        .str.strip()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )

    # ---------------------------------------------------------
    # Remove duplicate records
    # ---------------------------------------------------------

    df = df.drop_duplicates()

    # ---------------------------------------------------------
    # Remove records without CustomerID
    # ---------------------------------------------------------

    if "CustomerID" in df.columns:
        df = df.dropna(subset=["CustomerID"])

    # ---------------------------------------------------------
    # Convert numeric columns
    # ---------------------------------------------------------

    if "Quantity" in df.columns:
        df["Quantity"] = pd.to_numeric(
            df["Quantity"],
            errors="coerce"
        )

    if "Price" in df.columns:
        df["Price"] = pd.to_numeric(
            df["Price"],
            errors="coerce"
        )

    # ---------------------------------------------------------
    # Remove invalid quantities and prices
    # ---------------------------------------------------------

    if "Quantity" in df.columns:
        df = df[df["Quantity"] > 0]

    if "Price" in df.columns:
        df = df[df["Price"] > 0]

    # ---------------------------------------------------------
    # Convert invoice date
    # ---------------------------------------------------------

    if "InvoiceDate" in df.columns:
        df["InvoiceDate"] = pd.to_datetime(
            df["InvoiceDate"],
            errors="coerce"
        )

        df = df.dropna(
            subset=["InvoiceDate"]
        )

    # ---------------------------------------------------------
    # Create transaction value
    # ---------------------------------------------------------

    if "Quantity" in df.columns and "Price" in df.columns:
        df["TransactionValue"] = (
            df["Quantity"] * df["Price"]
        )

    # ---------------------------------------------------------
    # Save cleaned data
    # ---------------------------------------------------------

    OUTPUT_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_csv(
        OUTPUT_PATH,
        index=False
    )

    records_removed = initial_records - len(df)

    print(
        f"Cleaning completed.\n"
        f"Initial records: {initial_records:,}\n"
        f"Final records: {len(df):,}\n"
        f"Records removed: {records_removed:,}"
    )

    return df


if __name__ == "__main__":
    clean_data()
