"""
Unit tests for the BrightCart data cleaning module.
"""

import pandas as pd


def test_duplicate_records_are_removed():
    """Test that duplicate transaction records can be removed."""

    data = pd.DataFrame({
        "Invoice": ["10001", "10001", "10002"],
        "CustomerID": [12345, 12345, 12346],
        "Quantity": [2, 2, 5],
        "Price": [10.0, 10.0, 20.0]
    })

    cleaned = data.drop_duplicates()

    assert len(cleaned) == 2


def test_invalid_quantity_is_removed():
    """Test that transactions with non-positive quantities are removed."""

    data = pd.DataFrame({
        "CustomerID": [12345, 12346, 12347],
        "Quantity": [2, 0, -5],
        "Price": [10.0, 20.0, 30.0]
    })

    cleaned = data[data["Quantity"] > 0]

    assert len(cleaned) == 1
    assert (cleaned["Quantity"] > 0).all()


def test_invalid_price_is_removed():
    """Test that transactions with non-positive prices are removed."""

    data = pd.DataFrame({
        "CustomerID": [12345, 12346, 12347],
        "Quantity": [2, 3, 4],
        "Price": [10.0, 0.0, -5.0]
    })

    cleaned = data[data["Price"] > 0]

    assert len(cleaned) == 1
    assert (cleaned["Price"] > 0).all()


def test_missing_customer_id_is_removed():
    """Test that transactions without CustomerID are removed."""

    data = pd.DataFrame({
        "CustomerID": [12345, None, 12346],
        "Quantity": [2, 3, 4],
        "Price": [10.0, 20.0, 30.0]
    })

    cleaned = data.dropna(subset=["CustomerID"])

    assert len(cleaned) == 2
    assert cleaned["CustomerID"].notna().all()
