
---

# 3. `docs/governance_framework.md`

```markdown
# BrightCart Data Governance Framework

## 1. Purpose

The BrightCart Data Governance Framework defines how data is accessed, processed, validated, protected, documented and retained throughout the customer segmentation project.

The framework supports data quality, privacy, security, accountability and reproducibility.

## 2. Governance Objectives

The governance framework aims to:

- Maintain reliable and accurate data.
- Protect customer information.
- Ensure appropriate data access.
- Establish accountability for data processing.
- Support reproducible analytics.
- Maintain audit trails.
- Reduce risks associated with poor-quality or biased data.

## 3. Data Ownership

The BrightCart analytics project should assign clear responsibility for different data activities.

| Role | Responsibility |
|---|---|
| Data Owner | Defines acceptable use and business requirements |
| Data Engineer | Builds and maintains the data pipeline |
| Data Analyst | Uses validated analytical data |
| Project Manager | Oversees project delivery and compliance |
| Business Stakeholder | Uses analytical results for business decisions |

## 4. Access Control

Access should follow the principle of least privilege.

Users should receive only the level of access necessary to perform their responsibilities.

### Raw Data

Restricted to authorized technical users.

### Processed Data

Available to authorized members of the analytics team.

### Analytical Dataset

Available to analysts and approved project stakeholders.

### Business Outputs

Aggregated customer segment results can be shared with authorized business stakeholders.

## 5. Data Quality Governance

Data quality is maintained through automated validation.

The pipeline checks:

- Completeness
- Uniqueness
- Validity
- Consistency
- Accuracy-related rules
- Range constraints

Great Expectations is used to implement automated data-quality expectations.

Pytest is used to test individual processing functions.

## 6. Data Lineage

The project maintains traceability from the original dataset to the final analytical output.

```text
Online Retail II
      ↓
Raw Data
      ↓
Ingestion
      ↓
Cleaning
      ↓
Anonymization
      ↓
Transformation
      ↓
Validation
      ↓
Bias Assessment
      ↓
Customer RFM Dataset
      ↓
K-Means Segmentation
