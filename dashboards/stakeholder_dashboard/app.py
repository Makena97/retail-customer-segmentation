import streamlit as st
import pandas as pd


# ---------------------------------------------------------
# Page setup
# ---------------------------------------------------------

st.set_page_config(
    page_title="BrightCart Customer Insights",
    page_icon="🛒",
    layout="wide"
)


# ---------------------------------------------------------
# Header
# ---------------------------------------------------------

st.title("BrightCart Customer Intelligence Dashboard")

st.caption(
    "Supporting customer retention decisions with repeat-purchase analytics"
)

st.info(
    "The BrightCart model estimates whether an existing customer "
    "is likely to make another purchase within the next 90 days."
)


# ---------------------------------------------------------
# Executive summary
# ---------------------------------------------------------

st.header("Executive Summary")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Customers Modelled",
    "5,278"
)

col2.metric(
    "Model Accuracy",
    "73.3%"
)

col3.metric(
    "ROC-AUC",
    "0.799"
)

col4.metric(
    "Repeat Purchase Rate",
    "43.2%"
)

st.write(
    """
    The model performs materially better than the majority-class
    baseline and provides a useful ranking of customers by their
    likelihood of purchasing again.

    The strongest predictor is how recently a customer purchased,
    followed by monetary value, purchase frequency, product variety,
    and quantity purchased.
    """
)


# ---------------------------------------------------------
# Business problem
# ---------------------------------------------------------

st.header("1. Business Question")

st.write(
    """
    **Which existing customers are most likely to purchase again
    within 90 days?**

    BrightCart can use this information to support more focused
    retention activity instead of applying the same marketing
    strategy to every customer.
    """
)


# ---------------------------------------------------------
# Model performance
# ---------------------------------------------------------

st.header("2. How Well Does the Model Perform?")

performance = pd.DataFrame({
    "Measure": [
        "Majority Class Baseline",
        "Random Forest Accuracy",
        "Precision",
        "Recall",
        "F1 Score",
        "ROC-AUC"
    ],
    "Result": [
        "56.8%",
        "73.3%",
        "69.8%",
        "67.3%",
        "68.5%",
        "79.9%"
    ],
    "Business Meaning": [
        "Simple benchmark with no predictive intelligence",
        "Correct classification for approximately 73 in 100 customers",
        "About 70% of predicted repeat purchasers actually repeat",
        "Model identifies about 67% of actual repeat purchasers",
        "Balances precision and recall",
        "Good ability to rank repeat purchasers above non-repeat purchasers"
    ]
})

st.dataframe(
    performance,
    use_container_width=True,
    hide_index=True
)

st.success(
    "The Random Forest improves accuracy by approximately "
    "16.5 percentage points compared with the majority-class baseline."
)


# ---------------------------------------------------------
# Customer profiles
# ---------------------------------------------------------

st.header("3. Example Customer Profiles")

profiles = pd.DataFrame({
    "Customer Profile": [
        "Higher Probability",
        "Moderate Probability",
        "Lower Probability"
    ],
    "Recency (Days)": [
        16,
        308,
        323
    ],
    "Frequency": [
        9,
        5,
        1
    ],
    "Monetary Value": [
        2391.16,
        3334.82,
        877.70
    ],
    "Average Order Value": [
        265.68,
        666.96,
        877.70
    ],
    "Predicted Probability": [
        "80%",
        "50%",
        "20%"
    ],
    "Actual Outcome": [
        "Repeated",
        "Repeated",
        "Did not repeat"
    ]
})

st.dataframe(
    profiles,
    use_container_width=True,
    hide_index=True
)

st.write(
    """
    These examples illustrate why probability is more useful than
    a simple yes/no classification. BrightCart can distinguish
    higher-, moderate-, and lower-probability customers and tailor
    business actions accordingly.
    """
)


# ---------------------------------------------------------
# Segmentation strategy
# ---------------------------------------------------------

st.header("4. Recommended Retention Strategy")

strategy = pd.DataFrame({
    "Customer Group": [
        "Higher Probability",
        "Moderate Probability",
        "Lower Probability"
    ],
    "Suggested Action": [
        "Protect and grow the relationship",
        "Use targeted reminders or personalized offers",
        "Re-engage selectively and avoid excessive marketing spend"
    ],
    "Business Objective": [
        "Maintain loyalty and increase value",
        "Encourage the next purchase",
        "Recover valuable customers efficiently"
    ]
})

st.dataframe(
    strategy,
    use_container_width=True,
    hide_index=True
)


# ---------------------------------------------------------
# Feature importance
# ---------------------------------------------------------

st.header("5. What Drives Repeat Purchasing?")

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

st.write(
    """
    **Recency is the strongest signal.**

    Customers who purchased more recently generally have a higher
    predicted likelihood of returning. However, feature importance
    represents predictive association rather than proof of causation.
    """
)


# ---------------------------------------------------------
# Counterfactual
# ---------------------------------------------------------

st.header("6. What Could Change a Prediction?")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Example Starting Recency",
    "31 days"
)

col2.metric(
    "Starting Probability",
    "80%"
)

col3.metric(
    "Approximate Flip Point",
    "274 days"
)

st.write(
    """
    In one counterfactual example, a higher-probability customer's
    prediction moved toward the decision boundary as the number of
    days since their last purchase increased.

    This reinforces the business importance of maintaining customer
    engagement before long periods of inactivity develop.
    """
)


# ---------------------------------------------------------
# Fairness
# ---------------------------------------------------------

st.header("7. Responsible AI Check")

fairness = pd.DataFrame({
    "Measure": [
        "Demographic Parity Difference",
        "Disparate Impact Ratio",
        "Equal Opportunity Difference",
        "Equalized Odds Difference"
    ],
    "Baseline": [
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

st.warning(
    "Fairness results are exploratory. The validation sample contained "
    "967 UK customers and only 89 Non-UK customers. The small Non-UK "
    "sample limits the strength of conclusions that can be drawn."
)


# ---------------------------------------------------------
# Decision support
# ---------------------------------------------------------

st.header("8. How BrightCart Can Use the Model")

st.write(
    """
    The model should support—not replace—business judgement.

    BrightCart can use repeat-purchase probabilities to prioritize
    retention campaigns, compare customer groups, allocate marketing
    resources more efficiently, and identify customers who may require
    re-engagement.

    Predictions should not be treated as guarantees of customer
    behaviour.
    """
)


# ---------------------------------------------------------
# Key limitations
# ---------------------------------------------------------

st.header("9. Key Limitations")

st.write(
    """
    - Model accuracy is useful but not sufficient for error-free decisions.
    - The default operating threshold may need further business-cost analysis.
    - Geographic fairness results are exploratory because the Non-UK sample is small.
    - Correlated customer-value features may influence interpretation of SHAP importance.
    - Customer behaviour may change over time, requiring drift monitoring and periodic revalidation.
    """
)


# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------

st.divider()

st.caption(
    "BrightCart Repeat Purchase Prediction | "
    "Decision Support Dashboard"
)
