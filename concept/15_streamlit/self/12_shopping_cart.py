import streamlit as st
import pandas as pd

st.set_page_config(page_title="E-Commerce State Matrix", page_icon="🛒", layout="wide")

st.title("Stateful Inventory Shopping Cart 🛒")
st.write("Add individual tracking items to memory buffers and monitor the live collection array.")

st.write("---")

# 1. SETUP SESSION STATE DATA LEDGER
if "shopping_cart" not in st.session_state:
    # Initialize our cart as an empty list container matrix
    st.session_state["shopping_cart"] = []

# Mock product directory menu
inventory_catalog = {
    "Quantum Laptop Engine": 1499.00,
    "Mechanical Macro Keyboard": 125.00,
    "OLED Spatial Monitor": 899.00,
    "Titanium Ergo Desk": 650.00
}

# 2. WIDGET CONTROLS PANELS
left_pane, right_pane = st.columns([1, 2])

with left_pane:
    st.header("Product Catalogue")
    
    target_product = st.selectbox("Choose an item to acquire:", options=list(inventory_catalog.keys()))
    product_price = inventory_catalog[target_product]
    
    st.write(f"**Unit Cost:** ${product_price:,.2f} USD")
    
    # Ingestion Trigger Button
    if st.button("🛒 Add Item to Cart Session", use_container_width=True):
        # Append selected data straight into the session state list buffer
        st.session_state["shopping_cart"].append({
            "Product Name": target_product,
            "Price_USD": product_price
        })
        st.toast(f"Added {target_product} to memory array!", icon="✅")

    st.write("---")
    if st.button("🗑️ Empty Cart Matrix", type="secondary"):
        st.session_state["shopping_cart"] = []
        st.rerun() # Forces a clean rerun to wipe the screen immediately

with right_pane:
    st.header("Your Active Shopping Cart State")
    
    if not st.session_state["shopping_cart"]:
        st.info("Your shopping cart is completely unpopulated.")
    else:
        # Convert our session state memory array directly into a Pandas DataFrame
        cart_df = pd.DataFrame(st.session_state["shopping_cart"])
        
        # Render the current state table
        st.dataframe(cart_df, use_container_width=True)
        
        # Calculate summary telemetry metrics
        total_sum = cart_df["Price_USD"].sum()
        item_count = len(cart_df)
        
        st.write("---")
        c1, c2 = st.columns(2)
        c1.metric(label="Total Items Captured", value=item_count)
        c2.metric(label="Aggregated Financial Ledger Cost", value=f"${total_sum:,.2f}")