
---

# 2. `docs/privacy_plan.md`

```markdown
# BrightCart Data Privacy and Anonymization Plan

## 1. Purpose

The purpose of this Privacy Plan is to ensure that customer information used in the BrightCart customer segmentation project is handled responsibly and that unnecessary personally identifiable information (PII) is not exposed during data processing or analysis.

The plan builds upon the Ethical AI Charter and Privacy Plan established in Modules 1 and 2.

## 2. Privacy Principles

The BrightCart pipeline follows these principles:

- Data minimization
- Purpose limitation
- Pseudonymization
- Controlled access
- Secure processing
- Transparency
- Limited data retention
- Auditability

## 3. Personally Identifiable Information

The raw retail dataset contains a customer identifier.

The original CustomerID is not required for customer segmentation and therefore should not be exposed in the final analytical dataset.

The pipeline replaces the original CustomerID with a pseudonymous identifier.

Example:

```text
Original CustomerID
        ↓
Pseudonymization
        ↓
CUST_00001
