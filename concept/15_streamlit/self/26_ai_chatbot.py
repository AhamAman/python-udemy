import streamlit as st
import time
from openai import OpenAI

st.set_page_config(page_title="AI Inference Engine", page_icon="🤖", layout="centered")

st.title("Accelerated AI Chat Core 🤖")
st.write("A stateful interface featuring real-time token response streaming.")

# =====================================================================
# 1. LIVE PERSISTENT CHAT HISTORY INITIALIZATION
# =====================================================================
if "messages" not in st.session_state:
    # Initialize the global messaging ledger with a default system greeting
    st.session_state["messages"] = [
        {"role": "assistant", "content": "AI Core operational. Standing by for prompt injection input tokens."}
    ]

# =====================================================================
# 2. LOCAL API CONFIGURATION GATEWAY
# =====================================================================
# To use live models, change the key string below or set it to read from st.secrets
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"

def get_llm_stream_generator(messages_history):
    """Dispatches chat arrays to inference endpoints and yields a chunk generator."""
    if OPENAI_API_KEY == "YOUR_OPENAI_API_KEY":
        # SAFE SANDBOX FALLBACK: Simulates an AI streaming generator locally
        mock_response = "This is an automated structural streaming response from your local matrix container. It demonstrates token generation speed without relying on external network dependencies or secret keys."
        for word in mock_response.split(" "):
            yield word + " "
            time.sleep(0.08) # Simulates natural inference latency
        return

    # To target a local model via Ollama instead, switch base_url to "http://localhost:11434/v1"
    client = OpenAI(api_key=OPENAI_API_KEY)
    
    response_stream = client.chat.completions.create(
        model="gpt-4o-mini", # Or your local model name target like "llama3"
        messages=messages_history,
        stream=True # CRITICAL: Tells the backend engine to stream tokens chunks
    )
    
    for chunk in response_stream:
        if chunk.choices[0].delta.content is not None:
            yield chunk.choices[0].delta.content

# =====================================================================
# 3. CONCURRENT CONVERSATION RENDERING VIEW
# =====================================================================
st.write("---")
# Loop through and redraw historical messages stored in session state memory
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# =====================================================================
# 4. INBOUND PROMPT CAPTURE (The Input Widget)
# =====================================================================
# st.chat_input builds a sticky, high-performance input bar at the bottom of the page
if user_prompt := st.chat_input("Inject prompt context here..."):
    
    # Render user prompt immediately onto the screen layout
    with st.chat_message("user"):
        st.write(user_prompt)
        
    # Append the message to our permanent history state array
    st.session_state["messages"].append({"role": "user", "content": user_prompt})
    
    # Trigger response generation loop inside the assistant chat context box
    with st.chat_message("assistant"):
        # Invoke the generator function passing our state history block
        token_generator = get_llm_stream_generator(st.session_state["messages"])
        
        # st.write_stream automatically drains the generator and animates characters
        streamed_response = st.write_stream(token_generator)
        
    # Append the finalized string output back to state to lock it across future reruns
    st.session_state["messages"].append({"role": "assistant", "content": streamed_response})