import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="Database CRUD Matrix", page_icon="💾", layout="wide")

# =====================================================================
# PERSISTENT CONNECTION HANDLING LAYER
# =====================================================================
@st.cache_resource
def establish_secure_db_engine():
    """
    Initializes the database connection engine EXACTLY ONCE.
    Retains the connection reference pointer across all future script reruns.
    """
    # Connects to a local persistent SQLite file named 'cluster_inventory.db'
    conn = sqlite3.connect("cluster_inventory.db", check_same_thread=False)
    
    # Initialize the baseline structural schema tables
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS system_hardware (
            node_id INTEGER PRIMARY KEY AUTOINCREMENT,
            node_name TEXT NOT NULL,
            rack_location TEXT NOT NULL,
            core_count INTEGER NOT NULL,
            status_flag TEXT NOT NULL
        );
    """)
    conn.commit()
    return conn

# Mount our persistent database connection client pointer reference
db_connection = establish_secure_db_engine()

# =====================================================================
# SYSTEM COMPONENT INTERFACES (SQL ACTIONS)
# =====================================================================
def sql_create_node(name, location, cores, status):
    cur = db_connection.cursor()
    # Parameterized Query execution protects against SQL Injection vulnerabilities
    cur.execute("""
        INSERT INTO system_hardware (node_name, rack_location, core_count, status_flag)
        VALUES (?, ?, ?, ?);
    """, (name, location, cores, status))
    db_connection.commit()

def sql_read_all_nodes() -> pd.DataFrame:
    # Read straight from the database engine frame back into an interactive dataframe
    return pd.read_sql_query("SELECT * FROM system_hardware;", db_connection)

def sql_update_node_status(node_id, new_status):
    cur = db_connection.cursor()
    cur.execute("UPDATE system_hardware SET status_flag = ? WHERE node_id = ?;", (new_status, node_id))
    db_connection.commit()

def sql_delete_node(node_id):
    cur = db_connection.cursor()
    cur.execute("DELETE FROM system_hardware WHERE node_id = ?;", (node_id,))
    db_connection.commit()


# =====================================================================
# FRONTEND VIEW WORKSPACE LAYOUT
# =====================================================================
st.title("Infrastructure Database Management Workspace 💾")
st.write("Interactions slice straight through to a persistent SQLite relational database engine layer.")

st.write("---")

# Layout multi-view workspaces using functional panels
tab_view_create, tab_modify_delete = st.tabs(["📊 Read & Create Nodes", "⚙️ Update & Purge Matrix"])

# ---------------------------------------------------------------------
# TAB 1: READ (DISPLAY) AND CREATE (INSERT) OPERATIONAL WORKSPACES
# ---------------------------------------------------------------------
with tab_view_create:
    left_col, right_col = st.columns([2, 1])
    
    with left_col:
        st.header("Active Datacenter Infrastructure Registry")
        # Pull the fresh database dataset state out on every script refresh pass
        active_df = sql_read_all_nodes()
        
        if active_df.empty:
            st.info("The relational infrastructure inventory database is currently unpopulated.")
        else:
            st.dataframe(active_df, use_container_width=True, hide_index=True)
            
    with right_col:
        st.header("Provision New Node")
        # Enclose the data entry fields inside an atomic submission block
        with st.form(key="hardware_intake_form", clear_on_submit=True):
            in_name = st.text_input("Node Host Name:", placeholder="e.g., matrix-node-alpha")
            in_rack = st.selectbox("Rack Location Sector:", options=["US-EAST-RACK1", "US-WEST-RACK4", "EU-CENT-RACK2"])
            in_cores = st.slider("Allocated CPU Core Matrix:", min_value=2, max_value=128, value=16, step=2)
            in_status = st.radio("Initial Node Operational Status:", options=["ONLINE", "MAINTENANCE", "OFFLINE"])
            
            submit_node_btn = st.form_submit_button("Commit Node to Database")
            
        if submit_node_btn:
            if not in_name:
                st.error("Transaction Aborted: Node name cannot be empty.")
            else:
                sql_create_node(in_name, in_rack, in_cores, in_status)
                st.success(f"Successfully injected record reference '{in_name}' to relational memory.")
                st.rerun() # Forces top-to-bottom rerun to refresh the active dataframe view instantly

# ---------------------------------------------------------------------
# TAB 2: UPDATE (MODIFICATION) AND DELETE (PURGE) GATES
# ---------------------------------------------------------------------
with tab_modify_delete:
    fresh_df = sql_read_all_nodes()
    
    if fresh_df.empty:
        st.info("No database entries available to modify.")
    else:
        st.header("Database Mutation Operations")
        
        # Pull current node options to map user widget inputs directly to valid primary index IDs
        node_options = {f"ID {row['node_id']} | {row['node_name']}": row['node_id'] for _, row in fresh_df.iterrows()}
        selected_node_label = st.selectbox("Target Node Registry Reference:", options=list(node_options.keys()))
        target_id = node_options[selected_node_label]
        
        st.write("---")
        up_col, del_col = st.columns(2)
        
        with up_col:
            st.subheader("Update Operations Matrix")
            target_new_status = st.selectbox("Assign New Status Level:", options=["ONLINE", "MAINTENANCE", "OFFLINE"], key="up_status_select")
            
            if st.button("⚡ Update Status Record", use_container_width=True):
                sql_update_node_status(target_id, target_new_status)
                st.toast(f"Updated Node #{target_id} status matrix to {target_new_status}!", icon="✅")
                st.rerun()
                
        with del_col:
            st.subheader("Destructive Delete Operations Matrix")
            st.warning("Warning: Clicking the button below executes an un-recoverable SQL DELETE instruction row drop.")
            
            if st.button("🗑️ Permanently Delete Record from Disk", type="secondary", use_container_width=True):
                sql_delete_node(target_id)
                st.toast(f"Dropped Node #{target_id} tracking schema matrix permanently.", icon="💥")
                st.rerun()