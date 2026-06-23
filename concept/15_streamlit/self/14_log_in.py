import streamlit as st

st.set_page_config(page_title="Identity Access: Gateway", page_icon="🔑", layout="centered")

# 1. INITIALIZE DATABASE SEED AND TRACKING STATUS STATE
if "user_registry_db" not in st.session_state:
    st.session_state["user_registry_db"] = {"admin": "matrix_core_2026", "alex": "concurrency_99"}

if "is_logged_in" not in st.session_state:
    st.session_state["is_logged_in"] = False

if "current_user" not in st.session_state:
    st.session_state["current_user"] = None


# =====================================================================
# CONDITIONAL VIEW LAYER CONTROLLER
# =====================================================================

# PATH A: USER IS AUTHENTICATED -> Render the Protected Dashboard Space
if st.session_state["is_logged_in"]:
    st.title(f"Secure Operational Portal Matrix 🖥️")
    st.success(f"Access Clear: Verified session key active for **{st.session_state['current_user']}**")
    
    st.write("---")
    st.header("Protected Enterprise Cluster Metrics")
    st.info("System Engine Status: Active | Port 8501 Multiplexer functional.")
    st.metric(label="Secure Vault Memory Ingest", value="89.4 TB/s", delta="+12.5%")
    
    st.write("---")
    if st.button("🔴 Terminate Session & Log Out", type="secondary"):
        st.session_state["is_logged_in"] = False
        st.session_state["current_user"] = None
        st.rerun() # Forces instant interface re-draw back to the login wall

# PATH B: USER IS ANONYMOUS -> Enforce the Security Login Wall Layout
else:
    st.title("Secure Infrastructure Gateway 🔑")
    st.write("Provide your credentials to establish a verified session lease window.")
    
    st.write("---")
    
    with st.form(key="login_gateway_matrix", clear_on_submit=False):
        st.subheader("Identity Verification Check")
        
        input_user = st.text_input(label="Username Handle", placeholder="e.g., admin").strip()
        input_pass = st.text_input(label="Security Password Access Token", type="password", placeholder="••••••••")
        
        login_submit = st.form_submit_button(label="Authorize Connection Session")

    if login_submit:
        # Fetch the baseline dictionary references from our persistent session database
        db_ref = st.session_state["user_registry_db"]
        
        # Validate entry against stored record dictionary matching keys
        if input_user in db_ref and db_ref[input_user] == input_pass:
            # Shift the logical tracking state flags permanently
            st.session_state["is_logged_in"] = True
            st.session_state["current_user"] = input_user
            st.toast("Authorization token matching confirmed!", icon="🔓")
            st.rerun() # Force an immediate top-to-bottom re-run to transition to PATH A
        else:
            st.error("Authorization Denied: Invalid handle or matching cryptographic payload.")