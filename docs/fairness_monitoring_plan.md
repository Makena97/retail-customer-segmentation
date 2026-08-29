# BrightCart Fairness Monitoring Plan

## 1. Purpose

The purpose of this Fairness Monitoring Plan is to ensure that the BrightCart repeat-purchase prediction model continues to operate responsibly after deployment.

Fairness monitoring will focus on identifying whether prediction outcomes or error rates become materially different between customer groups over time. Fairness results will support human review and will not be used as the sole basis for automatic model retraining or business decisions.

---

## 2. Fairness Attribute

The available dataset does not contain direct demographic characteristics such as age, gender, race, or disability status.

Country information was therefore used to create the following geographic groups for exploratory fairness assessment:

- UK customers
- Non-UK customers

Geographic region is treated as a monitoring attribute for this project rather than as a substitute for demographic protected characteristics.

---

## 3. Baseline Fairness Results

The model validation test sample contained:

| Group | Customers |
|---|---:|
| UK | 967 |
| Non-UK | 89 |

The baseline fairness assessment produced:

| Fairness Metric | Baseline |
|---|---:|
| Demographic Parity Difference | 0.1094 |
| Disparate Impact Ratio | 1.2685 |
| Equal Opportunity Difference | 0.1203 |
| Equalized Odds Difference | 0.1203 |
| TPR Difference | 0.1203 |
| FPR Difference | 0.1152 |

These results should be interpreted cautiously because the Non-UK test sample contains only 89 customers. The fairness assessment is therefore exploratory rather than conclusive.

---

## 4. Continuous Fairness Monitoring

When sufficient new production data and observed customer outcomes become available, fairness metrics will be recalculated for UK and Non-UK customers.

Monitoring will include:

- prediction rates by group;
- true-positive rates;
- false-positive rates;
- demographic parity difference;
- disparate impact ratio;
- equal opportunity difference; and
- equalized odds difference.

Production results will be compared with the established validation baseline and with previous monitoring periods.

Fairness should be assessed alongside model performance and data drift rather than interpreted as a single isolated metric.

---

## 5. Bias Drift

Bias drift occurs when differences in model behaviour between monitored groups materially change over time.

Potential indicators include:

- increasing differences in positive prediction rates;
- increasing differences in true-positive or false-positive rates;
- deterioration in demographic parity;
- deterioration in equal opportunity;
- substantial movement in the disparate impact ratio; and
- changes in the geographic composition of customers.

Changes will trigger investigation rather than automatic conclusions that discrimination has occurred.

---

## 6. Monitoring Frequency

Fairness should initially be reviewed monthly once sufficient production outcomes are available.

A review may be performed earlier where:

- substantial data drift is detected;
- model performance deteriorates;
- customer population composition changes significantly;
- a fairness-related complaint is received; or
- a material model or data pipeline change is introduced.

Where subgroup sample sizes are too small for reliable interpretation, results will be labelled exploratory and additional observations will be collected before strong conclusions are made.

---

## 7. Fairness Investigation and Mitigation

Where potential unfairness is identified, the following process will be followed:

1. Verify data quality and subgroup sample sizes.
2. Confirm that the observed difference is reproducible.
3. Examine model errors separately for each monitored group.
4. Review feature distributions and potential proxy effects.
5. Evaluate whether the difference has a legitimate business explanation.
6. Test appropriate mitigation strategies where necessary.
7. Revalidate model performance and fairness before redeployment.
8. Document the investigation, decision and outcome.

Possible mitigation approaches may include data rebalancing, feature review, model retraining, threshold assessment, or additional data collection.

No mitigation technique will be deployed solely because it improves one fairness metric if it creates unacceptable performance, operational, or ethical consequences elsewhere.

---

## 8. Escalation

A fairness concern should be escalated where:

- disparities materially worsen over successive monitoring periods;
- a subgroup experiences substantially poorer error rates;
- data quality issues affect a particular group;
- a stakeholder raises a credible fairness concern; or
- the model can no longer be demonstrated to operate within approved responsible-AI requirements.

Serious concerns may result in temporary suspension of automated predictions while the issue is investigated.

---

## 9. Documentation and Auditability

Fairness assessments should record:

- evaluation date;
- model version;
- dataset or monitoring period;
- subgroup sample sizes;
- fairness metrics;
- identified concerns;
- investigation performed;
- mitigation decisions; and
- approval or escalation outcome.

SHAP and other explanation outputs should also be retained where they are relevant to investigating group-level or individual prediction behaviour.

This provides an auditable record of how fairness concerns were identified, investigated and resolved.

---

## 10. Current Monitoring Status

The BrightCart model currently has an established validation fairness baseline.

Because sufficient post-deployment outcome data has not yet accumulated, the project does not claim to have measured long-term production fairness or bias drift.

The deployed monitoring framework establishes how these measures will be evaluated as production evidence becomes available.
