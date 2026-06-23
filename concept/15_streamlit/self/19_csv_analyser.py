import streamlit as st
import pandas as pd
import io

st.set_page_config(page_title="CSV Analyzer Matrix", page_icon="📊", layout="wide")

st.title("Enterprise CSV Analyzer & Analytics Dashboard 📊")
st.write("Upload a business dataset to calculate aggregations and render dynamic metrics.")

# 1. INITIALIZE DEMO SCRIPT FILE STREAM DATA
demo_csv = """
Order_ID,Segment,Product_Category,Revenue_USD,Units_Sold
ORD-1001,Enterprise,Cloud Infrastructure,4500.00,3
ORD-1002,Mid-Market,Hardware Terminals,1250.00,10
ORD-1003,Enterprise,SaaS Subscriptions,8900.00,12
ORD-1004,SMB,Hardware Terminals,350.00,2
ORD-1005,Mid-Market,Cloud Infrastructure,2100.00,2
ORD-1006,SMB,SaaS Subscriptions,1200.00,4
ORD-1007,Enterprise,Consulting Services,6000.00,1
"""

# 2. FILE INGESTION INTERFACE
with st.sidebar:
    st.header("Data Ingestion Control")
    uploaded_file = st.file_uploader("Upload business CSV dataset:", type=["csv"])
    
    st.write("---")
    use_demo = st.checkbox("Load Demo Transaction Dataset", value=True if not uploaded_file else False)

# Resolve file stream input mapping
df = None
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
elif use_demo:
    df = pd.read_csv(io.StringIO(demo_csv.strip()))

# 3. DATA PROCESSING AND INTERACTIVE FILTERING TIER
if df is not None:
    # Build filter boundaries based on the actual unique values found in the data columns
    available_categories = df["Product_Category"].unique().tolist()
    available_segments = df["Segment"].unique().tolist()
    
    with st.sidebar:
        st.write("---")
        st.header("Live Workspace Filters")
        
        # User-driven multi-selection arrays
        selected_categories = st.multiselect("Filter by Product Category:", options=available_categories, default=available_categories)
        selected_segments = st.multiselect("Filter by Customer Segment:", options=available_segments, default=available_segments)

    # Apply data masks based on interactive inputs
    filtered_df = df[
        (df["Product_Category"].isin(selected_categories)) & 
        (df["Segment"].isin(selected_segments))
    ]

    # 4. AGGREGATION & METRICS DISPLAY
    st.header("Operational Performance Telemetry")
    
    # Calculate summary aggregations on the filtered dataframe
    total_revenue = filtered_df["Revenue_USD"].sum()
    total_units = filtered_df["Units_Sold"].sum()
    avg_order_value = filtered_df["Revenue_USD"].mean() if len(filtered_df) > 0 else 0.0

    m1, m2, m3 = st.columns(3)
    m1.metric(label="Aggregated Revenue", value=f"${total_revenue:,.2f}")
    m2.metric(label="Total Units Transmitted", value=f"{total_units:,}")
    m3.metric(label="Average Transaction Value", value=f"${avg_order_value:,.2f}")

    st.write("---")

    # 5. CHARTS & DATA SUMMARY PANELS
    chart_lane, data_lane = st.columns([3, 2])

    with chart_lane:
        st.subheader("Revenue Allocation Matrix by Category")
        if not filtered_df.empty:
            # Perform a GroupBy aggregation for visual charting
            category_group = filtered_df.groupby("Product_Category")["Revenue_USD"].sum()
            st.bar_chart(category_group)
        else:
            st.warning("No data matches current filter boundaries.")

    with data_lane:
        st.subheader("Filtered Workspace Ledger")
        st.dataframe(filtered_df, use_container_width=True, hide_index=True)

else:
    st.info("Please mount an operational dataset via the sidebar uploader to spin up the analytics pipeline.")