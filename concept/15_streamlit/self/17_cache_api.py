import streamlit as st
import time
import pandas as pd

st.set_page_config(page_title="Cache Engine: API", page_icon="🌐", layout="centered")

st.title("Accelerated HTTP API Caching Matrix 🌐")
st.write("Demonstrates how `@st.cache_data` intercepts network latency boundaries across script reruns.")

# 1. DECORATE THE GATHERING LAYER
@st.cache_data(show_spinner="Querying remote HTTP API asset endpoints...")
def fetch_volatile_api_stream(endpoint_node):
    """Simulates a heavy, slow network-bound API ingest."""
    time.sleep(2.5) # Forced network latency penalty block
    
    # Generate mock telemetry records
    payload = {
        "Node_Address": [f"{endpoint_node}-01", f"{endpoint_node}-02", f"{endpoint_node}-03"],
        "Throughput_Mb_s": [894.2, 741.8, 912.5],
        "Packet_Drop_Rate": [0.001, 0.005, 0.000]
    }
    return pd.DataFrame(payload)

st.write("---")

# User widget control forces an intentional top-to-bottom script rerun on alteration
selected_node = st.selectbox("Select Cloud Target Cluster Vector:", options=["US-EAST", "EU-CENTRAL", "AP-SOUTH"])

start_clock = time.time()

# 2. INVOKE THE CACHED INTERACTION
# If 'selected_node' matches a previous signature, execution finishes in microseconds
data_lake = fetch_volatile_api_stream(selected_node)

duration = time.time() - start_clock

# 3. VERIFY EXECUTION SPEED
if duration > 1.0:
    st.warning(f"🚨 Cache Miss! Function ran completely. Network roundtrip latency: {duration:.4f} seconds.")
else:
    st.success(f"⚡ Cache Hit! Extracted results instantly out of system RAM in {duration:.4f} seconds.")

st.dataframe(data_lake, use_container_width=True)

st.write("---")
# Interactive button to manually trigger a rerun and test cache retention
st.button("🔄 Trigger Stateless App Rerun Loop")