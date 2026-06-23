import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Enterprise Sales Engine", page_icon="🛍️", layout="wide")

st.title("Enterprise Sales Performance Dashboard 🛍️")
st.write("Renders high-frequency product sales data using Streamlit's high-performance native charting blocks.")

st.write("---")

# 1. GENERATE MOCK SALES TIMELINE DATASET
np.random.seed(42)
date_range = pd.date_range(start="2026-01-01", periods=30, freq="D")
sales_matrix = pd.DataFrame({
    "Date": date_range,
    "Hardware Division": np.random.randint(20000, 50000, size=30),
    "SaaS Subscriptions": np.random.randint(35000, 70000, size=30),
    "Professional Services": np.random.randint(10000, 25000, size=30)
}).set_index("Date")

# 2. TELEMETRY KPIS MATRIX GRID
st.subheader("Gross Financial Revenue Streams")
col1, col2, col3 = st.columns(3)
col1.metric(label="Total Hardware Inflow", value=f"${sales_matrix['Hardware Division'].sum():,}")
col2.metric(label="Total Recurring SaaS ARR", value=f"${sales_matrix['SaaS Subscriptions'].sum():,}", delta="+14.2%")
col3.metric(label="Consulting Services Yield", value=f"${sales_matrix['Professional Services'].sum():,}")

st.write("---")

# 3. LAYOUT GRID FOR NATIVE CHARTS
left_chart_lane, right_chart_lane = st.columns(2)

with left_chart_lane:
    st.header("Cumulative Division Trends")
    st.caption("Area distribution matrix highlighting macro revenue generation over 30 days:")
    # Native Area Chart
    st.area_chart(sales_matrix)

with right_chart_lane:
    st.header("Daily Component Comparisons")
    st.caption("Bar chart tracking segment performance side-by-side per timeline unit:")
    # Native Bar Chart
    st.bar_chart(sales_matrix)