# Great Expectations Validation

## Purpose

This directory contains the data-quality validation configuration and documentation for the BrightCart Online Retail Customer Segmentation pipeline.

Great Expectations is used to verify that the customer-level analytical dataset meets predefined quality requirements before it is passed to Module 4 for RFM analysis and K-Means customer segmentation.

## Dataset Being Validated

The primary dataset being validated is:

`data/validated/brightcart_customer_rfm.csv`

The dataset contains customer-level features generated from the Online Retail II transactional dataset.

### Key Variables

| Variable          | Description                                              |
| ----------------- | -------------------------------------------------------- |
| CustomerID        | Pseudonymized customer identifier                        |
| Recency           | Number of days since the customer's most recent purchase |
| Frequency         | Number of transactions associated with the customer      |
| Monetary          | Total customer transaction value                         |
| AverageOrderValue | Average transaction value for the customer               |
| LastPurchaseDate  | Date of the customer's most recent purchase              |

## Data Quality Expectations

The validation suite checks the following conditions:

### 1. CustomerID completeness

CustomerID must not contain missing values.

**Expectation:**

`CustomerID` should not be null.

### 2. CustomerID uniqueness

The final analytical dataset is maintained at customer level. Therefore, each customer should appear only once.

**Expectation:**

`CustomerID` values must be unique.

### 3. Recency validity

Recency represents the number of days between the analysis date and the customer's most recent purchase.

**Expectation:**

Recency must be greater than or equal to zero.

### 4. Frequency validity

Frequency represents the number of transactions associated with a customer.

**Expectation:**

Frequency must be greater than zero.

### 5. Monetary validity

Monetary represents total customer spending.

**Expectation:**

Monetary values must be greater than or equal to zero.

### 6. Average Order Value validity

AverageOrderValue represents the average transaction value for each customer.

**Expectation:**

AverageOrderValue must be greater than or equal to zero.

### 7. Missing-value validation

Critical RFM variables must not contain missing values.

The following fields are checked:

* CustomerID
* Recency
* Frequency
* Monetary
* AverageOrderValue

### 8. Dataset volume

The pipeline checks that the resulting dataset contains customer records before allowing the workflow to continue.

## Validation Workflow

The validation process occurs after data cleaning, anonymization and RFM feature engineering.

```text
Raw Online Retail II Data
          ↓
      Data Cleaning
          ↓
      Anonymization
          ↓
     RFM Transformation
          ↓
   Customer RFM Dataset
          ↓
 Great Expectations Checks
          ↓
   ┌───────────────┐
   │               │
 PASS            FAIL
   │               │
   ↓               ↓
Continue       Stop Pipeline
   │
   ↓
Bias Detection
   │
   ↓
Module 4 Dataset
```

## Validation Outcome

A validation run is considered successful only when all critical expectations pass.

A failed expectation should prevent an invalid dataset from being used for downstream customer segmentation.

Examples of validation failures include:

* Missing CustomerID
* Duplicate CustomerID
* Negative Recency
* Zero or negative Frequency
* Negative Monetary value
* Missing RFM variables

## Data Quality and Governance

Validation supports the BrightCart Data Governance Framework by ensuring that analytical datasets meet documented quality standards before being used for decision-making.

Validation results should be retained as evidence of the quality checks performed during each pipeline execution.

## Reproducibility

The validation process is automated and forms part of the BrightCart pipeline orchestrated through Apache Airflow.

This ensures that the same data-quality rules are applied consistently whenever the pipeline is executed.

## Module 4 Handoff

The validated customer-level RFM dataset produced by this pipeline will be used in Module 4 for:

1. RFM analysis
2. Feature preparation
3. Customer clustering
4. K-Means model development
5. Customer segment interpretation

The validation stage therefore acts as a quality gate between data engineering and machine-learning development.

## Validation Evidence

Screenshots of successful Great Expectations validation results should be added to the Module 3 PowerPoint presentation as evidence that the validation suite was executed against the BrightCart dataset.

## Status

**Pipeline Stage:** Data Validation

**Tool:** Great Expectations

**Dataset:** `brightcart_customer_rfm.csv`

**Purpose:** Automated data-quality assurance before customer segmentation

