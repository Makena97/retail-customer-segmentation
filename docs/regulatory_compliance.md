# BrightCart Regulatory Compliance Assessment

## 1. Purpose

This document assesses the principal privacy and data-protection considerations relevant to the BrightCart repeat-purchase prediction system.

The assessment focuses on GDPR principles, the California Consumer Privacy Act (CCPA/CPRA), and HIPAA because these frameworks are identified within the project requirements.

This document is a project-level compliance assessment and does not constitute legal advice or formal certification of regulatory compliance.

---

## 2. BrightCart Data Context

The BrightCart system uses historical retail transaction information to predict whether an existing customer is likely to make another purchase within 90 days.

The analytical dataset includes information such as:

- purchasing frequency;
- monetary value;
- purchase recency;
- average order value;
- quantities purchased;
- number of unique products; and
- customer tenure.

Customer identifiers are not used as predictive model features.

Where identifiers are required during data preparation, appropriate pseudonymization and access controls should be applied.

---

## 3. GDPR Considerations

Retail transaction and customer behavioural information may constitute personal data where it relates to an identified or identifiable individual.

Where GDPR applies, BrightCart should therefore establish an appropriate lawful basis and follow core data-protection requirements.

Relevant controls include:

### Lawfulness, Fairness and Transparency

Customers should receive appropriate information regarding how their personal data is collected and used.

Where behavioural information is used for analytics or profiling, the purpose should be communicated clearly.

### Purpose Limitation

Customer information collected for legitimate retail purposes should not automatically be reused for unrelated purposes without assessing whether the additional processing is lawful and compatible.

The BrightCart model is specifically limited to repeat-purchase prediction and customer-retention decision support.

### Data Minimization

Only information necessary for the prediction objective should be processed.

The final model therefore uses seven behavioural features rather than unnecessary customer information.

### Accuracy

Reasonable controls should ensure that customer transaction information is accurate and that data-quality problems are identified before model predictions are generated.

BrightCart addresses this through data-validation and cleaning controls.

### Storage Limitation

Personal data should not be retained indefinitely without a justified purpose.

Retention periods should therefore be documented, and information should be deleted or anonymized when it is no longer required.

### Integrity and Confidentiality

Appropriate technical and organizational measures should protect customer information against unauthorized access, loss or misuse.

Relevant BrightCart controls include pseudonymization, restricted access, validation, version control and documented incident-response procedures.

### Accountability

BrightCart should maintain evidence demonstrating how privacy and responsible-AI requirements are implemented.

Project documentation, GitHub version history, model records, monitoring evidence and governance documentation contribute to this accountability framework.

---

## 4. Profiling and Automated Decision-Making

The repeat-purchase model evaluates customer behaviour to estimate future purchasing probability and therefore may constitute profiling where GDPR applies.

The system is designed as decision support rather than as a mechanism for making decisions that produce legal or similarly significant effects on customers.

Model predictions should therefore support human business judgement rather than automatically determine access to essential products, services, employment, credit, insurance or other high-impact opportunities.

Where future use materially changes the effect of automated decisions on individuals, an additional privacy and legal assessment should be performed.

---

## 5. Individual Rights

Where GDPR applies, processes should exist to support applicable data-subject rights, including rights relating to:

- information and transparency;
- access;
- correction;
- erasure where applicable;
- restriction of processing;
- data portability where applicable;
- objection; and
- safeguards relating to certain automated decisions and profiling.

BrightCart's technical system should therefore be supported by organizational procedures capable of identifying and responding to relevant customer requests.

---

## 6. CCPA/CPRA Considerations

If BrightCart were subject to the California Consumer Privacy Act, applicable consumers would have rights concerning personal information collected and used by the business.

Relevant operational considerations include:

- informing consumers about collection and use of personal information;
- maintaining appropriate processes for consumer privacy requests;
- providing access to applicable information;
- supporting correction or deletion where legally required;
- respecting applicable rights relating to sale or sharing of personal information; and
- protecting personal information through appropriate security and governance controls.

The BrightCart governance framework therefore emphasizes transparency, defined data use, controlled access, retention management and documented handling of customer information.

Whether CCPA applies to an actual organization would depend on the organization's circumstances and applicable statutory requirements.

---

## 7. HIPAA Assessment

HIPAA is not directly applicable to the current BrightCart retail analytics use case based on the project's described data and purpose.

The system processes retail transaction and customer purchasing information rather than protected health information.

HIPAA primarily applies to covered entities such as certain healthcare providers, health plans and healthcare clearinghouses, as well as applicable business associates.

BrightCart has not been identified in this project as a HIPAA covered entity or business associate, and the project does not process protected health information.

HIPAA should therefore be documented as **not applicable to the current use case**, rather than claiming HIPAA compliance.

If the system were later extended to process protected health information on behalf of a HIPAA-regulated entity, a separate HIPAA assessment would be required.

---

## 8. Privacy-by-Design Controls

The BrightCart project incorporates privacy and governance principles through:

- limiting model features to those required for the business objective;
- excluding direct customer identifiers from model inputs;
- pseudonymization where identifiers are required during processing;
- documented data-quality validation;
- controlled data access;
- retention and deletion considerations;
- model versioning;
- explainability documentation;
- fairness monitoring;
- incident-response procedures; and
- model decommissioning procedures.

These controls support responsible handling of customer information throughout the model lifecycle.

---

## 9. Cross-Border and Cloud Processing

Deployment of analytics or prediction services through cloud infrastructure may involve processing or storage in jurisdictions different from the customer's location.

Before production implementation, BrightCart should therefore document:

- where personal data is stored;
- which service providers process it;
- applicable contractual protections;
- access controls;
- retention arrangements; and
- applicable international-transfer requirements.

The demonstration deployment used for this academic project should not be interpreted as evidence that all requirements for a commercial production deployment have been completed.

---

## 10. Compliance Monitoring

Regulatory compliance should be reviewed throughout the system lifecycle rather than only during initial development.

Reviews should be triggered by:

- changes in the model's intended use;
- introduction of new data sources;
- collection of additional personal attributes;
- significant model redesign;
- new deployment locations;
- new third-party processors;
- privacy or ethical incidents; and
- material regulatory changes.

---

## 11. Overall Assessment

BrightCart is a retail decision-support system rather than a high-impact healthcare, employment, credit or legal decision system.

Nevertheless, customer behavioural information requires responsible handling.

The project's governance approach therefore emphasizes transparency, purpose limitation, data minimization, security, human oversight, fairness monitoring, explainability, incident response and lifecycle management.

GDPR and CCPA/CPRA may impose requirements depending on where BrightCart operates, whose data is processed and whether applicable legal thresholds are met.

HIPAA is not directly applicable to the current retail use case.

Formal commercial deployment would require organization-specific legal and privacy review in addition to the technical controls demonstrated by this project.
