import streamlit as st

# Set up page configurations
st.set_page_config(page_title="My Personal Profile", page_icon="🚀", layout="centered")

# Title Element
st.title("Welcome to My Portfolio Matrix 🪐")

# Subheader
st.subheader("Data Engineer | System Architect | Lifelong Learner")

# Use st.write with Markdown for regular paragraph prose
st.write("""
Hi there! I am an engineer passionate about designing fault-tolerant, high-concurrency data systems. 
I specialize in breaking down complex architectural patterns into elegant code structures. 
""")

st.write("---") # Horizontal Rule separator

# Section 1: Core Competencies
st.header("🎯 Core Focus Areas")

st.write("""
* **Languages:** Python, SQL, Rust
* **Frameworks:** FastAPI, Streamlit, Asyncio
* **Data Tier:** PostgreSQL, Redis, Apache Kafka
""")

# Section 2: Personal Mission
st.header("💡 Engineering Philosophy")

st.write("> *'Simplicity is a prerequisite for reliability.'* – Edsger W. Dijkstra")

st.text("Current Status: Building distributed worker systems in stealth mode.")