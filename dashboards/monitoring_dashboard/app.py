import streamlit as st
import pandas as pd


# ---------------------------------------------------------
# Page configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="BrightCart Model Monitoring",
    page_icon="📊",
    layout="wide"
)


# ---------------------------------------------------------
# Title
# ---------------------------------------------------------

st.title("BrightCart Model Monitoring Dashboard")

st.caption(
    "Repeat Purchase Prediction | Performance, Drift and Fairness Monitoring"
)

st.info(
    "This dashboard establishes the initial monitoring baseline "
    "using model validation results. Production metrics will be "
    "compared against these values as new prediction and outcome "
    "data become available."
)


# ---------------------------------------------------------
# Baseline model performance
# ---------------------------------------------------------

st.header("1. Model Performance Baseline")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    label="Accuracy",
    value="73.3%"
)

col2.metric(
    label="ROC-AUC",
    value="0.799"
)

col3.metric(
    label="Recall",
    value="67.3%"
)

col4.metric(
    label="F1 Score",
    value="68.5%"
)


# ---------------------------------------------------------
# Model status
# ---------------------------------------------------------

st.subheader("Model Status")

st.success(
    "Model deployed and operational. "
    "Current values represent the validated baseline."
)


# ---------------------------------------------------------
# Performance monitoring table
# ---------------------------------------------------------

st.header("2. Performance Monitoring")

performance_data = pd.DataFrame({
    "Metric": [
        "Accuracy",
        "ROC-AUC",
        "Precision",
        "Recall",
        "F1 Score"
    ],
    "Baseline": [
        0.733,
        0.799,
        0.698,
        0.673,
        0.685
    ],
    "Monitoring Threshold": [
        0.68,
        0.75,
        0.65,
        0.60,
        0.63
    ]
})

# Automatically assess each performance metric
performance_data["Status"] = performance_data.apply(
    lambda row: (
        "Within Threshold"
        if row["Baseline"] >= row["Monitoring Threshold"]
        else "Review Required"
    ),
    axis=1
)

st.dataframe(
    performance_data,
    use_container_width=True,
    hide_index=True
)

# Overall monitoring status
if (performance_data["Status"] == "Review Required").any():
    st.error(
        "Performance Alert: At least one model metric "
        "requires investigation."
    )
else:
    st.success(
        "Performance Status: All baseline metrics are "
        "currently within the proposed monitoring thresholds."
    )

st.caption(
    "Monitoring thresholds are proposed operational triggers. "
    "A sustained decline below a threshold should initiate "
    "model investigation rather than automatic retraining."
)

# ---------------------------------------------------------
# Data drift
# ---------------------------------------------------------

st.header("3. Data Drift Monitoring")

st.write(
    """
    Production customer characteristics should be compared with
    the training baseline to identify changes in customer behaviour.
    """
)

drift_data = pd.DataFrame({
    "Feature": [
        "Recency_Days",
        "Frequency",
        "Monetary",
        "Avg_Order_Value",
        "Total_Quantity",
        "Unique_Products",
        "Tenure_Days"
    ],
    "Monitoring Method": [
        "Distribution comparison",
        "Distribution comparison",
        "Distribution comparison",
        "Distribution comparison",
        "Distribution comparison",
        "Distribution comparison",
        "Distribution comparison"
    ],
    "Current Status": [
        "Baseline established",
        "Baseline established",
        "Baseline established",
        "Baseline established",
        "Baseline established",
        "Baseline established",
        "Baseline established"
    ]
})

st.dataframe(
    drift_data,
    use_container_width=True,
    hide_index=True
)

st.warning(
    "Live drift statistics require sufficient production data. "
    "No artificial production history is displayed."
)


# ---------------------------------------------------------
# Prediction drift
# ---------------------------------------------------------

st.header("4. Prediction Drift")

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Validation Repeat-Purchase Rate",
        "43.2%"
    )

with col2:

    st.metric(
        "Production Prediction Distribution",
        "Pending"
    )

st.write(
    """
    The proportion of customers predicted to make a repeat
    purchase will be monitored against the validation baseline.
    Large sustained changes may indicate customer behaviour
    changes, data drift, or model degradation.
    """
)


# ---------------------------------------------------------
# Fairness monitoring
# ---------------------------------------------------------

st.header("5. Fairness Monitoring")

fairness_data = pd.DataFrame({
    "Metric": [
        "Demographic Parity Difference",
        "Disparate Impact Ratio",
        "Equal Opportunity Difference",
        "Equalized Odds Difference"
    ],
    "Baseline Result": [
        0.1094,
        1.2685,
        0.1203,
        0.1203
    ]
})

st.dataframe(
    fairness_data,
    use_container_width=True,
    hide_index=True
)

st.warning(
    "Fairness results are exploratory. The validation sample "
    "contained 967 UK customers and only 89 Non-UK customers. "
    "The smaller Non-UK sample limits statistical reliability."
)


# ---------------------------------------------------------
# Explainability monitoring
# ---------------------------------------------------------

st.header("6. Explainability Monitoring")

feature_importance = pd.DataFrame({
    "Feature": [
        "Recency_Days",
        "Monetary",
        "Frequency",
        "Unique_Products",
        "Total_Quantity",
        "Tenure_Days",
        "Avg_Order_Value"
    ],
    "Mean Absolute SHAP": [
        0.1235,
        0.0469,
        0.0394,
        0.0376,
        0.0376,
        0.0181,
        0.0147
    ]
})

st.bar_chart(
    feature_importance.set_index("Feature")
)

st.caption(
    "Recency_Days was the strongest driver of repeat-purchase "
    "predictions during model validation."
)


# ---------------------------------------------------------
# Monitoring alerts
# ---------------------------------------------------------

st.header("7. Monitoring Alerts")

st.success("No production performance alerts recorded.")

st.info(
    "Future alerts should be generated when performance, "
    "drift, or fairness indicators exceed agreed thresholds."
)


# ---------------------------------------------------------
# Monitoring actions
# ---------------------------------------------------------

st.header("8. Response Actions")

response_actions = pd.DataFrame({
    "Condition": [
        "Performance below threshold",
        "Significant feature drift",
        "Prediction distribution shift",
        "Fairness deterioration",
        "Repeated ethical or technical failure"
    ],
    "Action": [
        "Investigate and validate model",
        "Review incoming data and retrain if necessary",
        "Review customer behaviour and model calibration",
        "Conduct fairness review and mitigation assessment",
        "Suspend or decommission model"
    ]
})

st.dataframe(
    response_actions,
    use_container_width=True,
    hide_index=True
)


# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------

st.divider()

st.caption(
    "BrightCart Repeat Purchase Prediction System | "
    "Model Monitoring and Responsible AI"
)
