
---

# 4. `docs/pipeline_documentation.md`

```markdown
# BrightCart Data Pipeline Documentation

## 1. Project Overview

The BrightCart Data Pipeline transforms raw Online Retail II transaction data into a clean, anonymized and validated customer-level dataset for customer segmentation.

The pipeline is designed to be reproducible, testable and scalable.

## 2. Business Objective

BrightCart aims to identify meaningful customer groups using transaction behaviour.

The final analytical dataset will support:

- RFM analysis
- Customer segmentation
- K-Means clustering
- Targeted marketing
- Customer relationship management
- Operational decision-making

## 3. Pipeline Architecture

```text
                 RAW DATA
                    │
                    ▼
             ┌─────────────┐
             │  INGESTION  │
             └──────┬──────┘
                    ▼
             ┌─────────────┐
             │   CLEANING  │
             └──────┬──────┘
                    ▼
             ┌─────────────┐
             │ANONYMIZATION│
             └──────┬──────┘
                    ▼
             ┌─────────────┐
             │TRANSFORMATION│
             └──────┬──────┘
                    ▼
             ┌─────────────┐
             │ VALIDATION  │
             └──────┬──────┘
                    ▼
             ┌─────────────┐
             │BIAS CHECKING│
             └──────┬──────┘
                    ▼
             ┌─────────────┐
             │ AUDIT LOG   │
             └──────┬──────┘
                    ▼
          CUSTOMER RFM DATASET
                    │
                    ▼
             MODULE 4 MODEL
