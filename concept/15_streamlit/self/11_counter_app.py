import streamlit as st

st.set_page_config(page_title="State Workspace: Counter", page_icon="🔢", layout="centered")

st.title("Stateful Incremental Counter 🔢")
st.write("Demonstrates how variables survive top-to-bottom execution scripts using Session State.")

st.write("---")

# 1. INITIALIZATION: Verify state memory exists before building widgets
if "click_counter" not in st.session_state:
    st.session_state["click_counter"] = 0
    st.caption("✨ Counter memory workspace initialized on the heap.")

# 2. INTERACTION PHASE: Button anchors trigger state additions
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("➕ Increment (+1)", use_container_width=True):
        st.session_state["click_counter"] += 1

with col2:
    if st.button("➖ Decrement (-1)", use_container_width=True):
        st.session_state["click_counter"] -= 1

with col3:
    if st.button("🔄 Reset Memory", use_container_width=True):
        st.session_state["click_counter"] = 0

# 3. DISPLAY VALUE
st.write("---")
st.metric(label="Persistent Counter State Value", value=st.session_state["click_counter"])