import streamlit as st
import joblib
import numpy as np

# ---- Load the trained model ----
model = joblib.load("aqi_model.pkl")

# ---- Page setup ----
st.set_page_config(page_title="AQI Predictor", page_icon="🌡️")
st.title("🌡️ AQI Predictor")
st.write(
    "This app predicts the **Air Quality Index (AQI)** from temperature "
    "using a simple linear regression model trained from scratch."
)

# ---- User input ----
temp = st.slider("Select Temperature (°C)", min_value=0, max_value=50, value=25)

# ---- Prediction ----
predicted_aqi = model.predict([[temp]])[0]

st.subheader(f"Predicted AQI: {predicted_aqi:.2f}")

# ---- Simple AQI category label ----
if predicted_aqi <= 50:
    category, color = "Good", "green"
elif predicted_aqi <= 100:
    category, color = "Moderate", "orange"
elif predicted_aqi <= 150:
    category, color = "Unhealthy for Sensitive Groups", "orangered"
elif predicted_aqi <= 200:
    category, color = "Unhealthy", "red"
else:
    category, color = "Very Unhealthy", "darkred"

st.markdown(f"**Air Quality Category:** :{color}[{category}]")

st.divider()

# ---- Model info ----
with st.expander("ℹ️ About this model"):
    st.write(f"**Coefficient (slope):** {model.coef_[0]:.5f}")
    st.write(f"**Intercept:** {model.intercept_:.5f}")
    st.write(
        "This is a simple linear regression model using a single feature "
        "(temperature). It does not account for other factors affecting AQI "
        "such as humidity, wind speed, or pollution sources, so predictions "
        "are approximate."
    )

st.caption("Built with scikit-learn & Streamlit • First ML project 🚀")
