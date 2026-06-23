import streamlit as st

st.title("Enterprise Identity Access Gate 🔒")
st.write("Provide structural tokens to unlock specific navigation sectors.")

st.write("---")
_, center_pane, _ = st.columns([1, 2, 1])

with center_pane:
    with st.form(key="identity_form", clear_on_submit=False):
        username = st.text_input("Username Handle:", placeholder="admin OR user").strip()
        password = st.text_input("Access Token Signature:", type="password", placeholder="••••••••")
        submit_auth = st.form_submit_button("Authorize Session Link", use_container_width=True)
        
    if submit_auth:
        if username == "admin" and password == "matrix_2026":
            st.session_state["authenticated"] = True
            st.session_state["user_role"] = "ADMIN"
            st.success("Admin access cleared! Redirecting...")
            st.rerun()
        elif username == "user" and password == "concurrency_99":
            st.session_state["authenticated"] = True
            st.session_state["user_role"] = "OPERATOR"
            st.success("Standard operator cleared! Redirecting...")
            st.rerun()
        else:
            st.error("Authentication Failed: Cryptographic signature payload mismatch.")