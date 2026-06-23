import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Component Matrix Studio", page_icon="🧩", layout="centered")

st.title("Custom Component Communication Studio 🧩")
st.write("Demonstrates how standard Python scripts inject raw client-side HTML, CSS, and JavaScript canvas spaces.")

st.write("---")

# 1. ARCHITECT THE RAW FRONTEND CHUNK (HTML + CSS + JavaScript)
# This code runs directly inside the client's web browser DOM frame
custom_html_code = """
<div style="background-color: #1e1e2e; padding: 20px; border-radius: 10px; border: 1px solid #ff79c6; color: #f8f8f2; font-family: monospace;">
    <h3 style="color: #ff79c6; margin-top: 0;">Client-Side JavaScript Canvas Box</h3>
    <p>This box is executed inside an isolated browser iframe block layer.</p>
    
    <label for="node-selector">Dispatch Internal Token Selection:</label><br/>
    <select id="node-selector" style="background: #282a36; color: #f8f8f2; border: 1px solid #6272a4; padding: 5px; margin-top: 8px; border-radius: 5px; width: 100%;">
        <option value="CLUSTER_NODE_ALPHA">Cluster Vector Alpha</option>
        <option value="CLUSTER_NODE_BETA">Cluster Vector Beta</option>
        <option value="CLUSTER_NODE_GAMMA">Cluster Vector Gamma</option>
    </select>
    
    <br/><br/>
    <button onclick="dispatchAlert()" style="background: #ff79c6; color: #1e1e2e; border: none; padding: 8px 12px; font-weight: bold; border-radius: 5px; cursor: pointer; width: 100%;">
        Trigger Client Browser Alert
    </button>
</div>

<script>
    function dispatchAlert() {
        const selectedNode = document.getElementById('node-selector').value;
        // Native client browser popup alert trigger
        alert("Event Frame Intercepted! Target Matrix Node Selected: " + selectedNode);
    }
</script>
"""

# 2. RENDER THE CUSTOM FRAME INNER CANVAS
st.subheader("Embedded Component Viewport")
st.write("The widget below is generated completely out of custom string arrays:")

# components.html mounts our raw code layout safely on the screen page
components.html(custom_html_code, height=220, scrolling=False)

st.write("---")

# 3. INTERFACING WITH POPULAR THIRD-PARTY COMPONENTS
st.subheader("Third-Party Ecosystem Implementation Preview")
st.write("To utilize heavy open-source tools like `streamlit_option_menu`, you initialize them cleanly in your standard script files:")

st.code("""
# Pipeline reference pattern for production deployment
from streamlit_option_menu import option_menu

selected_tab = option_menu(
    menu_title="Main Network Navigation",
    options=["Home Vector", "Database Metrics", "Cloud Topologies"],
    icons=["house", "database", "cloud"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal"
)
""", language="python")