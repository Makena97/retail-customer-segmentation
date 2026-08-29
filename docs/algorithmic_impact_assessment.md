# BrightCart Algorithmic Impact Assessment

## 1. System Overview

BrightCart uses a machine-learning model to estimate the probability that an existing customer will make another purchase within 90 days.

The model is intended to support customer-retention and marketing decisions by helping BrightCart identify customers who may be more or less likely to return.

The model provides decision support. It should not independently make high-impact decisions concerning customers.

---

## 2. Intended Use

The system may be used to:

- support customer-retention planning;
- prioritize marketing analysis;
- identify customer groups for further business review;
- support targeted engagement strategies; and
- improve understanding of repeat-purchase behaviour.

The model should not be used to determine access to employment, healthcare, credit, insurance, housing, education, or other high-impact services.

---

## 3. Model Inputs

The prediction model uses customer-level behavioural features:

- Recency_Days;
- Frequency;
- Monetary;
- Avg_Order_Value;
- Total_Quantity;
- Unique_Products; and
- Tenure_Days.

Direct demographic characteristics such as race, gender and age are not included in the model.

Customer identifiers are not used as predictive features.

---

## 4. Model Output

The system produces:

- a binary repeat-purchase prediction; and
- a probability representing estimated likelihood of repeat purchase within 90 days.

The prediction should be interpreted as a statistical estimate rather than a guaranteed future customer action.

---

## 5. Potential Benefits

Potential benefits include:

- more focused customer-retention activity;
- improved allocation of marketing resources;
- better understanding of customer purchasing patterns;
- reduced reliance on broad untargeted campaigns; and
- more evidence-based business decisions.

---

## 6. Potential Risks

Potential risks include:

| Risk | Potential Impact | Control |
|---|---|---|
| Incorrect prediction | Customer may be incorrectly prioritized | Monitor precision, recall and error rates |
| Data drift | Model becomes less representative | Monitor feature distributions |
| Concept drift | Relationship between behaviour and repeat purchase changes | Monitor production performance |
| Group disparity | Different customer groups may experience different model outcomes | Continuous fairness monitoring |
| Small subgroup samples | Fairness results may be unreliable | Report sample sizes and avoid overinterpretation |
| Privacy risk | Customer behavioural data may be exposed or misused | Pseudonymization, access controls and data governance |
| Over-reliance on AI | Staff may treat prediction as certainty | Human oversight and model documentation |
| Explainability limitations | Stakeholders may misunderstand model behaviour | SHAP analysis and model card |
| Model misuse | Prediction may be applied outside its intended purpose | Defined intended-use and governance controls |

---

## 7. Fairness Impact

Fairness was explored using geographic grouping because the source data did not provide direct demographic protected attributes.

The validation fairness sample contained:

- 967 UK customers; and
- 89 Non-UK customers.

Baseline fairness measures included:

- Demographic Parity Difference: 0.1094
- Disparate Impact Ratio: 0.7883
- Equal Opportunity Difference: 0.1203
- Equalized Odds Difference: 0.1203

These findings are exploratory because the Non-UK subgroup is relatively small.

Country grouping should not be interpreted as a substitute for race, ethnicity or other demographic protected characteristics.

---

## 8. Explainability

SHAP analysis is used to explain model behaviour.

The strongest global predictor identified during validation was Recency_Days, followed by Monetary, Frequency, Unique_Products and Total_Quantity.

Local explanations may be used to investigate individual predictions.

Counterfactual analysis can additionally demonstrate how changes in customer behaviour may alter a prediction.

Explanations should support interpretation and investigation rather than imply causal relationships.

---

## 9. Human Oversight

The model should support rather than replace human business judgement.

Human review is particularly important when:

- monitoring thresholds are breached;
- fairness metrics deteriorate;
- unusual predictions occur;
- data drift is detected;
- customer complaints arise; or
- a model retraining or retirement decision is considered.

---

## 10. Monitoring Controls

The deployed system establishes monitoring for:

- accuracy;
- precision;
- recall;
- F1 score;
- ROC-AUC;
- feature drift;
- prediction drift;
- fairness metrics; and
- model incidents.

The current dashboard uses validated results as the initial baseline. Long-term production performance and drift will only be reported once sufficient post-deployment evidence becomes available.

---

## 11. Accountability and Auditability

Model lifecycle evidence should include:

- source code and version history;
- data-quality checks;
- experiment records;
- model versions;
- performance results;
- fairness assessments;
- SHAP explanations;
- monitoring outputs;
- incident records; and
- deployment and decommissioning decisions.

GitHub, MLflow, model documentation and monitoring artifacts provide supporting traceability for the project.

---

## 12. Overall Impact Assessment

The BrightCart system is considered a relatively limited-impact decision-support application because it predicts repeat purchasing for marketing and retention purposes rather than determining access to essential services or legal rights.

However, limited impact does not eliminate ethical obligations.

Incorrect predictions, privacy failures, systematic group disparities, model drift and inappropriate use remain possible. The system therefore requires continued monitoring, human oversight, documented governance and appropriate incident-response procedures.

Deployment should remain conditional on the model continuing to demonstrate acceptable performance, responsible data use and manageable fairness risk.
