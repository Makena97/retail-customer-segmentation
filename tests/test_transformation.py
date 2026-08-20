"""
Unit tests for BrightCart RFM feature engineering.
"""

import pandas as pd


def create_test_rfm(df):
    """
    Create RFM features for testing.
    """

    df = df.copy()

    df["InvoiceDate"] = pd.to_datetime(
        df["InvoiceDate"]
    )

    analysis_date = (
        df["InvoiceDate"].max()
        + pd.Timedelta(days=1)
    )

    rfm = (
        df.groupby("CustomerID")
        .agg(
            LastPurchaseDate=("InvoiceDate", "max"),
            Frequency=("InvoiceDate", "count"),
            Monetary=("TransactionValue", "sum")
        )
        .reset_index()
    )

    rfm["Recency"] = (
        analysis_date - rfm["LastPurchaseDate"]
    ).dt.days

    rfm["AverageOrderValue"] = (
        rfm["Monetary"] / rfm["Frequency"]
    )

    return rfm


def test_rfm_features_are_created():
    """Test that Recency, Frequency and Monetary are generated."""

    data = pd.DataFrame({
        "CustomerID": [
            "CUST_00001",
            "CUST_00001",
            "CUST_00002"
        ],
        "InvoiceDate": [
            "2026-01-01",
            "2026-01-10",
            "2026-01-05"
        ],
        "TransactionValue": [
            100.0,
            200.0,
            50.0
        ]
    })

    rfm = create_test_rfm(data)

    assert "Recency" in rfm.columns
    assert "Frequency" in rfm.columns
    assert "Monetary" in rfm.columns


def test_frequency_is_calculated_correctly():
    """Test the number of transactions per customer."""

    data = pd.DataFrame({
        "CustomerID": [
            "CUST_00001",
            "CUST_00001",
            "CUST_00001",
            "CUST_00002"
        ],
        "InvoiceDate": [
            "2026-01-01",
            "2026-01-02",
            "2026-01-03",
            "2026-01-05"
        ],
        "TransactionValue": [
            100.0,
            200.0,
            300.0,
            50.0
        ]
    })

    rfm = create_test_rfm(data)

    customer_1 = rfm[
        rfm["CustomerID"] == "CUST_00001"
    ].iloc[0]

    assert customer_1["Frequency"] == 3


def test_monetary_value_is_calculated_correctly():
    """Test total spending per customer."""

    data = pd.DataFrame({
        "CustomerID": [
            "CUST_00001",
            "CUST_00001",
            "CUST_00002"
        ],
        "InvoiceDate": [
            "2026-01-01",
            "2026-01-02",
            "2026-01-05"
        ],
        "TransactionValue": [
            100.0,
            200.0,
            50.0
        ]
    })

    rfm = create_test_rfm(data)

    customer_1 = rfm[
        rfm["CustomerID"] == "CUST_00001"
    ].iloc[0]

    assert customer_1["Monetary"] == 300.0


def test_recency_is_non_negative():
    """Test that Recency cannot be negative."""

    data = pd.DataFrame({
        "CustomerID": [
            "CUST_00001",
            "CUST_00002"
        ],
        "InvoiceDate": [
            "2026-01-01",
            "2026-01-05"
        ],
        "TransactionValue": [
            100.0,
            50.0
        ]
    })

    rfm = create_test_rfm(data)

    assert (rfm["Recency"] >= 0).all()


def test_average_order_value_is_correct():
    """Test average order value calculation."""

    data = pd.DataFrame({
        "CustomerID": [
            "CUST_00001",
            "CUST_00001"
        ],
        "InvoiceDate": [
            "2026-01-01",
            "2026-01-02"
        ],
        "TransactionValue": [
            100.0,
            300.0
        ]
    })

    rfm = create_test_rfm(data)

    customer = rfm.iloc[0]

    assert customer["AverageOrderValue"] == 200.0
