"""
Unit tests for BrightCart customer anonymization.
"""

import pandas as pd


def anonymize_customer_ids(df):
    """
    Create pseudonymous customer IDs for testing.
    """

    customer_ids = sorted(
        df["CustomerID"].dropna().unique()
    )

    mapping = {
        customer_id: f"CUST_{index:05d}"
        for index, customer_id
        in enumerate(customer_ids, start=1)
    }

    df = df.copy()

    df["CustomerID"] = df["CustomerID"].map(
        mapping
    )

    return df


def test_customer_ids_are_anonymized():
    """Test that original IDs are replaced."""

    data = pd.DataFrame({
        "CustomerID": [17850, 17851, 17852]
    })

    anonymized = anonymize_customer_ids(data)

    assert anonymized["CustomerID"].tolist() == [
        "CUST_00001",
        "CUST_00002",
        "CUST_00003"
    ]


def test_anonymized_ids_have_correct_format():
    """Test that anonymized IDs follow the expected format."""

    data = pd.DataFrame({
        "CustomerID": [17850, 17851]
    })

    anonymized = anonymize_customer_ids(data)

    for customer_id in anonymized["CustomerID"]:
        assert customer_id.startswith("CUST_")
        assert len(customer_id) == 10


def test_anonymized_ids_are_unique():
    """Test that each customer receives a unique identifier."""

    data = pd.DataFrame({
        "CustomerID": [17850, 17851, 17852, 17850]
    })

    anonymized = anonymize_customer_ids(data)

    assert (
        anonymized["CustomerID"].nunique()
        == data["CustomerID"].nunique()
    )
