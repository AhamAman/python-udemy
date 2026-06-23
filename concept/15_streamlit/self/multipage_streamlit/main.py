import streamlit as st

# 1. GLOBAL LIFECYCLE MANAGEMENT SETTINGS
st.set_page_config(page_title="Core Platform Engine", page_icon="🏢", layout="wide")

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
if "user_role" not in st.session_state:
    st.session_state["user_role"] = "GUEST"

# 2. DEFINING PAGE ROUTE DESCRIPTORS
login_gate = st.Page("views/login.py", title="Security Gateway", icon="🔒")
analytics_suite = st.Page("views/analytics.py", title="Performance Analytics Suite", icon="📈")
admin_dashboard = st.Page("views/admin.py", title="System Administration Control", icon="⚙️")

# 3. DYNAMIC CONDITIONAL ROUTING AND ACCESS CONTROL GATES
# Grouping layouts dynamically using a dictionary map
if not st.session_state["authenticated"]:
    # Hard Isolation: If anonymous, lock navigation tree strictly to the login panel
    routing_matrix = [login_gate]
else:
    # Role-Based Access Control (RBAC) filtering layout boundaries
    if st.session_state["user_role"] == "ADMIN":
        routing_matrix = {
            "Analytics Portal": [analytics_suite],
            "Root Management": [admin_dashboard]
        }
    else:
        # Standard users cannot see or navigate to the Admin page
        routing_matrix = {
            "Analytics Portal": [analytics_suite]
        }

# 4. INSTANTIATE THE NAVIGATION ROUTER ENGINE
selected_page = st.navigation(routing_matrix)

# Sidebar Shared Logout Button Component
if st.session_state["authenticated"]:
    with st.sidebar:
        st.write("---")
        if st.button("🔴 Terminate Session Link", use_container_width=True):
            st.session_state["authenticated"] = False
            st.session_state["user_role"] = "GUEST"
            st.toast("Session dropped.")
            st.rerun()

# Execute the isolated page view file target code
selected_page.run()