import streamlit as st

st.set_page_config(page_title="Metrics Engine: BMI", page_icon="⚖️", layout="centered")

st.title("Body Mass Index (BMI) Calculator ⚖️")
st.write("Input your physical telemetry metrics below to calculate your BMI index classification.")

st.write("---")

# 1. Create columns for side-by-side numerical inputs
col1, col2 = st.columns(2)

with col1:
    # weight input in kilograms
    weight = st.number_input(
        label="Weight (kg)", 
        min_value=10.0, 
        max_value=300.0, 
        value=70.0, 
        step=0.5,
        help="Enter your total body mass in kilograms."
    )

with col2:
    # height input in centimeters (converted to meters in code)
    height_cm = st.number_input(
        label="Height (cm)", 
        min_value=50.0, 
        max_value=250.0, 
        value=175.0, 
        step=1.0,
        help="Enter your standing height in centimeters."
    )

# 2. Math Execution Phase (Runs instantly every time a value changes)
height_m = height_cm / 100
bmi = weight / (height_m ** 2)

st.write("---")
st.subheader("Analysis Metrics")

# Render the calculated KPI
st.metric(label="Your Calculated BMI Index", value=f"{bmi:.1f}")

# 3. Conditional Status Classifications
if bmi < 18.5:
    st.warning("Classification: Underweight 🟡")
    st.write("Consider consulting a health professional regarding nutritional strategies.")
elif 18.5 <= bmi < 25.0:
    st.success("Classification: Normal / Healthy Weight ✅")
    st.write("Great job! Your physical metrics match standard healthy distribution boundaries.")
elif 25.0 <= bmi < 30.0:
    st.warning("Classification: Overweight 🟠")
    st.write("Consider increasing cardiovascular pacing or tracking daily caloric ingestion profiles.")
else:
    st.error("Classification: Obesity 🔴")
    st.write("Health risks are significantly elevated. Consulting a clinical specialist is highly advised.")