"""
Bias and representation checks for the BrightCart pipeline.

The purpose is to identify potential representation imbalance
before customer segmentation is performed.
"""

from pathlib import Path
import pandas as pd


TRANSACTION_DATA = Path(
    "data/processed/anonymized_data.csv"
)

OUTPUT_REPORT = Path(
    "data/validated/bias_report.csv"
)


def run_bias_checks():
    """
    Check representation across customer countries.
    """

    if not TRANSACTION_DATA.exists():
        raise FileNotFoundError(
            f"Input file not found: {TRANSACTION_DATA}"
        )

    df = pd.read_csv(TRANSACTION_DATA)

    if "Country" not in df.columns:
        print(
            "Country column not available. "
            "Country representation check skipped."
        )
        return True

    # Count unique customers by country
    customer_counts = (
        df.groupby("Country")["CustomerID"]
        .nunique()
        .reset_index(
            name="UniqueCustomers"
        )
    )

    total_customers = (
        customer_counts["UniqueCustomers"].sum()
    )

    customer_counts["RepresentationPercentage"] = (
        customer_counts["UniqueCustomers"]
        / total_customers
        * 100
    )

    customer_counts = customer_counts.sort_values(
        "UniqueCustomers",
        ascending=False
    )

    OUTPUT_REPORT.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    customer_counts.to_csv(
        OUTPUT_REPORT,
        index=False
    )

    print("Bias/representation assessment completed.")
    print(
        customer_counts.head(10).to_string(
            index=False
        )
    )

    return True


if __name__ == "__main__":
    run_bias_checks()
