import streamlit as st
import pandas as pd

st.set_page_config(page_title="CSV Stream Profiler", page_icon="📝", layout="wide")

st.title("CSV Data Stream Profiler 📝")
st.write("Upload a target CSV spreadsheet file to load its memory data frame.")

# 1. Instantiate the File Uploader Widget
uploaded_csv = st.file_uploader(
    label="Choose a CSV file to profile", 
    type=["csv"], 
    help="Accepts standard comma-separated text files."
)

if uploaded_csv is not None:
    st.success(f"File matrix locked: {uploaded_csv.name} ({uploaded_csv.size / 1024:.2f} KB)")
    
    # Read the data straight out of the uploaded memory buffer stream
    df = pd.read_csv(uploaded_csv)
    
    # 2. Display Telemetry Layout Metrics
    st.write("---")
    st.subheader("Data Dimensionality Summary")
    
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Total Rows Captured", value=df.shape[0])
    col2.metric(label="Total Columns Detected", value=df.shape[1])
    col3.metric(label="Total Null Cells", value=int(df.isna().sum().sum()))
    
    # 3. Interactive Filtering Pane
    st.write("---")
    st.header("Interactive Data Inspection Grid")
    
    # Allow user to preview a subset of the file dynamically
    row_preview_limit = st.slider("Select maximum rows to preview:", min_value=5, max_value=len(df), value=10)
    
    st.dataframe(df.head(row_preview_limit), use_container_width=True)
    
else:
    st.info("Awaiting file upload. Please drop a valid CSV dataset to begin parsing.")