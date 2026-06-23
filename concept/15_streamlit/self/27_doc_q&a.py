import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Knowledge Engine Matrix", page_icon="💾", layout="centered")

st.title("Contextual Document Q&A Matrix 💾")
st.write("Upload a reference text document to ground your AI prompt tokens in custom data.")

st.write("---")

# 1. FILE INGESTION BUFFER
uploaded_doc = st.file_uploader("Mount target reference document configuration asset:", type=["txt", "md"])

if uploaded_doc is not None:
    # Read raw bytes straight out of the volatile memory buffer and decode to string
    document_string_context = uploaded_doc.read().decode("utf-8")
    
    st.success(f"Context locked: {uploaded_doc.name} (~{len(document_string_context)} characters uploaded)")
    
    with st.expander("👁️ Inspect Encapsulated Document Data View"):
        st.text(document_string_context[:1000] + ("..." if len(document_string_context) > 1000 else ""))
        
    st.write("---")
    st.subheader("Query Context Window")
    user_query = st.text_input("Ask a question specific to the grounded data above:", placeholder="e.g., Summarize the core metrics.")
    
    if st.button("⚡ Dispatch Query Context to LLM", use_container_width=True):
        if not user_query:
            st.error("Transaction Aborted: Prompt field cannot be left unpopulated.")
        else:
            # 2. CONSTRUCT SYSTEM GROUNDING PROMPT MATRIX
            # We inject the data directly into the system message wrapper
            structured_messages = [
                {
                    "role": "system", 
                    "content": f"You are a precise data analysis bot. You must answer the user's question using ONLY the provided document text context block below.\n\nDOCUMENT CONTEXT:\n{document_string_context}"
                },
                {"role": "user", "content": user_query}
            ]
            
            st.write("---")
            st.subheader("Inference Analysis Output")
            
            # 3. INTERFERENCE ROUTE DISPATCH
            with st.spinner("Executing analytical prompt engineering path..."):
                try:
                    # Direct generation block call
                    # Substitute OpenAI setup with your live client or mock stream as done in Project 1
                    client = OpenAI(api_key="YOUR_OPENAI_API_KEY")
                    response = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=structured_messages,
                        stream=False
                    )
                    st.info(response.choices[0].message.content)
                    
                except Exception:
                    # Graceful interface sandbox fallback logic if keys are missing
                    st.caption("⚠️ Running inside Sandbox Offline Mode. Below is the generated prompt context template package that would be pushed to your LLM API:")
                    st.json(structured_messages)
else:
    st.info("Please mount an operational plain text data file (`.txt`) via the uploader to begin.")