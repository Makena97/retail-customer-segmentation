import streamlit as st
import pandas as pd


# ---------------------------------------------------------
# Page configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="BrightCart Model Explainability",
    page_icon="🔎",
    layout="wide"
)


# ---------------------------------------------------------
# Header
# ---------------------------------------------------------

st.title("BrightCart Model Explainability Dashboard")

st.caption(
    "Understanding why the repeat-purchase model makes its predictions"
)

st.info(
    "This dashboard uses model validation evidence to explain the "
    "BrightCart Random Forest model. Feature importance represents "
    "predictive association and should not be interpreted as causation."
)


# ---------------------------------------------------------
# Model overview
# ---------------------------------------------------------

st.header("1. What Does the Model Predict?")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Prediction Horizon",
    "90 days"
)

col2.metric(
    "ROC-AUC",
    "0.799"
)

col3.metric(
    "Accuracy",
    "73.3%"
)

st.write(
    """
    The model estimates the probability that an existing BrightCart
    customer will make another purchase within 90 days.

    Explainability helps stakeholders understand which customer
    characteristics influenced the model rather than treating the
    prediction as a black box.
    """
)


# ---------------------------------------------------------
# Global SHAP
# ---------------------------------------------------------

st.header("2. Global SHAP Feature Importance")

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

st.dataframe(
    feature_importance,
    use_container_width=True,
    hide_index=True
)

st.success(
    "Recency_Days is the strongest global predictor in the "
    "validated model."
)

st.write(
    """
    **Business interpretation:** how recently a customer purchased
    provides substantially more predictive information than any
    individual spending or frequency measure.

    Monetary value, purchase frequency, product variety and total
    quantity also contribute to the model's predictions.
    """
)


# ---------------------------------------------------------
# SHAP explanation
# ---------------------------------------------------------

st.header("3. How to Interpret SHAP")

st.write(
    """
    SHAP assigns each model feature a contribution to a prediction.

    For an individual customer:

    - a feature may push the prediction toward repeat purchase;
    - a feature may push the prediction away from repeat purchase; or
    - a feature may have relatively little influence.

    The global values above use **mean absolute SHAP values**. They
    measure the average magnitude of each feature's influence across
    customers, regardless of whether that influence increases or
    decreases the predicted probability.
    """
)

st.warning(
    "A high SHAP value does not mean that changing the feature will "
    "necessarily cause customer behaviour to change."
)


# ---------------------------------------------------------
# Local example
# ---------------------------------------------------------

st.header("4. Individual Prediction Example")

local_example = pd.DataFrame({
    "Customer Characteristic": [
        "Recency_Days",
        "Frequency",
        "Monetary",
        "Avg_Order_Value"
    ],
    "Value": [
        "16 days",
        "9 orders",
        "2,391.16",
        "265.68"
    ]
})

col1, col2 = st.columns([1, 1])

with col1:

    st.subheader("Customer Profile")

    st.dataframe(
        local_example,
        use_container_width=True,
        hide_index=True
    )

with col2:

    st.subheader("Prediction")

    st.metric(
        "Repeat-Purchase Probability",
        "80%"
    )

    st.success(
        "Higher probability of repeat purchase"
    )

st.write(
    """
    This example customer purchased relatively recently and had
    repeated purchasing activity. The model assigned the customer
    a relatively high probability of purchasing again.

    A local SHAP explanation can be used to identify which features
    contributed most strongly to this individual prediction.
    """
)


# ---------------------------------------------------------
# Counterfactual
# ---------------------------------------------------------

st.header("5. Counterfactual Explanation")

st.write(
    """
    A counterfactual asks:

    **What would need to change for the model to produce a different
    prediction?**
    """
)

col1, col2, col3 = st.columns(3)

col1.metric(
    "Original Recency",
    "31 days"
)

col2.metric(
    "Original Probability",
    "80%"
)

col3.metric(
    "Approximate Decision Boundary",
    "274 days"
)

st.write(
    """
    In the validation counterfactual analysis, increasing
    **Recency_Days** from approximately 31 days toward 274 days,
    while holding the other tested customer characteristics fixed,
    moved the predicted probability toward approximately 50%.

    This demonstrates the model's sensitivity to customer inactivity.
    """
)

st.warning(
    "This is a model counterfactual, not a causal claim. It does not "
    "prove that changing recency alone will cause a customer to purchase."
)


# ---------------------------------------------------------
# Fairness
# ---------------------------------------------------------

st.header("6. Fairness and Explanation Context")

fairness = pd.DataFrame({
    "Metric": [
        "Demographic Parity Difference",
        "Disparate Impact Ratio",
        "Equal Opportunity Difference",
        "Equalized Odds Difference"
    ],
    "Baseline Result": [
        0.1094,
        0.7883,
        0.1203,
        0.1203
    ]
})

st.dataframe(
    fairness,
    use_container_width=True,
    hide_index=True
)

col1, col2 = st.columns(2)

col1.metric(
    "UK Test Customers",
    "967"
)

col2.metric(
    "Non-UK Test Customers",
    "89"
)

st.warning(
    "The geographic fairness analysis is exploratory because the "
    "Non-UK test sample contains only 89 customers. Country grouping "
    "should not be interpreted as a substitute for demographic "
    "protected characteristics."
)


# ---------------------------------------------------------
# Interpretation limitations
# ---------------------------------------------------------

st.header("7. Explainability Limitations")

st.write(
    """
    **Correlated features:** Customer-value variables can be related
    to one another. For example, Monetary, Frequency and
    Avg_Order_Value contain overlapping information. This can affect
    how model importance is distributed between features.

    **Association versus causation:** SHAP explains how the trained
    model uses information; it does not demonstrate that a feature
    causes repeat purchasing.

    **Local versus global explanations:** A feature that is important
    across the full customer population may not be the dominant factor
    for every individual customer.

    **Model dependence:** Explanations describe this specific trained
    Random Forest model and may change following model retraining.
    """
)


# ---------------------------------------------------------
# Explanation governance
# ---------------------------------------------------------

st.header("8. Explanation Governance")

st.write(
    """
    Explainability evidence should be retained with the relevant
    model version so that important predictions can be investigated
    later.

    The BrightCart governance approach therefore links explanation
    outputs with model versioning, validation evidence, fairness
    assessments and monitoring records.

    Explanations support human review; they do not replace it.
    """
)


# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------

st.divider()

st.caption(
    "BrightCart Repeat Purchase Prediction | "
    "Explainable AI and Responsible Model Interpretation"
)
