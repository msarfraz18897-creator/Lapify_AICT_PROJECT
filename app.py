import streamlit as st

# ================= PAGE CONFIG =================

st.set_page_config(
    page_title="Lapify",
    page_icon="💻",
    layout="wide"
)

# ================= TITLE =================

st.title("Lapify - Laptop Recommendation System")

st.write("""
Welcome to Lapify

A smart laptop recommendation system that helps users choose the right laptop according to their needs and budget.
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

laptop_categories = {
    "Business Laptops": "Slim, lightweight, portable, Long battery life",
    "Gaming Laptops": "High-performance CPUs & GPUs, High-refresh-rate displays",
    "Workstation Laptops": "Very powerful hardware, For 3D modeling, video editing, engineering, AI/ML",
    "2-in-1 / Convertible Laptops": "Can be used as both laptop and tablet, Touchscreen + stylus support",
    "Budget / Entry-Level Laptops": "Affordable, Good for basic tasks like browsing, office apps, and online classes",
}

# ================= ACCESSORIES =================

accessory_data = {

    'keyboard': {
        'Logitech': ['MX Keys', 'MX Mechanical', 'G Pro X', 'G915 Lightspeed', 'K380'],
        'Microsoft': ['Sculpt Ergonomic Keyboard', 'Surface Keyboard', 'Designer Compact Keyboard'],
        'Razer': ['BlackWidow V4', 'Huntsman Mini', 'Huntsman Elite', 'Ornata V3'],
        'Corsair': ['K95 RGB Platinum', 'K70 RGB MK.2', 'K100 RGB', 'K65 Mini'],
        'SteelSeries': ['Apex Pro', 'Apex 7', 'Apex 3', 'Apex Pro Mini'],
        'Keychron': ['Keychron K2', 'Keychron K4', 'Keychron K6', 'Keychron K8 Pro', 'Keychron Q1'],
        'Ducky': ['One 2 Mini', 'One 3 SF', 'One 3 TKL', 'Shine 7'],
        'Drop': ['Drop CTRL', 'Drop ALT', 'Drop SHIFT'],
        'Filco': ['Majestouch 2', 'Majestouch Convertible 2'],
        'HHKB': ['HHKB Professional Hybrid', 'HHKB Professional Classic'],
        'Epomaker': ['EP84', 'TH80', 'GK68XS'],
        'Akko': ['Akko 3068B', 'Akko 5075S', 'Akko MOD 007'],
        'Royal Kludge': ['RK61', 'RK84', 'RK96']
    },

    'microphone': {
        'Shure': ['SM58', 'SM57', 'SM7B', 'MV7', 'MV7+'],
        'Audio-Technica': ['AT2020', 'AT2020USB', 'AT2035', 'AT4040'],
        'Rode': ['NT1-A', 'NT-USB', 'NT-USB Mini', 'PodMic'],
        'Sennheiser': ['MD421', 'MD441', 'MKH416', 'Evolution Series'],
        'Neumann': ['U87', 'TLM 102', 'KM 184', 'TLM 103'],
        'AKG': ['C414 XLS', 'P220', 'C214'],
        'Blue': ['Yeti', 'Snowball'],
        'HyperX': ['QuadCast', 'QuadCast S', 'QuadCast 2'],
        'Samson': ['Q2U', 'Go Mic'],
        'Behringer': ['C-1U', 'XM8500'],
        'Fifine': ['AM8', 'A6V'],
        'Boya': ['BY-MM1', 'Magic Mic']
    },

    'cooling_fan': {
        'Cooler Master': ['Notepal X3', 'Notepal U3 Plus', 'Notepal XL'],
        'Thermaltake': ['Massive 20 RGB', 'Massive TM', 'Massive 14'],
        'Havit': ['HV-F2056', 'HV-F2076', 'HV-F2081'],
        'KLIM': ['Wind', 'Cool Plus', 'Cyclone'],
        'TopMate': ['C5', 'C11', 'K5'],
        'Deepcool': ['N200', 'Multi Core X6'],
        'Targus': ['Chill Mat', 'Dual Fan Chill Mat'],
        'Tree New Bee': ['Cooling Pad', 'RGB Cooling Pad'],
        'Cosmic Byte': ['Meteor', 'Cyclone'],
        'Zinq': ['Zinq Cool Slate', 'Zinq Z20 Cooler'],
        'Portronics': ['Toad 13', 'Toad 15'],
        'Lapcare': ['ChillMate', 'Coolpad']
    }
}

# ================= LAPTOPS =================

laptops = {

    'Business/Students Laptops': {
        'Apple': ['MacBook Air M1', 'MacBook Air M2', 'MacBook Pro 13'],
        'HP': ['EliteBook 840', 'ProBook 450', 'Dragonfly'],
        'Dell': ['Latitude 5440', 'Latitude 7440', 'XPS 13'],
        'Lenovo': ['ThinkPad X1 Carbon', 'ThinkPad T14', 'ThinkPad L14'],
        'Asus': ['ExpertBook B9', 'ZenBook 14', 'ZenBook S13'],
        'Acer': ['TravelMate P6', 'TravelMate P4', 'Swift 5'],
        'Samsung': ['Galaxy Book2 Pro', 'Galaxy Book Pro 360', 'Galaxy Book3'],
        'Huawei': ['MateBook X Pro', 'MateBook 14', 'MateBook D16'],
        'Microsoft': ['Surface Laptop 4', 'Surface Laptop 5', 'Surface Laptop Studio']
    },

    'Gaming Laptops': {
        'Apple': ['MacBook Pro 14', 'MacBook Pro 16', 'MacBook Air M2'],
        'HP': ['Omen 16', 'Victus 15', 'Omen X'],
        'Dell': ['Alienware m15', 'Alienware x16', 'Dell G15'],
        'Lenovo': ['Legion 5', 'Legion 7', 'Legion Pro 5'],
        'Asus': ['ROG Strix G16', 'ROG Zephyrus G14', 'TUF Gaming F15'],
        'Acer': ['Predator Helios 300', 'Predator Triton 500', 'Nitro 5'],
        'Samsung': ['Galaxy Book Odyssey', 'Galaxy Book Ultra', 'Galaxy Book Pro'],
        'Huawei': ['MateBook 16s', 'MateBook X Pro', 'MateBook D16'],
        'Microsoft': ['Surface Laptop Studio', 'Surface Book 3', 'Surface Pro 9']
    }
}

# ================= FAQS =================

faq_list = {

    "1. How do I choose the right laptop?":
    "Consider your usage: business, gaming, or basic tasks. Look at specs like RAM, storage, CPU, and battery life.",

    "2. What is the best laptop for students?":
    "Business or student laptops with long battery life, portability, and moderate performance are ideal.",

    "3. Can I upgrade the RAM or storage later?":
    "Depends on the model. Some laptops have soldered RAM or SSDs, so check specs before buying.",

    "4. How often should I replace my laptop?":
    "Typically every 3-5 years depending on usage, software requirements, and performance needs.",

    "5. Do you provide warranty or support info?":
    "Yes, always check the manufacturer’s warranty for each laptop and available support plans.",

    "6. What is the difference between SSD and HDD?":
    "SSD is faster, quieter, and more durable than HDD. HDD is cheaper and offers more storage.",

    "7. What is a 2-in-1 laptop?":
    "A 2-in-1 or convertible laptop can function as both a laptop and a tablet.",

    "8. How much RAM do I need?":
    "For basic use: 8GB is sufficient. For gaming or professional work: 16GB or more is recommended.",

    "9. How long does a laptop battery last?":
    "Battery life varies from 4 to 20 hours depending on the model, usage, and power settings.",

    "10. Are gaming laptops suitable for work tasks?":
    "Yes, gaming laptops are powerful but heavier and consume more battery.",

    "11. What is the difference between Intel and AMD processors?":
    "Intel has strong single-core performance; AMD offers better multi-core performance in many models.",

    "12. Should I prioritize CPU, GPU, or RAM?":
    "Gaming = GPU, Workstation = CPU+RAM, Basic = balanced specs.",

    "13. Do I need a touchscreen laptop?":
    "Only if you plan to use touch features or stylus input.",

    "14. Can I use a laptop for gaming on a budget?":
    "Yes, but budget laptops may limit graphics settings.",

    "15. How do I clean and maintain my laptop?":
    "Keep it dust-free, avoid liquid spills, use a cooling pad, and clean the screen with microfiber cloth."
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

    st.header("Home")

    st.write("""
This laptop suggester allows users to view laptops, categories, accessories and display product details.
""")

    st.info("""
Many people waste money on the wrong devices because they follow trends instead of their real needs,
ending up with features they never use and performance they don’t get.

Lapify helps users choose the right device so their money is spent wisely.
""")
# ================= BRANDS =================

elif menu == "Laptop Brands":

    st.header("Laptop Brands")

    for brand in laptop_brands:
        st.write(f"• {brand}")

# ================= CATEGORIES =================

elif menu == "Laptop Categories":

    st.header("Laptop Categories")

    for category, info in laptop_categories.items():
        st.write(f"### {category}")
        st.write(info)

# ================= LAPTOP SUGGESTOR =================

elif menu == "Laptop Suggestor":

    st.header("Laptop Suggestor")

    category = st.selectbox(
        "Select Laptop Category",
        list(laptops.keys())
    )

    brand = st.selectbox(
        "Select Brand",
        list(laptops[category].keys())
    )

    st.subheader("Available Models")

    for model in laptops[category][brand]:
        st.write(f"• {model}")

# ================= ACCESSORIES =================

elif menu == "Accessories":

    st.header("Laptop Accessories")

    accessory_type = st.selectbox(
        "Select Accessory Type",
        list(accessory_data.keys())
    )

    for brand, items in accessory_data[accessory_type].items():

        st.markdown(f"### {brand}")

        for item in items:
            st.write(f"• {item}")

# ================= FAQS =================

elif menu == "FAQs":

    st.header("Frequently Asked Questions")

    for question, answer in faq_list.items():

        with st.expander(question):
            st.write(answer)

# ================= ABOUT US =================

elif menu == "About Us":

    st.header("About Us")

    st.markdown("""
<div style="
padding:35px;
border-radius:18px;
background: linear-gradient(135deg, #1f1f1f, #2b2b2b);
">

<h1 style="color:#00D4FF;">Lapify</h1>

<p style="font-size:20px;color:#E0E0E0;">
Lapify is a smart laptop recommendation system developed to help users choose the right laptop according to their needs and budget.
</p>

<h2 style="color:#FFD700;">Project Supervisors</h2>

<h3 style="color:#00BFFF;">Muhammad Musa</h3>
<h3 style="color:#00BFFF;">Urwa Rasheed</h3>

<h2 style="color:#FFB000;">Developed By</h2>

<h3 style="color:#FFB000;">Muhammad Sarfraz</h3>
<h3 style="color:#FFB000;">Mehwish Bibi</h3>

</div>
""", unsafe_allow_html=True)

# ================= CONTACT =================

elif menu == "Contact Us":

    st.header("Contact Us")

    st.write("Location: Lapify, 58-B, 3rd Floor, Hafeez Center, Gulberg 3, Lahore")
    st.write("Phone: 062-2733980")
    st.write("Email: support@lapify.com")
