# BrightCart Data Dictionary

## 1. Project Overview

BrightCart is an online retail analytics project focused on customer segmentation. The objective is to transform transactional retail data into a customer-level analytical dataset that can be used for RFM analysis and K-Means clustering.

The primary dataset used is the Online Retail II dataset from the UCI Machine Learning Repository.

## 2. Source Dataset

**Dataset:** Online Retail II

**Source:** UCI Machine Learning Repository

**Original data type:** Transaction-level retail data

**Primary use:** Customer segmentation and retail analytics

The raw dataset contains historical transactions including invoice information, product information, quantities, prices, customer identifiers, transaction dates, and country.

## 3. Raw Data Fields

| Field | Description | Data Type | Pipeline Treatment |
|---|---|---|---|
| Invoice | Unique invoice/transaction identifier | String | Used for transaction identification |
| StockCode | Product/item identifier | String | Retained for transaction analysis |
| Description | Product description | String | Retained where required |
| Quantity | Number of units purchased | Numeric | Invalid/non-positive values investigated and removed |
| InvoiceDate | Date and time of transaction | DateTime | Converted to standardized datetime |
| Price | Unit price of product | Numeric | Invalid/non-positive values removed |
| CustomerID | Original customer identifier | Numeric/String | Pseudonymized before analysis |
| Country | Customer country | String | Used for representation/bias assessment |

## 4. Derived Variables

The pipeline creates additional variables required for customer-level analysis.

| Variable | Description | Calculation |
|---|---|---|
| TransactionValue | Total value of a transaction line | Quantity × Price |
| Recency | Number of days since the customer's latest purchase | Analysis Date − Last Purchase Date |
| Frequency | Number of transactions associated with a customer | Count of transactions |
| Monetary | Total customer spending | Sum of TransactionValue |
| AverageOrderValue | Average transaction value for a customer | Monetary ÷ Frequency |

## 5. Final Analytical Dataset

The final output is:

`data/validated/brightcart_customer_rfm.csv`

The dataset is maintained at customer level.

| Variable | Description | Expected Format |
|---|---|---|
| CustomerID | Pseudonymized customer identifier | CUST_00001 |
| Recency | Days since most recent purchase | Integer ≥ 0 |
| Frequency | Number of transactions | Integer > 0 |
| Monetary | Total spending | Numeric ≥ 0 |
| AverageOrderValue | Average transaction value | Numeric ≥ 0 |
| LastPurchaseDate | Most recent purchase date | Date |

## 6. Data Quality Rules

The pipeline applies the following quality rules:

- CustomerID must not be missing.
- CustomerID must be unique in the customer-level dataset.
- Recency must not be negative.
- Frequency must be greater than zero.
- Monetary must not be negative.
- AverageOrderValue must not be negative.
- Required RFM variables must not contain missing values.
- Transaction dates must be valid.
- Quantity must be greater than zero after the defined cleaning process.
- Price must be greater than zero after the defined cleaning process.

## 7. Data Transformation Flow

```text
Raw Transaction Data
        ↓
Data Cleaning
        ↓
Customer ID Pseudonymization
        ↓
Transaction Value Calculation
        ↓
Customer Aggregation
        ↓
RFM Feature Engineering
        ↓
Validated Customer Dataset
