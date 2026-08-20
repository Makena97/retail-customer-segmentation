"""
Data ingestion module for the BrightCart pipeline.

Loads the raw Online Retail II dataset and saves a standardized
CSV copy for downstream processing.
"""

from pathlib import Path
import pandas as pd


RAW_DATA_PATH = Path("data/raw/online_retail_II.xlsx")
PROCESSED_DATA_PATH = Path("data/processed/ingested_data.csv")


def ingest_data():
    """
    Load the raw Online Retail II dataset.

    The function supports Excel and CSV files and stores the
    ingested dataset as CSV for downstream pipeline stages.
    """

    if not RAW_DATA_PATH.exists():
        raise FileNotFoundError(
            f"Raw dataset not found: {RAW_DATA_PATH}"
        )

    if RAW_DATA_PATH.suffix.lower() in [".xlsx", ".xls"]:
        df = pd.read_excel(RAW_DATA_PATH)

    elif RAW_DATA_PATH.suffix.lower() == ".csv":
        df = pd.read_csv(RAW_DATA_PATH)

    else:
        raise ValueError(
            "Unsupported file format. Use CSV or Excel."
        )

    PROCESSED_DATA_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_csv(
        PROCESSED_DATA_PATH,
        index=False
    )

    print(
        f"Ingestion completed successfully. "
        f"Records loaded: {len(df):,}"
    )

    return df


if __name__ == "__main__":
    ingest_data()
