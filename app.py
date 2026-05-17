import streamlit as st
import json

st.title("Lapify - Laptop Recommendation System")

st.write("Welcome to Lapify")

# Load laptops data
with open("Lapify.py1/laptops.json", "r") as file:
    laptops = json.load(file)

brands = []

for laptop in laptops:
    if laptop["brand"] not in brands:
        brands.append(laptop["brand"])

selected_brand = st.selectbox("Select Brand", brands)

if st.button("Show Laptops"):
    for laptop in laptops:
        if laptop["brand"] == selected_brand:
            st.subheader(laptop["name"])
            st.write(laptop)
