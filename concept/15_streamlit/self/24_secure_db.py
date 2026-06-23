import streamlit as st
import pandas as pd
import numpy as np

# Set up page configurations
st.set_page_config(page_title="Enterprise Vault Access", page_icon="🔒", layout="wide")

# =====================================================================
# 1. INITIALIZATION & SESSION MANAGEMENT TIER
# =====================================================================
# Seed an in-memory user registry database matrix
USER_DATABASE = {
    "root_operator": "concurrency_2026",
    "alex_mercer": "first_principles_99"
}

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if "session_user" not in st.session_state:
    st.session_state["session_user"] = None


# =====================================================================
# 2. INTERFACE COMPONENT: REGISTRATION & LOGIN WALL
# =====================================================================
def render_security_login_wall():
    """Enforces a strict visual and logical gateway boundary."""
    st.title("Secure Infrastructure Gateway 🔒")
    st.write("Provide valid cluster tokens to establish an authenticated session context lease.")
    
    st.write("---")
    
    # Center the login panel using columns layout
    _, center_col, _ = st.columns([1, 2, 1])
    
    with center_col:
        with st.form(key="identity_verification_matrix", clear_on_submit=False):
            st.subheader("Identity Verification Check")
            
            username_input = st.text_input(label="Username Handle:", placeholder="e.g., alex_mercer").strip()
            password_input = st.text_input(label="Access Token Signature:", type="password", placeholder="••••••••")
            
            submit_auth = st.form_submit_button(label="Authorize Session Link", use_container_width=True)
            
        if submit_auth:
            # Check input strings against our secure registry dict keys
            if username_input in USER_DATABASE and USER_DATABASE[username_input] == password_input:
                # Mutate state variables permanently
                st.session_state["authenticated"] = True
                st.session_state["session_user"] = username_input
                st.toast("Cryptographic signature match confirmed! Unlocking panel...", icon="🔓")
                st.rerun() # Immediately re-run from line 1 to bypass the login wall
            else:
                st.error("Access Denied: Invalid handle or token signature payload mapping.")


# =====================================================================
# 3. ENFORCE ACCESS CONTROL GATE
# =====================================================================
if not st.session_state["authenticated"]:
    render_security_login_wall()
    st.stop() # CRITICAL SECURITY GUARDRAIL: Halts execution completely for unauthenticated sessions


# =====================================================================
# 4. PROTECTED APP REGION (Only reached if authenticated is True)
# =====================================================================
# Persistent Header Sidebar Panel with Logout Command Anchor
with st.sidebar:
    st.title("⚙️ Session Portal")
    st.write(f"Active Operator: **{st.session_state['session_user']}**")
    st.caption("Status: Encrypted Tunnel Lease Active")
    
    st.write("---")
    # Destructive session drop routine
    if st.button("🔴 Terminate Session & Log Out", use_container_width=True):
        st.session_state["authenticated"] = False
        st.session_state["session_user"] = None
        st.toast("Session dropped cleanly.", icon="🔒")
        st.rerun() # Instantly forces top-to-bottom re-run back to the login wall

# Main Vault Protected Analytics Canvas Canvas
st.title("Protected Core Infrastructure Dashboard 🖥️")
st.success(f"Security Clearance Verified. Node connection matrix open for user: {st.session_state['session_user']}.")

st.write("---")

# Render high-value metric charts and data frames safely
st.subheader("Live Cluster Memory Telemetry")
m1, m2, m3 = st.columns(3)
m1.metric(label="Secure Vault Memory Ingest", value="89.4 TB/s", delta="+12.5%")
m2.metric(label="Active Encryption Pipelines", value="1,024 Nodes", delta="Stable")
m3.metric(label="Network Packet Drop Rate", value="0.0000%", delta="-0.001%")

st.write("---")

left_pane, right_pane = st.columns([2, 1])

with left_pane:
    st.subheader("Historical Load Variance Trend Matrix")
    chart_data = pd.DataFrame(np.random.randn(30, 2), columns=["Core-Alpha Ingest", "Core-Beta Ingest"])
    st.line_chart(chart_data)
    
with right_pane:
    st.subheader("System Access Log Footprint")
    st.markdown("""
    * **Authorization Protocol:** Secure Stateful Token
    * **Host Multiplexer:** Port 8501 Engine
    * **Data Core Integrity:** Relational Matrix Check Clear
    * **OS Environment Profile:** Linux Secure Container
    """)