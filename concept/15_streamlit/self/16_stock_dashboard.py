import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="Quant Ticker Matrix", page_icon="📈", layout="wide")

st.title("Quant Asset Stock Analytics Workspace 📈")
st.write("Toggle between static Matplotlib execution frames and rich, interactive Plotly visualization matrices.")

st.write("---")

# 1. TIME SERIES GENERATION (Simulated Stock Price Walk)
@st.cache_data # Keep generation fast across user clicks
def generate_stock_history():
    dates = pd.date_range(start="2026-01-01", periods=100, freq="D")
    # Simulate geometric brownian motion price drifts
    price_alpha = 150 + np.cumsum(np.random.randn(100) * 2.5)
    price_beta = 320 + np.cumsum(np.random.randn(100) * 4.0)
    
    df = pd.DataFrame({"Date": dates, "Asset-Alpha (Tech)": price_alpha, "Asset-Beta (Energy)": price_beta})
    return df

stock_df = generate_stock_history()

# 2. PERSISTENT SIDEBAR VIEW PORT SELECTION
with st.sidebar:
    st.header("Visualization Engine Profile")
    engine_choice = st.radio(
        label="Select Rendering Engine:",
        options=["Interactive Plotly Framework", "Static Matplotlib Framework"]
    )
    st.write("---")
    st.caption("Quant Stack Version 2.6 | Active Loop")

# 3. CONDITIONAL VISUALIZATION ROUTING ENGINE
if engine_choice == "Interactive Plotly Framework":
    st.header("Plotly Client-Side Interactive Workstation")
    st.write("Hover over traces to inspect metrics, double-click the legend to isolate curves, or click-and-drag to zoom:")
    
    # Transform data wide-to-long format for standard Plotly Express plotting
    melted_df = stock_df.melt(id_vars=["Date"], value_vars=["Asset-Alpha (Tech)", "Asset-Beta (Energy)"], 
                              var_name="Asset Ticker", value_name="Price_USD")
    
    # Construct the rich interactive figure
    plotly_fig = px.line(
        melted_df, 
        x="Date", 
        y="Price_USD", 
        color="Asset Ticker",
        title="Asset Trajectory Variance Matrix",
        template="plotly_dark"
    )
    
    # Render inside the Streamlit canvas
    st.plotly_chart(plotly_fig, use_container_width=True)

else:
    st.header("Matplotlib Static Server-Side Plot Profile")
    st.write("Renders solid mathematical print graphs directly out of the memory frame:")
    
    # Construct explicit Matplotlib Figure and Axes objects
    fig, ax = plt.subplots(figsize=(10, 4))
    
    ax.plot(stock_df["Date"], stock_df["Asset-Alpha (Tech)"], label="Asset-Alpha (Tech)", color="#1f77b4", linewidth=2)
    ax.plot(stock_df["Date"], stock_df["Asset-Beta (Energy)"], label="Asset-Beta (Energy)", color="#ff7f0e", linewidth=1.5, linestyle="--")
    
    # Style the plotting grids defensively
    ax.set_title("Historical Valuation Log Linear Bounds", fontsize=12, fontweight="bold")
    ax.set_xlabel("Timeline Units", fontsize=10)
    ax.set_ylabel("Valuation Index (USD)", fontsize=10)
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.legend(loc="upper left")
    fig.autofmt_xdate() # Auto-rotate dates nicely
    
    # Render the static figure block securely
    st.pyplot(fig)