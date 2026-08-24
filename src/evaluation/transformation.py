# =========================================================
# MODULE 4: MODEL DATA PREPARATION
# Predicting 90-Day Repeat Purchase
# =========================================================

import pandas as pd
import numpy as np


# ---------------------------------------------------------
# 1. Import cleaned dataset
# ---------------------------------------------------------

df = pd.read_csv(
    "C:/Users/kbnmi5985/Downloads/cleaned_online_retail_II.csv",
    low_memory=False
)

print("Original dataset shape:", df.shape)
print(df.head())

# ---------------------------------------------------------
# 2. Prepare variables
# ---------------------------------------------------------

# Convert InvoiceDate from text to a Python datetime
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Customer-level prediction requires a Customer ID
df = df.dropna(subset=["Customer_ID"]).copy()

# Convert Customer_ID to a clean string
df["Customer_ID"] = (
    df["Customer_ID"]
    .astype(int)
    .astype(str)
)

print("Rows available for customer modeling:", len(df))
print("Unique customers:", df["Customer_ID"].nunique())

print(
    "Transaction period:",
    df["InvoiceDate"].min(),
    "to",
    df["InvoiceDate"].max()
)

# ---------------------------------------------------------
# 3. Define prediction cutoff and horizon
# ---------------------------------------------------------

prediction_date = pd.Timestamp("2011-09-09")

prediction_end = prediction_date + pd.Timedelta(days=90)

print("Prediction date:", prediction_date)
print("Prediction horizon ends:", prediction_end)

# ---------------------------------------------------------
# 4. Separate historical and future transactions
# ---------------------------------------------------------

historical_df = df[
    df["InvoiceDate"] < prediction_date
].copy()


future_df = df[
    (df["InvoiceDate"] >= prediction_date) &
    (df["InvoiceDate"] < prediction_end)
].copy()


print("Historical transactions:", len(historical_df))
print("Future transactions:", len(future_df))

# ---------------------------------------------------------
# 5. Create customer-level features
# ---------------------------------------------------------

customer_features = historical_df.groupby(
    "Customer_ID"
).agg(

    Last_Purchase=("InvoiceDate", "max"),

    First_Purchase=("InvoiceDate", "min"),

    Frequency=("Invoice", "nunique"),

    Monetary=("TransactionValue", "sum"),

    Total_Quantity=("Quantity", "sum"),

    Unique_Products=("StockCode", "nunique")

).reset_index()

# Recency = days since most recent purchase

customer_features["Recency_Days"] = (
    prediction_date -
    customer_features["Last_Purchase"]
).dt.days


# Tenure = days between first and most recent purchase

customer_features["Tenure_Days"] = (
    customer_features["Last_Purchase"] -
    customer_features["First_Purchase"]
).dt.days

# ---------------------------------------------------------
# 6. Calculate Average Order Value
# ---------------------------------------------------------

invoice_values = (
    historical_df
    .groupby(["Customer_ID", "Invoice"])["TransactionValue"]
    .sum()
    .reset_index()
)


average_order = (
    invoice_values
    .groupby("Customer_ID")["TransactionValue"]
    .mean()
    .reset_index()
)


average_order.columns = [
    "Customer_ID",
    "Avg_Order_Value"
]


customer_features = customer_features.merge(
    average_order,
    on="Customer_ID",
    how="left"
)

# ---------------------------------------------------------
# 7. Create target variable
# ---------------------------------------------------------

future_customers = set(
    future_df["Customer_ID"].unique()
)


customer_features["Repeat_Purchase_90d"] = (
    customer_features["Customer_ID"]
    .isin(future_customers)
    .astype(int)
)

# ---------------------------------------------------------
# 8. Select final modeling variables
# ---------------------------------------------------------

model_data = customer_features[
    [
        "Customer_ID",
        "Recency_Days",
        "Frequency",
        "Monetary",
        "Avg_Order_Value",
        "Total_Quantity",
        "Unique_Products",
        "Tenure_Days",
        "Repeat_Purchase_90d"
    ]
].copy()


print(model_data.head())

print(
    model_data["Repeat_Purchase_90d"]
    .value_counts()
)


print(
    model_data["Repeat_Purchase_90d"]
    .value_counts(normalize=True)
    .round(3)
)

# ---------------------------------------------------------
# 10. Export modeling dataset
# ---------------------------------------------------------

model_data.to_csv(
    "C:/Users/kbnmi5985/Downloads/customer_modeling_dataset.csv",
    index=False
)


print(
    "Modeling dataset successfully created."
)

print(
    "Final dataset shape:",
    model_data.shape
)
