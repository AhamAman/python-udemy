import streamlit as st
import requests
import pandas as pd
import time

st.set_page_config(page_title="Crypto Market Matrix", page_icon="🪙", layout="wide")

# =====================================================================
# CACHED REST API NETWORK INGESTION LAYER
# =====================================================================
# We set an explicit Time-To-Live (TTL) of 60 seconds to refresh metrics
# without spamming the network socket on every user click interaction.
@st.cache_data(ttl=60, show_spinner="Querying global crypto exchange nodes...")
def fetch_crypto_ticker_metrics():
    """Queries the public CoinGecko REST API endpoint structure."""
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "ids": "bitcoin,ethereum,solana,cardano,ripple",
        "order": "market_cap_desc"
    }
    try:
        response = requests.get(url, params=params, timeout=5.0)
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"API Transport Error: HTTP Status {response.status_code}")
            return None
    except requests.exceptions.RequestException as err:
        st.error(f"Network Connection Failed: {err}")
        return None

# =====================================================================
# FRONTEND INTERFACE DASHBOARD APPLICATION
# =====================================================================
st.title("Global Cryptographical Asset Matrix 🪙")
st.write("Live exchange valuations cached at a strict 60-second operational threshold matrix.")

st.write("---")

# Execute network fetch
raw_market_data = fetch_crypto_ticker_metrics()

if raw_market_data:
    # Normalize the JSON dictionary array directly into a Pandas DataFrame
    df = pd.DataFrame(raw_market_data)
    
    # Extract specific target tracking arrays
    btc_metrics = df[df['id'] == 'bitcoin'].iloc[0]
    eth_metrics = df[df['id'] == 'ethereum'].iloc[0]
    sol_metrics = df[df['id'] == 'solana'].iloc[0]
    
    # 1. SIDE-BY-SIDE LEDGER KPIS
    col1, col2, col3 = st.columns(3)
    col1.metric(
        label="Bitcoin (BTC/USD)", 
        value=f"${btc_metrics['current_price']:,}", 
        delta=f"{btc_metrics['price_change_percentage_24h']:.2f}%"
    )
    col2.metric(
        label="Ethereum (ETH/USD)", 
        value=f"${eth_metrics['current_price']:,}", 
        delta=f"{eth_metrics['price_change_percentage_24h']:.2f}%"
    )
    col3.metric(
        label="Solana (SOL/USD)", 
        value=f"${sol_metrics['current_price']:,}", 
        delta=f"{sol_metrics['price_change_percentage_24h']:.2f}%"
    )
    
    st.write("---")
    
    # 2. SELECTION VISUALIZATION CHANNELS
    left_pane, right_pane = st.columns([1, 2])
    
    with left_pane:
        st.subheader("Market Cap Allocation")
        # Isolate subset matrix for charting
        viz_df = df[['name', 'market_cap']].set_index('name')
        st.bar_chart(viz_df)
        
    with right_pane:
        st.subheader("Asset Registry Ledger")
        display_df = df[['market_cap_rank', 'name', 'symbol', 'current_price', 'total_volume', 'high_24h']]
        st.dataframe(display_df, use_container_width=True, hide_index=True)
        
else:
    st.info("Unable to parse market metrics. Verify connection channels or local proxy routing parameters.")