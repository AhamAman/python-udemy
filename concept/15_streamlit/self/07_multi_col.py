import streamlit as st
import random

st.set_page_config(page_title="Infrastructure Matrix", page_icon="🖥️", layout="wide")

st.title("Enterprise Infrastructure Monitor 🖥️")
st.write("This layout utilizes structural horizontal columns to display high-frequency operational telemetry side-by-side.")

st.write("---")

st.subheader("Live Node Metrics")

# 1. Instantiate 4 horizontal columns with variable relative widths
# Pass an array of integers to define width proportions: [1, 1, 1, 1] means equal spacing
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("### Node-Alpha")
    st.metric(label="CPU Utilization", value="42.5%", delta="+2.1%")

with col2:
    st.markdown("### Node-Beta")
    st.metric(label="Memory Allocation", value="78.1 GB", delta="-4.3 GB", delta_color="inverse")

with col3:
    st.markdown("### Network Ingest")
    st.metric(label="Active Bandwidth", value="894 Mb/s", delta="0.0 Mb/s")

with col4:
    st.markdown("### Storage Array")
    st.metric(label="Disk Capacity Used", value="14.2 TB", delta="+0.8 TB", delta_color="off")

st.write("---")

# 2. Re-using columns further down the page to split chart / text layouts
left_pane, right_pane = st.columns([2, 1]) # The left pane is twice as wide as the right pane

with left_pane:
    st.header("Operational Event Streams")
    st.info("System Engine Note: Automated daily cron maintenance scripts cleared active cache tables.")
    st.code("""
[2026-06-23 20:01:05] CONNECTED: Remote node connection pool 127.0.0.1 handshaking...
[2026-06-23 20:01:08] TRANS_OK: Pydantic schema validated successfully.
[2026-06-23 20:01:10] DISCONNECT: Socket reference dropped cleanly by peer client.
    """, language="log")

with right_pane:
    st.header("Node Properties")
    st.markdown("""
    * **OS Kernel:** Linux Ubuntu 24.04 LTS
    * **Active Architecture:** x86_64 Matrix Core
    * **ASGI Server Node:** Uvicorn Engine
    * **Database Connector:** asyncpg Pool
    """)