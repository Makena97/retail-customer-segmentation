import pandas as pd


# ---------------------------------------------------------
# Cleaning function used for testing
# ---------------------------------------------------------

def clean_data(combined_df):

    combined_df = combined_df.copy()

    # Standardize column names
    combined_df.columns = (
        combined_df.columns
        .str.strip()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )

    # Remove duplicates
    combined_df = combined_df.drop_duplicates()

    # Remove records without CustomerID
    if "CustomerID" in combined_df.columns:
        combined_df = combined_df.dropna(
            subset=["CustomerID"]
        )

    # Convert numeric columns
    if "Quantity" in combined_df.columns:
        combined_df["Quantity"] = pd.to_numeric(
            combined_df["Quantity"],
            errors="coerce"
        )

    if "Price" in combined_df.columns:
        combined_df["Price"] = pd.to_numeric(
            combined_df["Price"],
            errors="coerce"
        )

    # Remove invalid quantities and prices
    if "Quantity" in combined_df.columns:
        combined_df = combined_df[
            combined_df["Quantity"] > 0
        ]

    if "Price" in combined_df.columns:
        combined_df = combined_df[
            combined_df["Price"] > 0
        ]

    # Convert invoice date
    if "InvoiceDate" in combined_df.columns:
        combined_df["InvoiceDate"] = pd.to_datetime(
            combined_df["InvoiceDate"],
            errors="coerce"
        )

        combined_df = combined_df.dropna(
            subset=["InvoiceDate"]
        )

    # Create transaction value
    if (
        "Quantity" in combined_df.columns
        and "Price" in combined_df.columns
    ):
        combined_df["TransactionValue"] = (
            combined_df["Quantity"]
            * combined_df["Price"]
        )

    return combined_df


# ---------------------------------------------------------
# Create small test dataset
# ---------------------------------------------------------

def create_test_data():

    return pd.DataFrame({
        "Invoice": [
            "10001",
            "10002",
            "10003",
            "10003",
            "10004"
        ],
        "StockCode": [
            "A1",
            "B2",
            "C3",
            "C3",
            "D4"
        ],
        "Description": [
            "Product A",
            "Product B",
            "Product C",
            "Product C",
            "Product D"
        ],
        "Quantity": [
            2,
            -1,
            3,
            3,
            1
        ],
        "InvoiceDate": [
            "2010-01-01",
            "2010-01-02",
            "2010-01-03",
            "2010-01-03",
            "invalid_date"
        ],
        "Price": [
            10.00,
            15.00,
            20.00,
            20.00,
            5.00
        ],
        "CustomerID": [
            101,
            102,
            103,
            103,
            104
        ]
    })


# ---------------------------------------------------------
# Tests
# ---------------------------------------------------------

def test_clean_data_removes_invalid_quantity():

    df = create_test_data()

    cleaned = clean_data(df)

    assert (cleaned["Quantity"] > 0).all()


def test_clean_data_removes_duplicates():

    df = create_test_data()

    cleaned = clean_data(df)

    assert cleaned.duplicated().sum() == 0


def test_clean_data_removes_invalid_dates():

    df = create_test_data()

    cleaned = clean_data(df)

    assert cleaned["InvoiceDate"].notna().all()


def test_transaction_value_created_correctly():

    df = create_test_data()

    cleaned = clean_data(df)

    expected = (
        cleaned["Quantity"]
        * cleaned["Price"]
    )

    assert (
        cleaned["TransactionValue"]
        == expected
    ).all()


def test_cleaned_data_not_empty():

    df = create_test_data()

    cleaned = clean_data(df)

    assert len(cleaned) > 0
