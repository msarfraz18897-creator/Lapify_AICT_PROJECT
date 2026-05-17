import streamlit as st
import json

st.title("Lapify - Laptop Recommendation System")
st.write("Welcome to Lapify")

# Load JSON data
with open("Lapify.py1/laptops.json", "r") as file:
    laptops = json.load(file)

# Get categories
categories = list(laptops.keys())

# Dropdown
selected_category = st.selectbox("Select Category", categories)

# Show laptops
if st.button("Show Laptops"):
    
    st.subheader(f"{selected_category}")

    for item in laptops[selected_category]:
        st.write(item)
