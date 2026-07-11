import streamlit as st
import pandas as pd
import joblib

# Load trained pipeline
model = joblib.load("fraud_detection_pipeline.pkl")
import streamlit as st
import pandas as pd
import joblib

model = joblib.load("fraud_detection_pipeline.pkl")


st.title("💳 Fraud Detection Web App")
st.markdown("Enter transaction details and click **Predict**")
st.divider()

# ---- User Inputs ----
step = st.number_input("Step (Time Index)", min_value=0, value=0)

age = st.selectbox("Age Group", ["1", "2", "3", "4", "5"])

gender = st.selectbox("Gender", ["M", "F"])

category = st.selectbox(
    "Transaction Category",
    [
        "es_transportation",
        "es_food",
        "es_health",
        "es_travel",
        "es_shopping"
    ]
)

amount = st.number_input("Transaction Amount", min_value=0.0, value=50.0)

# ---- Prediction ----
if st.button("Predict"):

    input_data = pd.DataFrame([{
        "step": step,
        "age": age,
        "gender": gender,
        "category": category,
        "amount": amount
    }])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("🚨 Fraudulent Transaction Detected")
    else:
        st.success("✅ Transaction is NOT Fraud")

