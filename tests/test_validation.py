"""
Unit tests for BrightCart data validation.
"""

import pandas as pd
import pytest


def validate_rfm_data(df):
    """
    Apply the core validation rules used by BrightCart.
    """

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

    if missing_columns:
        raise ValueError(
            f"Missing columns: {missing_columns}"
        )

    if df["CustomerID"].isna().any():
        raise ValueError(
            "CustomerID contains missing values."
        )

    if not df["CustomerID"].is_unique:
        raise ValueError(
            "CustomerID must be unique."
        )

    if (df["Recency"] < 0).any():
        raise ValueError(
            "Recency contains negative values."
        )

    if (df["Frequency"] <= 0).any():
        raise ValueError(
            "Frequency contains invalid values."
        )

    if (df["Monetary"] < 0).any():
        raise ValueError(
            "Monetary contains negative values."
        )

    if (df["AverageOrderValue"] < 0).any():
        raise ValueError(
            "AverageOrderValue contains negative values."
        )

    if df[required_columns].isnull().any().any():
        raise ValueError(
            "Required fields contain missing values."
        )

    return True


def test_valid_rfm_dataset_passes():
    """Test that a valid RFM dataset passes validation."""

    data = pd.DataFrame({
        "CustomerID": [
            "CUST_00001",
            "CUST_00002"
        ],
        "Recency": [
            10,
            20
        ],
        "Frequency": [
            5,
            3
        ],
        "Monetary": [
            500.0,
            250.0
        ],
        "AverageOrderValue": [
            100.0,
            83.33
        ]
    })

    assert validate_rfm_data(data) is True


def test_negative_recency_fails():
    """Test that negative Recency values fail validation."""

    data = pd.DataFrame({
        "CustomerID": ["CUST_00001"],
        "Recency": [-5],
        "Frequency": [5],
        "Monetary": [500.0],
        "AverageOrderValue": [100.0]
    })

    with pytest.raises(ValueError):
        validate_rfm_data(data)


def test_zero_frequency_fails():
    """Test that zero Frequency fails validation."""

    data = pd.DataFrame({
        "CustomerID": ["CUST_00001"],
        "Recency": [10],
        "Frequency": [0],
        "Monetary": [500.0],
        "AverageOrderValue": [100.0]
    })

    with pytest.raises(ValueError):
        validate_rfm_data(data)


def test_negative_monetary_value_fails():
    """Test that negative Monetary values fail validation."""

    data = pd.DataFrame({
        "CustomerID": ["CUST_00001"],
        "Recency": [10],
        "Frequency": [5],
        "Monetary": [-500.0],
        "AverageOrderValue": [100.0]
    })

    with pytest.raises(ValueError):
        validate_rfm_data(data)


def test_duplicate_customer_ids_fail():
    """Test that duplicate customer IDs fail customer-level validation."""

    data = pd.DataFrame({
        "CustomerID": [
            "CUST_00001",
            "CUST_00001"
        ],
        "Recency": [
            10,
            20
        ],
        "Frequency": [
            5,
            3
        ],
        "Monetary": [
            500.0,
            250.0
        ],
        "AverageOrderValue": [
            100.0,
            83.33
        ]
    })

    with pytest.raises(ValueError):
        validate_rfm_data(data)


def test_missing_customer_id_fails():
    """Test that missing CustomerID fails validation."""

    data = pd.DataFrame({
        "CustomerID": [None],
        "Recency": [10],
        "Frequency": [5],
        "Monetary": [500.0],
        "AverageOrderValue": [100.0]
    })

    with pytest.raises(ValueError):
        validate_rfm_data(data)
