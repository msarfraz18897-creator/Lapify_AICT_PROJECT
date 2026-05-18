
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
# ================= LAPTOP SPECS =================

laptop_specs = {

    'MacBook Air M1': {
        'Processor': 'Apple M1',
        'RAM': '8GB',
        'Storage': '256GB SSD',
        'Display': '13.3-inch Retina'
    },

    'MacBook Air M2': {
        'Processor': 'Apple M2',
        'RAM': '8GB',
        'Storage': '256GB SSD',
        'Display': '13.6-inch Retina'
    },

    'MacBook Pro 13': {
        'Processor': 'Apple M2',
        'RAM': '8GB',
        'Storage': '512GB SSD',
        'Display': '13.3-inch Retina'
    },

    'MacBook Pro 14': {
        'Processor': 'Apple M2 Pro',
        'RAM': '16GB',
        'Storage': '512GB SSD',
        'Display': '14-inch Liquid Retina'
    },

    'MacBook Pro 16': {
        'Processor': 'Apple M2 Max',
        'RAM': '16GB',
        'Storage': '1TB SSD',
        'Display': '16-inch Liquid Retina'
    },

    'EliteBook 840': {
        'Processor': 'Intel Core i5',
        'RAM': '8GB',
        'Storage': '512GB SSD',
        'Display': '14-inch FHD'
    },

    'ProBook 450': {
        'Processor': 'Intel Core i5',
        'RAM': '8GB',
        'Storage': '512GB SSD',
        'Display': '15.6-inch FHD'
    },

    'Omen 16': {
        'Processor': 'AMD Ryzen 7',
        'RAM': '16GB',
        'Storage': '1TB SSD',
        'Display': '16.1-inch 165Hz'
    },

    'XPS 13': {
        'Processor': 'Intel Core i7',
        'RAM': '16GB',
        'Storage': '512GB SSD',
        'Display': '13.4-inch FHD'
    },

    'Inspiron 15': {
        'Processor': 'Intel Core i3',
        'RAM': '8GB',
        'Storage': '256GB SSD',
        'Display': '15.6-inch HD'
    },

    'Alienware m15': {
        'Processor': 'Intel Core i7',
        'RAM': '16GB',
        'Storage': '1TB SSD',
        'Display': '15.6-inch 240Hz'
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

    st.markdown("---")

    st.markdown(f"""
    <h2 style='color:#00BFFF;'>
    {brand} Laptops
    </h2>
    """, unsafe_allow_html=True)

    models = laptops[category][brand]

    selected_model = st.selectbox(
        "Select Laptop Model",
        models
    )

    st.markdown("---")

    st.markdown(f"""
    <div style="
    background-color:#1f1f1f;
    padding:25px;
    border-radius:15px;
    border:1px solid #333;
    ">

    <h2 style='color:#FFD700;'>
    {selected_model}
    </h2>
    """, unsafe_allow_html=True)

    if selected_model in laptop_specs:

        specs = laptop_specs[selected_model]

        for key, value in specs.items():

            st.markdown(f"""
            <p style='font-size:18px; color:#E0E0E0;'>
            <b>{key}:</b> {value}
            </p>
            """, unsafe_allow_html=True)

    else:

        st.markdown("""
        <p style='color:#FF4B4B; font-size:18px;'>
        Specifications not available for this model.
        </p>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
# ================= ACCESSORIES =================

if menu == "Accessories":

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
box-shadow: 0px 0px 15px rgba(0,0,0,0.4);
">

<h1 style="
color:#00D4FF;
font-size:42px;
font-family:Arial;
font-weight:700;
margin-bottom:15px;
">
Lapify
</h1>

<p style="
font-size:20px;
color:#E0E0E0;
line-height:1.8;
font-family:Arial;
">
Lapify is a smart laptop recommendation system developed to help users choose the right laptop according to their needs and budget.
</p>

<hr style="border:1px solid #444; margin-top:25px; margin-bottom:25px;">

<h2 style="
color:#FFD700;
font-size:34px;
font-family:Arial;
font-weight:bold;
">
Project Supervisors
</h2>

<div style="
background-color:#252525;
padding:20px;
border-radius:12px;
margin-top:15px;
">

<h3 style="
color:#00BFFF;
font-size:30px;
font-weight:700;
font-family:Verdana;
margin-bottom:10px;
">
Muhammad Musa
</h3>

<p style="
font-size:17px;
color:#D3D3D3;
line-height:1.7;
margin-bottom:25px;
">
A supportive and dedicated supervisor whose guidance and technical assistance greatly helped in the successful completion of this project.
</p>

<h3 style="
color:#00BFFF;
font-size:30px;
font-weight:700;
font-family:Verdana;
margin-bottom:10px;
">
Urwa Rasheed
</h3>

<p style="
font-size:17px;
color:#D3D3D3;
line-height:1.7;
">
Provided continuous encouragement, valuable ideas, and professional mentorship throughout the development of this project.
</p>

</div>

<hr style="border:1px solid #444; margin-top:30px; margin-bottom:30px;">

<h2 style="
color:#FFD700;
font-size:34px;
font-family:Arial;
font-weight:bold;
">
Developed By
</h2>

<div style="
background-color:#252525;
padding:20px;
border-radius:12px;
margin-top:15px;
">

<h3 style="
color:#00BFFF;
font-size:32px;
font-weight:700;
font-family:Verdana;
margin-bottom:15px;
">
Muhammad Sarfraz
</h3>

<h3 style="
color:#00BFFF;
font-size:32px;
font-weight:700;
font-family:Verdana;
">
Mehwish Bibi
</h3>

</div>

<hr style="border:1px solid #444; margin-top:30px; margin-bottom:30px;">

<h2 style="
color:#FFD700;
font-size:34px;
font-family:Arial;
font-weight:bold;
">
Our Goal
</h2>

<p style="
font-size:19px;
color:#FF4B4B;
line-height:1.8;
font-family:Arial;
">
To help users make smarter, faster, and more informed laptop purchasing decisions through an interactive recommendation system.
</p>

</div>
""", unsafe_allow_html=True)

# ================= CONTACT =================

elif menu == "Contact Us":

    st.header("Contact Us")

    st.write("PIEAS University Islamabad,Pakistan")
    st.write("Whatsapp: <span style='color:#00BFFF;'>03049476304</span>", unsafe_allow_html=True)
    st.write("Email: msarfraz18897@gmail.com")
