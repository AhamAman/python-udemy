import streamlit as st
import pandas as pd

st.set_page_config(page_title="User Intake Survey", page_icon="📝", layout="centered")

st.title("Developer Ecosystem Survey 📝")
st.write("Please fill out this form to record your architectural footprint inside the ecosystem log.")

# 1. Establish the Form Container Block
with st.form(key="developer_survey_form", clear_on_submit=False):
    st.subheader("Demographic & Technical Profile")
    
    # Text input vector
    dev_name = st.text_input(label="Full Name / Handle", placeholder="e.g., Alex Mercer")
    
    # Numerical boundary slider
    years_exp = st.slider(label="Years of Core Software Experience", min_value=0, max_value=30, value=2)
    
    # Single selection dropdown matrix
    primary_role = st.selectbox(
        label="What is your primary architectural focus?",
        options=["Backend Systems", "Frontend Interface", "Data Infrastructure", "Machine Learning Eng", "DevOps / SRE"]
    )
    
    # Multi-selection tagging grid
    mastered_tools = st.multiselect(
        label="Select frameworks you have actively deployed to production:",
        options=["FastAPI", "Streamlit", "Asyncio Stack", "Django / Flask", "Next.js / React", "Docker Containers"]
    )
    
    # Form submission anchor button
    submit_button = st.form_submit_button(label="Commit Record to Log")

# 2. Form Submission Interception Phase
st.write("---")
if submit_button:
    if not dev_name:
        st.error("Submission Denied: Name field cannot be left blank.")
    elif not mastered_tools:
        st.warning("Submission Denied: Please select at least one technology framework.")
    else:
        st.success("🎉 Transaction Complete! Survey profile successfully logged to system state.")
        
        # 3. Structure data into a clean, scannable data summary view
        st.subheader("Your Compiled System Profile")
        
        profile_summary = {
            "Parameter Field": ["Operator Name", "Experience Metrics", "Core Core Architecture", "Assigned Toolsets"],
            "User Values": [dev_name, f"{years_exp} Years", primary_role, ", ".join(mastered_tools)]
        }
        
        summary_df = pd.DataFrame(profile_summary)
        st.table(summary_df)