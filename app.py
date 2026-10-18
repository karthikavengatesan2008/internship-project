import streamlit as st
import pandas as pd
import numpy as np

st.title('⚙️ Predictive Maintenance of Gearbox')
st.write('This dashboard classifies the gearbox condition as **Healthy** or **Faulty** based on real-time vibration sensor data.')

st.sidebar.header('Sensor Inputs')
vibration_x = st.sidebar.slider('Vibration X-axis', 0.0, 20.0, 5.0)
vibration_y = st.sidebar.slider('Vibration Y-axis', 0.0, 20.0, 5.0)
vibration_z = st.sidebar.slider('Vibration Z-axis', 0.0, 20.0, 5.0)
temperature = st.sidebar.slider('Temperature (°C)', 20.0, 100.0, 60.0)

if st.button('Predict Gearbox Condition'):
    # Simple logic simulating model prediction for demonstration
    if vibration_x > 12 or temperature > 85:
        st.error("🚨 Prediction: **FAULTY** - High risk of failure detected. Maintenance required.")
    else:
        st.success("✅ Prediction: **HEALTHY** - Gearbox is operating under normal conditions.")
