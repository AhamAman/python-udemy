import streamlit as st
import pandas as pd

st.set_page_config(page_title="Excel Processing Matrix", page_icon="🛠️", layout="centered")

st.title("Excel Stream Processing Matrix 🛠️")
st.write("This engine reads Excel spreadsheets, drops missing entries, and transforms them into CSV downloads.")

st.write("---")

# 1. Ingest Excel Binary Stream
uploaded_excel = st.file_uploader("Upload target Excel worksheet:", type=["xlsx"])

if uploaded_excel is not None:
    st.success("Excel binary buffer stream mounted.")
    
    # Parse the Excel workbook file stream
    df_excel = pd.read_excel(uploaded_excel)
    
    st.subheader("Original Sheet Sample View")
    st.dataframe(df_excel.head(5), use_container_width=True)
    
    # 2. Execution Processing Phase
    st.write("---")
    st.subheader("Data Cleansing Controls")
    
    if st.button("Execute Structural Missing-Value Cleanse"):
        # Drop rows where critical cells are empty
        cleaned_df = df_excel.dropna()
        rows_removed = len(df_excel) - len(cleaned_df)
        
        st.info(f"Cleanse complete. Permanently dropped {rows_removed} unpopulated tracking rows.")
        st.dataframe(cleaned_df.head(5), use_container_width=True)
        
        # 3. Export Transformation to Download Stream
        # Convert the cleaned DataFrame into a standard text string block buffer
        csv_download_payload = cleaned_df.to_csv(index=False).encode('utf-8')
        
        st.write("---")
        st.subheader("Export Pipeline")
        
        # Deploy the explicit download button widget
        st.download_button(
            label="📥 Download Cleaned Dataset as CSV",
            data=csv_download_payload,
            file_name=f"processed_{uploaded_excel.name.split('.')[0]}.csv",
            mime="text/csv",
            help="Click here to download your clean dataset file straight to your machine."
        )
        
else:
    st.warning("Please upload an Excel workbook sheet (`.xlsx`) to spin up the transformation loop.")