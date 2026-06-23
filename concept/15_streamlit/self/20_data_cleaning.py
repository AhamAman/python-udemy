import streamlit as st
import pandas as pd
import io

st.set_page_config(page_title="Data Cleansing Studio", page_icon="🛠️", layout="centered")

st.title("Automated Data Cleansing Studio 🛠️")
st.write("Scan operational files for missing records, drop duplicates, and export a sanitized asset.")

st.write("---")

# 1. INITIALIZE DATA STREAM CONTAINERS
if "cleansed_df" not in st.session_state:
    st.session_state["cleansed_df"] = None

# Mock un-sanitized dataset with structural missing rows and duplicate values
dirty_data = """
User_ID,Handle,Region,Access_Score
U101,amercer,North,85
U102,bsmith,,92
U101,amercer,North,85
U103,jdoe,South,
U104,rwhitt,West,78
U104,rwhitt,West,78
"""

uploaded_dirty_file = st.file_uploader("Upload un-cleansed CSV data tracking asset:", type=["csv"])

# Read input into baseline variables
raw_df = None
if uploaded_dirty_file is not None:
    raw_df = pd.read_csv(uploaded_dirty_file)
elif st.checkbox("Mount Dirty Mock Dataset Example", value=True):
    raw_df = pd.read_csv(io.StringIO(dirty_data.strip()))

# 2. ARCHITECTURAL ANALYSIS MATRIX
if raw_df is not None:
    # Cache the original state inside session state if no action has been taken yet
    if st.session_state["cleansed_df"] is None:
        st.session_state["cleansed_df"] = raw_df.copy()

    st.subheader("Raw Data Diagnostic Profile")
    
    # Calculate anomaly counts using Pandas lookups
    total_duplicates = int(st.session_state["cleansed_df"].duplicated().sum())
    total_nulls = int(st.session_state["cleansed_df"].isna().sum().sum())

    col1, col2 = st.columns(2)
    col1.metric(label="Duplicate Rows Found", value=total_duplicates, delta="Action Advised" if total_duplicates > 0 else 0, delta_color="inverse")
    col2.metric(label="Null/Empty Cells Found", value=total_nulls, delta="Action Advised" if total_nulls > 0 else 0, delta_color="inverse")

    st.write("---")
    st.subheader("Active Data Frame Workspace")
    st.dataframe(st.session_state["cleansed_df"], use_container_width=True)

    # 3. DISPATCH ACTION CONTROL GATES
    st.write("---")
    st.subheader("Transformation Engineering Panel")
    
    ctrl_col1, ctrl_col2, ctrl_col3 = st.columns(3)

    with ctrl_col1:
        if st.button("🗑️ Drop Duplicate Records", use_container_width=True):
            st.session_state["cleansed_df"] = st.session_state["cleansed_df"].drop_duplicates()
            st.toast("Duplicate matrix clusters removed.", icon="🧼")
            st.rerun()

    with ctrl_col2:
        if st.button("🧼 Purge Null/Empty Rows", use_container_width=True):
            st.session_state["cleansed_df"] = st.session_state["cleansed_df"].dropna()
            st.toast("Unpopulated missing value rows dropped.", icon="🧼")
            st.rerun()

    with ctrl_col3:
        if st.button("🔄 Reset to Original State", type="secondary", use_container_width=True):
            st.session_state["cleansed_df"] = raw_df.copy()
            st.toast("Memory ledger reset to original parameters.", icon="🔄")
            st.rerun()

    # 4. EXPORT AND EXTRUSION PHASE
    st.write("---")
    st.subheader("Export Sanitized Data Pipe")
    
    # Transform active state dataframe back into a text download byte buffer block
    csv_download_stream = st.session_state["cleansed_df"].to_csv(index=False).encode('utf-8')
    
    st.download_button(
        label="📥 Download Cleaned CSV File Asset",
        data=csv_download_stream,
        file_name="sanitized_dataset_report.csv",
        mime="text/csv",
        use_container_width=True,
        help="Click here to flush the cleaned memory data frame straight to an explicit disk file copy."
    )