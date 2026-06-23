import streamlit as st
import pandas as pd
import io

st.set_page_config(page_title="CSV Metrics Dashboard", page_icon="📊", layout="wide")

st.title("System Inventory Matrix 📊")
st.write("This application reads data sources and renders them inside an interactive, high-performance UI grid.")

# 1. Simulate a CSV file stream buffer (Replace this with pd.read_csv('file.csv') in production)
csv_data = """
Product_ID,Product_Name,Category,Price_USD,Stock_Count
ORD-1001,Quantum Laptop Engine,Hardware,1499.00,10
ORD-1002,Mechanical Macro Keyboard,Peripherals,125.00,50
ORD-1003,OLED Spatial Monitor,Hardware,899.00,15
ORD-1004,Titanium Ergo Desk,Furniture,650.00,5
ORD-1005,USB-C Hub Array,Peripherals,45.00,120
"""

# Read the data stream into a standard Pandas DataFrame
df = pd.read_csv(io.StringIO(csv_data.strip()))

# 2. Extract and display summary telemetry metrics using columns
st.subheader("System Telemetry Summary")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Total Unique SKUs", value=len(df))
with col2:
    st.metric(label="Total Inventory Value", value=f"${(df['Price_USD'] * df['Stock_Count']).sum():,.2f}")
with col3:
    st.metric(label="Highest Priced Item", value=f"${df['Price_USD'].max():,.2f}")

st.write("---")

# 3. Render the interactive dataframe view layout
st.header("Active Inventory Ledger")
st.write("Use the column headers to sort, search, or expand data rows dynamically:")

# st.dataframe provides full interactive controls (filtering, resizing, sorting)
st.dataframe(df, use_container_width=True)