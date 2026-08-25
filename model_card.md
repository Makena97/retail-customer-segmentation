# Model Card: BrightCart 90-Day Repeat Purchase Prediction Model

## 1. Model Overview

**Model Name:** BrightCart 90-Day Repeat Purchase Prediction Model

**Model Type:** Random Forest Classifier

**Model Version:** 1.0

**Prediction Task:** Binary classification

**Target Variable:** Repeat_Purchase_90d

**Positive Class:** Customer makes a repeat purchase within 90 days.

**Negative Class:** Customer does not make a repeat purchase within 90 days.

The model was developed to identify customers who are likely to make a repeat
purchase within a 90-day prediction horizon. The intended business use is to
support customer retention and marketing prioritization.

---

## 2. Training Data

The model was developed using customer-level features derived from the
Online Retail II transactional dataset.

The cleaned transactional dataset contained 1,007,914 records after
59,457 records were removed during data cleaning.

The final customer-level modeling dataset contained 5,278 customers.

The model uses the following seven predictors:

- Recency_Days
- Frequency
- Monetary
- Avg_Order_Value
- Total_Quantity
- Unique_Products
- Tenure_Days

Customer_ID was retained for identification and analysis but was excluded
from the model predictors.

---

## 3. Data Splitting and Validation

The customer modeling dataset was divided using a stratified 80/20
train-test split with random_state=42.

The final test dataset contained 1,056 customers.

Five-fold stratified cross-validation was used during model evaluation
and hyperparameter tuning.

A majority-class classifier was used as the baseline model.

---

## 4. Models Evaluated

Three classification algorithms were evaluated:

1. Logistic Regression
2. Random Forest
3. Gradient Boosting

Initial test ROC-AUC results were:

| Model | ROC-AUC |
|---|---:|
| Majority Class Baseline | 0.500 |
| Logistic Regression | 0.802 |
| Random Forest | 0.795 |
| Gradient Boosting | 0.805 |

Cross-validation demonstrated stable performance across the candidate
models.

The Random Forest was selected for further tuning because it provided
competitive predictive performance while supporting tree-based SHAP
explanations.

---

## 5. Final Model Configuration

The tuned Random Forest used:

- n_estimators = 300
- max_depth = 10
- min_samples_leaf = 4
- min_samples_split = 2
- class_weight = balanced
- random_state = 42

Best cross-validation ROC-AUC:

**0.799**

Final test performance:

| Metric | Value |
|---|---:|
| Accuracy | 0.733 |
| Precision | 0.698 |
| Recall | 0.673 |
| F1 Score | 0.685 |
| ROC-AUC | 0.799 |

---

## 6. Explainability

SHAP was used for global and local model interpretation.

Global mean absolute SHAP importance:

| Feature | Mean Absolute SHAP |
|---|---:|
| Recency_Days | 0.1235 |
| Monetary | 0.0469 |
| Frequency | 0.0394 |
| Unique_Products | 0.0376 |
| Total_Quantity | 0.0376 |
| Tenure_Days | 0.0181 |
| Avg_Order_Value | 0.0147 |

Recency_Days was the dominant predictor. Customers who purchased more
recently generally received higher predicted probabilities of repeat
purchase.

Monetary value and purchase frequency were the next most influential
features.

These relationships describe model behavior and should not be interpreted
as causal relationships.

---

## 7. Local Explanation

A local SHAP explanation was evaluated for an individual customer with
an approximately 0.80 predicted probability of repeat purchase.

Recency_Days = 31 was the largest positive contributor to the prediction.
Tenure, purchase frequency, total quantity, monetary value, and average
order value also contributed positively.

This demonstrates that individual model predictions can be decomposed into
business-interpretable feature contributions.

---

## 8. Counterfactual Analysis

For the selected customer, the original prediction was:

- Recency_Days = 31
- Repeat-purchase probability = 0.800
- Predicted class = 1

Holding all other customer characteristics constant, Recency_Days was
progressively increased.

The first observed classification change occurred at:

- Recency_Days = 274
- Repeat-purchase probability = 0.4997
- Predicted class = 0

The counterfactual therefore required an increase of approximately 243
days in recency for this particular observation to cross the model's
0.50 decision threshold.

This counterfactual illustrates model behavior and does not establish
causality.

---

## 9. Fairness Evaluation

The source dataset does not contain conventional protected demographic
attributes such as gender, race, or age.

Country was therefore used only as an available geographic grouping
variable for group-level fairness diagnostics and should not be interpreted
as a substitute for protected demographic attributes.

The customer population was geographically imbalanced:

- UK customers: 91.02%
- Non-UK customers: 8.98%

The test dataset contained:

- UK: 967 customers
- Non-UK: 89 customers

Original model fairness metrics:

| Metric | Value |
|---|---:|
| Demographic Parity Difference | 0.109 |
| Disparate Impact Ratio | 0.788 |
| Equalized Odds Difference | 0.120 |

The disparate impact ratio fell slightly below the commonly used 0.80
screening threshold and was treated as a potential disparity requiring
investigation rather than definitive evidence of discrimination.

---

## 10. Bias Mitigation

Inverse-frequency sample weighting was evaluated to increase the influence
of the underrepresented Non-UK training observations.

The weighted model achieved:

- Accuracy = 0.733
- Precision = 0.691
- Recall = 0.691
- F1 = 0.691
- ROC-AUC = 0.803

However, fairness metrics worsened:

| Metric | Before | After Weighting |
|---|---:|---:|
| Demographic Parity Difference | 0.109 | 0.130 |
| Disparate Impact Ratio | 0.788 | 0.764 |
| Equalized Odds Difference | 0.120 | 0.143 |

The mitigation strategy was therefore rejected.

The original tuned Random Forest was retained because the weighting
strategy did not improve geographic group fairness.

---

## 11. Sensitivity Analysis

Robustness was evaluated by perturbing Recency_Days, Monetary, and
Frequency by ±10%.

No perturbation scenario changed more than 2.65% of test classifications.

Recency_Days produced the greatest sensitivity. Increasing Recency_Days
by 10% resulted in a mean absolute probability change of 0.0197 and
changed 2.65% of classifications.

The model was therefore considered reasonably robust to modest input
variations at the population level, although some individual predictions
showed greater sensitivity.

---

## 12. Intended Use

The model is intended to support:

- Customer retention analysis
- Identification of customers likely to purchase again
- Marketing prioritization
- Customer engagement planning
- Analytical decision support

Model predictions should supplement rather than replace business judgment.

---

## 13. Out-of-Scope Uses

The model should not be used for:

- Credit or lending decisions
- Employment decisions
- Insurance decisions
- Healthcare decisions
- Legal decisions
- Determining customer eligibility for essential services
- Inferring protected demographic characteristics

The model was developed specifically for retail repeat-purchase prediction.

---

## 14. Limitations

Important limitations include:

1. The dataset is historical and may not represent future purchasing
   behavior.

2. Approximately 91% of customers are from the United Kingdom, creating
   geographic representation imbalance.

3. The dataset does not contain conventional protected demographic
   attributes, limiting formal demographic fairness assessment.

4. The Non-UK test sample contains only 89 customers, making its fairness
   estimates less stable.

5. Customer behavior may change because of economic conditions,
   promotions, seasonality, competitor actions, or changes in the product
   portfolio.

6. SHAP and counterfactual explanations describe model behavior rather
   than causal relationships.

---

## 15. Monitoring Recommendations

Post-deployment monitoring should include:

- ROC-AUC
- Recall
- Precision
- F1 score
- Prediction distribution
- Repeat-purchase prevalence
- Feature distribution drift
- Recency_Days distribution
- Monetary distribution
- Frequency distribution
- UK vs Non-UK performance
- Demographic parity difference
- Disparate impact ratio
- Equalized odds difference

Material deterioration in predictive performance, input distributions,
or geographic fairness metrics should trigger investigation and potential
model retraining.

---

## 16. Model Governance

The production model should be versioned and registered using MLflow.

Each model version should document:

- Training dataset version
- Hyperparameters
- Validation metrics
- Fairness metrics
- Explainability artifacts
- Model owner
- Approval status
- Deployment date

The model should be periodically reviewed and retrained when meaningful
data or performance drift is detected.
