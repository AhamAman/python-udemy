import streamlit as st
import time

st.set_page_config(page_title="Cache Engine: Resources", page_icon="💾", layout="centered")

st.title("Persistent Database Driver Cache Engine 💾")
st.write("Demonstrates how `@st.cache_resource` retains connection state wrappers across the runtime context.")

# Mock class representing a stateful Database Connection Pool Driver
class MockDatabaseConnectionPool:
    def __init__(self):
        self.connection_id = "CONN-POOL-0X7F82"
        self.creation_time = time.time()
        
    def execute_query(self, sql_statement):
        return f"Executing [ {sql_statement} ] via dedicated pipe reference {self.connection_id}"

# =====================================================================
# PERSISTENT SYSTEM RESOURCE CACHING LAYER
# =====================================================================
@st.cache_resource
def establish_master_db_connection_pool():
    """Initializes a heavy database connection client once, preserving it across runs."""
    st.write("🔧 *[System Message]* Booting connection handshake sequence over socket...")
    time.sleep(2.0) # Simulate a heavy initialization handshake
    return MockDatabaseConnectionPool()

st.write("---")

start_init = time.time()

# Claim our database resource pool pointer reference
db_pool = establish_master_db_connection_pool()

init_duration = time.time() - start_init
st.caption(f"Resource resolution window: **{init_duration:.4f} seconds**")

# =====================================================================
# INTERACTIVE WORKSPACE VIEW
# =====================================================================
st.subheader("Live Database Interaction Node")
st.write(f"Active Pool Handle ID: `{db_pool.connection_id}`")
st.write(f"Initial Socket Allocation Timestamp: `{db_pool.creation_time}`")

sql_command = st.text_input("Construct relational SQL query line:", value="SELECT * FROM product_inventory;")

if st.button("⚡ Dispatch Query Packet to Database"):
    # Reuses the exact same cached pool instance to fire commands immediately
    query_receipt = db_pool.execute_query(sql_command)
    st.info(query_receipt)
    st.toast("Database transaction executed successfully!", icon="✅")