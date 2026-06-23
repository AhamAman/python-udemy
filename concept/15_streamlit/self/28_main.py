import streamlit as st
import os
from openai import OpenAI

st.set_page_config(page_title="Production Node Engine", page_icon="🌐", layout="wide")

# =====================================================================
# DEFENSIVE PRODUCTION SECRETS ACQUISITION GATEWAY
# =====================================================================
@st.cache_resource
def load_production_api_token() -> str:
    """
    Checks Streamlit's secrets matrix first. Fallbacks immediately to standard
    OS environment variables to comply with containerized cloud layouts.
    """
    # Pattern A: Check native Streamlit secrets
    if "OPENAI_API_KEY" in st.secrets:
        return st.secrets["OPENAI_API_KEY"]
        
    # Pattern B: Check systemic OS environment layers (Docker / AWS / Render)
    os_env_match = os.environ.get("OPENAI_API_KEY")
    if os_env_match:
        return os_env_match
        
    return "NOT_CONFIGURED"

# Resolve target token parameter
active_token = load_production_api_token()

# =====================================================================
# ARCHITECTURAL DASHBOARD INTERFACE CANVAS
# =====================================================================
st.title("Production Analytics & AI Inference Cluster 🌐")
st.write("Verifies container environment metrics and routes live inference token streams.")

st.write("---")

# Layout multi-column diagnostic grids
col_left, col_right = st.columns([1, 2])

with col_left:
    st.header("Infrastructure Node Diagnostics")
    
    # Render runtime credential configuration metrics
    if active_token == "NOT_CONFIGURED":
        st.error("Credential Status: OFFLINE (Missing OPENAI_API_KEY environment configuration)")
    else:
        st.success("Credential Status: ENCRYPTED_TUNNEL_ACTIVE")
        # Obfuscate secret token layout to secure the operator display
        st.caption(f"Token Mask: `...{active_token[-6:] if len(active_token) > 6 else 'VALID'}`")

    st.write("---")
    st.subheader("System Environment Properties")
    st.markdown(f"""
    * **Runtime Execution Layer:** {'Docker Container / Cloud Host' if os.environ.get('IS_DOCKER') else 'Localized Process Loop'}
    * **Server Gateway Port:** `8501`
    * **Internal Stream Engine:** Streamlit Production Core
    """)

with col_right:
    st.header("Inference Pipeline Portal")
    user_prompt = st.text_input("Dispatch real-time analysis prompt:", placeholder="e.g., Analyze cloud node performance data.")
    
    if st.button("⚡ Dispatch Pipeline Tokens", use_container_width=True):
        if active_token == "NOT_CONFIGURED":
            st.warning("Execution Suspended: Please provision a valid API Key asset within the environment variables.")
        elif not user_prompt:
            st.error("Execution Suspended: Input text path cannot be empty.")
        else:
            with st.spinner("Processing inference across target matrix nodes..."):
                try:
                    # Initialize our OpenAI client using the dynamically resolved production token
                    client = OpenAI(api_key=active_token)
                    completion = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=[{"role": "user", "content": user_prompt}]
                    )
                    st.info(completion.choices[0].message.content)
                except Exception as err:
                    st.error(f"Inference pipeline aborted with error trace: {err}")