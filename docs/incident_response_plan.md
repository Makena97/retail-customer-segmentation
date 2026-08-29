# BrightCart Ethical AI Incident Response Plan

## 1. Purpose

This plan defines how BrightCart will identify, assess, respond to, document, and resolve incidents involving the repeat-purchase prediction system.

The objective is to ensure that model-related issues are handled consistently and that customer impact, unfair treatment, privacy risk, and inappropriate business decisions are minimized.

---

## 2. What Constitutes an AI Incident?

An AI incident may include:

- significant deterioration in model performance;
- unexpected or unreliable predictions;
- material data drift or prediction drift;
- deterioration in fairness metrics;
- substantially different error rates between monitored customer groups;
- inappropriate use of model predictions;
- exposure or misuse of customer data;
- failure of the prediction API or data pipeline;
- incorrect or misleading model explanations;
- stakeholder or customer complaints concerning model decisions; or
- use of an outdated or unapproved model version.

---

## 3. Incident Severity

| Severity | Description | Example |
|---|---|---|
| Low | Limited impact with no significant customer harm | Temporary monitoring failure |
| Medium | Model reliability or fairness concern requiring investigation | Sustained performance decline |
| High | Significant customer, privacy, fairness, or business impact | Material subgroup disparity or serious data-quality failure |
| Critical | Severe or widespread harm requiring immediate intervention | Privacy breach or systematically harmful model behaviour |

Severity should consider the number of customers affected, duration, business impact, fairness implications, privacy risk, and reversibility of the consequences.

---

## 4. Detection

Potential incidents may be identified through:

- model performance monitoring;
- data and prediction drift monitoring;
- fairness and bias-drift monitoring;
- API and system monitoring;
- data-quality validation;
- SHAP or other explanation reviews;
- stakeholder feedback;
- customer complaints; and
- periodic governance reviews.

Monitoring alerts initiate investigation and do not automatically prove that an ethical violation has occurred.

---

## 5. Immediate Response

When an incident is detected:

1. Record the incident and detection time.
2. Identify the affected model version and data period.
3. Assess the severity and potential customer impact.
4. Preserve relevant logs, predictions, explanations and monitoring evidence.
5. Determine whether the model can continue operating safely.
6. Escalate significant incidents to the appropriate responsible stakeholders.

For high or critical incidents, prediction services may be temporarily suspended while investigation is conducted.

---

## 6. Investigation

The investigation should examine:

- model performance;
- subgroup performance and fairness metrics;
- data quality;
- feature distributions and drift;
- prediction distributions;
- recent pipeline or code changes;
- model version and configuration;
- individual prediction explanations where relevant; and
- whether the model was used outside its intended purpose.

The investigation should distinguish between model failure, data failure, infrastructure failure and inappropriate business use.

---

## 7. Corrective Actions

Depending on the cause, corrective actions may include:

- correcting data-quality problems;
- rolling back a recent deployment;
- restoring a previously validated model version;
- recalibrating or retraining the model;
- reviewing model features;
- reassessing classification thresholds;
- applying appropriate fairness mitigation;
- updating business rules;
- improving monitoring controls; or
- temporarily suspending the prediction system.

Any materially modified model should be revalidated before production redeployment.

---

## 8. Fairness-Related Incidents

Potential fairness incidents require additional review of:

- subgroup sample sizes;
- demographic parity;
- disparate impact;
- equal opportunity;
- equalized odds;
- true-positive and false-positive rates; and
- potential proxy effects in model features.

The current UK versus Non-UK fairness analysis is exploratory because of the relatively small Non-UK validation sample.

A change in a fairness metric therefore triggers investigation rather than an automatic conclusion of discriminatory behaviour.

---

## 9. Privacy and Data Governance Incidents

If an incident involves customer data, BrightCart should determine:

- what information was involved;
- whether unauthorized access occurred;
- how many records or customers were affected;
- whether pseudonymization or access controls failed;
- whether the information can be recovered or contained; and
- whether notification or regulatory obligations apply.

Access to investigation data should follow the project's established data-governance and privacy controls.

---

## 10. Recovery and Validation

Before returning a suspended or modified model to normal operation:

1. Confirm that the root cause has been addressed.
2. Repeat data-quality validation.
3. Reassess model performance.
4. Reassess fairness.
5. Review explainability outputs.
6. Confirm the correct model version.
7. Document approval for redeployment.
8. Continue enhanced monitoring following release.

---

## 11. Incident Documentation

Each incident record should contain:

- incident identifier;
- detection date and time;
- model version;
- incident description;
- affected data or customers;
- severity classification;
- monitoring evidence;
- investigation findings;
- corrective actions;
- fairness and privacy considerations;
- approval decisions;
- resolution date; and
- lessons learned.

This record provides traceability and supports future governance reviews.

---

## 12. Post-Incident Review

Following a significant incident, BrightCart should perform a post-incident review to determine:

- why the incident occurred;
- why existing controls did or did not detect it;
- whether monitoring thresholds require adjustment;
- whether additional tests or governance controls are needed; and
- how recurrence can be prevented.

Lessons learned should be incorporated into the monitoring, development and deployment processes.

---

## 13. Escalation to Model Decommissioning

Repeated or severe incidents may indicate that corrective actions are insufficient.

The model should be considered for decommissioning where it:

- repeatedly fails performance requirements;
- produces persistent unacceptable fairness concerns;
- can no longer be supported by representative data;
- creates unacceptable privacy or ethical risk;
- no longer addresses the intended business need; or
- is replaced by a demonstrably safer and more effective solution.
