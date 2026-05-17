import streamlit as st
import json

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Lapify",
    page_icon="💻",
    layout="wide"
)

# ---------------- TITLE ----------------
st.title("💻 Lapify - Laptop Recommendation System")
st.markdown("Find the perfect laptop according to your needs.")

# ---------------- LOAD FILES ----------------
with open("Lapify.py1/laptops.json", "r") as file:
    laptops_data = json.load(file)

with open("Lapify.py1/laptop_accessories.json", "r") as file:
    accessories_data = json.load(file)

with open("Lapify.py1/faq.json", "r") as file:
    faq_data = json.load(file)

# ---------------- SIDEBAR ----------------
st.sidebar.title("Navigation")

section = st.sidebar.radio(
    "Go To",
    [
        "Laptop Recommendations",
        "Laptop Accessories",
        "FAQs"
    ]
)

# =====================================================
# LAPTOP SECTION
# =====================================================

if section == "Laptop Recommendations":

    st.header("Laptop Categories")

    categories = list(laptops_data.keys())

    selected_category = st.selectbox(
        "Select a Category",
        categories
    )

    if st.button("Show Laptops"):

        st.subheader(f"{selected_category}")

        laptops_list = laptops_data[selected_category]

        for laptop in laptops_list:

            st.markdown("---")

            # If laptop is dictionary
            if isinstance(laptop, dict):

                for key, value in laptop.items():
                    st.write(f"**{key}:** {value}")

            else:
                st.write(laptop)

# =====================================================
# ACCESSORIES SECTION
# =====================================================

elif section == "Laptop Accessories":

    st.header("Laptop Accessories")

    for accessory in accessories_data:

        st.markdown("---")

        if isinstance(accessory, dict):

            for key, value in accessory.items():
                st.write(f"**{key}:** {value}")

        else:
            st.write(accessory)

# =====================================================
# FAQ SECTION
# =====================================================

elif section == "FAQs":

    st.header("Frequently Asked Questions")

    if isinstance(faq_data, list):

        for item in faq_data:

            st.markdown("---")

            if isinstance(item, dict):

                for key, value in item.items():
                    st.write(f"**{key}:** {value}")

            else:
                st.write(item)

    elif isinstance(faq_data, dict):

        for question, answer in faq_data.items():

            st.markdown("---")
            st.write(f"**Q:** {question}")
            st.write(f"**A:** {answer}")
