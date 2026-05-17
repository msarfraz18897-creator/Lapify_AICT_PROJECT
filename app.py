import streamlit as st

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Lapify",
    page_icon="💻",
    layout="wide"
)

# ================= TITLE =================
st.title("💻 Lapify - Laptop Recommendation System")

st.markdown("""
Welcome to **Lapify** 🎯

This smart laptop suggester helps users choose the right laptop
according to their needs and budget.
""")

# ================= DATA =================

laptop_brands = [
    "Apple",
    "HP",
    "Dell",
    "Lenovo",
    "Asus",
    "Acer",
    "Samsung",
    "Huawei",
    "Microsoft",
]

laptops = {
    'Business/Students Laptops': {
        'Apple': ['MacBook Air M1', 'MacBook Air M2', 'MacBook Pro 13'],
        'HP': ['EliteBook 840', 'ProBook 450', 'Dragonfly'],
        'Dell': ['Latitude 5440', 'Latitude 7440', 'XPS 13'],
        'Lenovo': ['ThinkPad X1 Carbon', 'ThinkPad T14', 'ThinkPad L14']
    },

    'Gaming Laptops': {
        'HP': ['Omen 16', 'Victus 15'],
        'Dell': ['Alienware m15', 'Dell G15'],
        'Lenovo': ['Legion 5', 'Legion 7'],
        'Asus': ['ROG Strix G16', 'TUF Gaming F15']
    },

    'Workstation Laptops': {
        'Apple': ['MacBook Pro 14 M2 Pro'],
        'Dell': ['Precision 3581'],
        'Lenovo': ['ThinkPad P1']
    }
}

laptop_specs = {
    'MacBook Air M1': {
        'Processor': 'Apple M1',
        'RAM': '8GB',
        'Storage': '256GB SSD',
        'Display': '13.3-inch Retina'
    },

    'Omen 16': {
        'Processor': 'AMD Ryzen 7',
        'RAM': '16GB',
        'Storage': '1TB SSD',
        'Display': '16.1-inch 165Hz'
    },

    'Alienware m15': {
        'Processor': 'Intel Core i7',
        'RAM': '16GB',
        'Storage': '1TB SSD',
        'Display': '15.6-inch 240Hz'
    },

    'XPS 13': {
        'Processor': 'Intel Core i7',
        'RAM': '16GB',
        'Storage': '512GB SSD',
        'Display': '13.4-inch FHD'
    }
}

faq_list = {
    "How do I choose the right laptop?":
        "Choose according to your needs such as gaming, business or study.",

    "How much RAM do I need?":
        "8GB for normal use and 16GB+ for gaming or professional work.",

    "What is SSD?":
        "SSD is faster and more reliable than HDD."
}

accessories = {
    "Keyboard": ["Logitech MX Keys", "Razer BlackWidow"],
    "Microphone": ["Blue Yeti", "HyperX QuadCast"],
    "Cooling Pad": ["Cooler Master Notepal", "KLIM Wind"]
}

# ================= SIDEBAR =================

st.sidebar.title("Navigation")

menu = st.sidebar.radio(
    "Select Option",
    [
        "Home",
        "Laptop Brands",
        "Laptop Categories",
        "Laptop Suggestor",
        "Accessories",
        "FAQs",
        "About Us",
        "Contact Us"
    ]
)

# ================= HOME =================

if menu == "Home":

    st.header("🏠 Home")

    st.write("""
Many people waste money on laptops they don't actually need.
Lapify helps users choose the best laptop according to their requirements.
""")

# ================= BRANDS =================

elif menu == "Laptop Brands":

    st.header("💻 Laptop Brands")

    for brand in laptop_brands:
        st.write(f"✅ {brand}")

# ================= CATEGORIES =================

elif menu == "Laptop Categories":

    st.header("📂 Laptop Categories")

    for category in laptops.keys():
        st.write(f"🔹 {category}")

# ================= LAPTOP SUGGESTOR =================

elif menu == "Laptop Suggestor":

    st.header("🎯 Laptop Suggestor")

    category = st.selectbox(
        "Select Laptop Category",
        list(laptops.keys())
    )

    brand = st.selectbox(
        "Select Brand",
        list(laptops[category].keys())
    )

    st.subheader("Available Models")

    models = laptops[category][brand]

    selected_model = st.selectbox(
        "Select Laptop Model",
        models
    )

    if selected_model in laptop_specs:

        st.subheader("Specifications")

        specs = laptop_specs[selected_model]

        for key, value in specs.items():
            st.write(f"**{key}:** {value}")

    else:
        st.warning("Specifications accessible with paid plan.")

# ================= ACCESSORIES =================

elif menu == "Accessories":

    st.header("🖥 Laptop Accessories")

    accessory_type = st.selectbox(
        "Select Accessory",
        list(accessories.keys())
    )

    for item in accessories[accessory_type]:
        st.write(f"✅ {item}")

# ================= FAQ =================

elif menu == "FAQs":

    st.header("❓ Frequently Asked Questions")

    for question, answer in faq_list.items():

        with st.expander(question):
            st.write(answer)

# ================= ABOUT =================

elif menu == "About Us":

    st.header("ℹ About Us")

    st.write("""
Lapify is a smart laptop recommendation system developed to help users choose the right laptop according to their needs and budget.
""")

    st.markdown("""
<div style='padding:15px;border-radius:10px;background-color:#1e1e1e'>

<h3 style='color:#00FFFF;'>🎓 ICT Lab Project</h3>

<p style='font-size:18px;color:white;'>
This project was developed under the guidance and support of our respected Lab Engineers.
</p>

<h2 style='color:#FFD700;'>👨‍🏫 Lab Engineers</h2>

<h3 style='color:#00FF7F;'>✨ Muhammad Musa ✨</h3>

<h3 style='color:#FF69B4;'>✨ Urwa Rasheed ✨</h3>

<p style='font-size:17px;color:#D3D3D3;'>
Their continuous encouragement, technical assistance, and support helped us complete this project successfully.
</p>

<h2 style='color:#00BFFF;'>👨‍💻 Developed By</h2>

<h3 style='color:#FFA500;'>Muhammad Sarfraz</h3>

<h3 style='color:#7CFC00;'>Mehwish bibi</h3>

<h2 style='color:#FF6347;'>🚀 Our Goal</h2>

<p style='font-size:17px;color:white;'>
To help users make smarter and more informed laptop purchasing decisions.
</p>

</div>
""", unsafe_allow_html=True)
# ================= CONTACT =================

elif menu == "Contact Us":

    st.header("📞 Contact Us")

    st.write("📍 PIEAS Islamabad, Pakistan")
    st.write("📧 msarfraz18897@gmail.com")
    st.write("whatsapp📱 +923049476304")
