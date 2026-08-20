"""
Customer anonymization module for the BrightCart pipeline.

Original customer identifiers are replaced with pseudonymous
customer IDs before analytical processing.
"""

from pathlib import Path
import pandas as pd


INPUT_PATH = Path("data/processed/cleaned_data.csv")
OUTPUT_PATH = Path("data/processed/anonymized_data.csv")


def anonymize_data():
    """
    Replace CustomerID with a pseudonymous identifier.

    Example:
        17850 -> CUST_00001
        17851 -> CUST_00002
    """

    if not INPUT_PATH.exists():
        raise FileNotFoundError(
            f"Input file not found: {INPUT_PATH}"
        )

    df = pd.read_csv(INPUT_PATH)

    if "CustomerID" not in df.columns:
        raise ValueError(
            "CustomerID column is required for anonymization."
        )

    # Ensure consistent ordering
    customer_ids = sorted(
        df["CustomerID"].dropna().unique()
    )

    customer_mapping = {
        customer_id: f"CUST_{index:05d}"
        for index, customer_id
        in enumerate(customer_ids, start=1)
    }

    df["CustomerID"] = df["CustomerID"].map(
        customer_mapping
    )

    OUTPUT_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_csv(
        OUTPUT_PATH,
        index=False
    )

    print(
        f"Anonymization completed. "
        f"Customers anonymized: {len(customer_mapping):,}"
    )

    return df


if __name__ == "__main__":
    anonymize_data()
