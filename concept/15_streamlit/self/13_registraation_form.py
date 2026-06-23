import streamlit as st

st.set_page_config(page_title="Identity Access: Register", page_icon="🔐", layout="centered")

st.title("User Authentication Registry 🔐")
st.write("Create a secure profile credential mapping below to append your token to the state ledger.")

# 1. INITIALIZE GLOBAL REUSABLE USER DATABASE IN SESSION STATE
if "user_registry_db" not in st.session_state:
    # Key = Username string, Value = Password string
    st.session_state["user_registry_db"] = {
        "admin": "matrix_core_2026" # Seed with a default root account
    }

st.write("---")

# 2. ENCAPSULATE DATA INTAKE INSIDE AN ATOMIC FORM BLOCK
with st.form(key="account_creation_matrix", clear_on_submit=True):
    st.subheader("Account Credential Profile")
    
    new_username = st.text_input(label="Desired Username Handle", placeholder="e.g., amercer").strip()
    
    # type="password" automatically cloaks character entries on the fly
    new_password = st.text_input(label="Secure Password Entrance", type="password", placeholder="••••••••")
    confirm_password = st.text_input(label="Confirm Password Matching Flag", type="password", placeholder="••••••••")
    
    register_submit = st.form_submit_button(label="Commit Credentials to Registry")

# 3. INTERCEPTION AND VALIDATION PHASE
if register_submit:
    if not new_username or not new_password:
        st.error("Registration Denied: Username and Password fields are non-negotiable data tracks.")
    elif new_password != confirm_password:
        st.error("Registration Denied: Cryptographic entry mismatch. Password matrices do not match.")
    elif new_username in st.session_state["user_registry_db"]:
        st.warning(f"Registration Denied: Handle '{new_username}' already exists inside memory allocation.")
    else:
        # Commit the validated record to our global user ledger state dictionary
        st.session_state["user_registry_db"][new_username] = new_password
        st.success(f"🎉 Success! Profile '{new_username}' is permanently mapped to the runtime registry.")

st.write("---")
# Hidden developer inspection pane to track state persistence
with st.expander("👁️ System Operator View: Inspect Memory Database"):
    st.json(st.session_state["user_registry_db"])