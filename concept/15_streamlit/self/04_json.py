import streamlit as st
import time

st.set_page_config(page_title="API Response Terminal", page_icon="🌐", layout="centered")

st.title("API Response Payload Inspector 🌐")
st.write("Simulates fetching remote system matrices and displays the telemetry outputs.")

st.write("---")

# 1. Mock a structured transaction payload returned from a mock microservice gateway
mock_api_payload = {
    "status": "ACCEPTED",
    "transaction_meta": {
        "order_id": "ORD-99124",
        "cluster_node": "US-EAST-MATRIX-01",
        "timestamp": int(time.time()),
        "security_hash": "0x7f82b3a1c99e"
    },
    "order_data": {
        "ticker": "NVDA",
        "quantity": 50,
        "price_cents": 85000,
        "execution_priority": 1
    },
    "routing_logs": [
        "Inbound connection handshake accepted.",
        "Pydantic schema parameters validated successfully.",
        "Transaction committed to local record matrix."
    ]
}

# 2. Render the API output view configurations
st.header("Terminal Node Status")

# Use st.success/st.info for clear notification banners
st.success("HTTP 200 OK: Data asset stream received.")

st.subheader("Interactive JSON Payload Tree")
st.write("Click the arrows below to expand or collapse specific nested nodes in the data structure:")

# st.json elegantly formats complex nested objects out-of-the-box
st.json(mock_api_payload)

st.write("---")

# 3. Alternative: Show raw code blocks if the user prefers unformatted logs
st.subheader("Raw Code Print Block Alternative")
st.write("If you need to copy unformatted raw text logs:")
st.code(str(mock_api_payload), language="python")