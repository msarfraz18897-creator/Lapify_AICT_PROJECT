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
    "Microsoft"
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
    },

    '2-in-1 / Convertible Laptops': {
        'HP': ['Spectre x360'],
        'Dell': ['Inspiron 14 2-in-1'],
        'Lenovo': ['Yoga 7i']
    },

    'Budget / Entry-Level Laptops': {
        'HP': ['HP 15'],
        'Dell': ['Inspiron 15'],
        'Lenovo': ['IdeaPad 3']
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
        'Storage': '512GB SSD',
        'Display': '13.6-inch Retina'
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
        'Graphics': 'RTX 3070'
    },

    'XPS 13': {
        'Processor': 'Intel Core i7',
        'RAM': '16GB',
        'Storage': '512GB SSD',
        'Display': '13.4-inch FHD'
    },

    'Legion 5': {
        'Processor': 'AMD Ryzen 7',
        'RAM': '16GB',
        'Storage': '512GB SSD',
        'Graphics': 'RTX 3060'
    },

    'ROG Strix G16': {
        'Processor': 'Intel Core i9',
        'RAM': '16GB',
        'Storage': '1TB SSD',
        'Graphics': 'RTX 4070'
    }
}

# ================= FAQS =================

faq_list = {

    "1. How do I choose the right laptop?":
    "Consider your usage: business, gaming, or basic tasks. Look at RAM, storage, processor, and battery life.",

    "2. What is the best laptop for students?":
    "Business or student laptops with good battery life and portability are ideal.",

    "3. Can I upgrade RAM or storage later?":
    "Some laptops allow upgrades while others have soldered components.",

    "4. How often should I replace my laptop?":
    "Typically every 3-5 years depending on performance needs.",

    "5. What is the difference between SSD and HDD?":
    "SSD is much faster and more reliable than HDD.",

    "6. What is a 2-in-1 laptop?":
    "A laptop that works as both a tablet and laptop.",

    "7. How much RAM do I need?":
    "8GB for normal use and 16GB+ for gaming or professional work.",

    "8. Are gaming laptops good for work?":
    "Yes, gaming laptops are powerful enough for professional tasks.",

    "9. Do I need a touchscreen laptop?":
    "Only if you need stylus or touch functionality.",

    "10. Can I game on a budget laptop?":
    "Yes, but with lower graphics settings.",

    "11. What is the difference between Intel and AMD?":
    "Intel offers strong single-core performance while AMD excels in multi-core tasks.",

    "12. How long does battery life last?":
    "Usually between 4 to 20 hours depending on usage.",

    "13. Should I prioritize CPU or GPU?":
    "Gaming needs GPU while workstation tasks need CPU + RAM.",

    "14. How can I maintain my laptop?":
    "Keep it dust-free and avoid overheating.",

    "15. Do you provide warranty info?":
    "Always check the manufacturer warranty before purchase."
}

# ================= ACCESSORIES =================

accessories = {

    "Keyboard": [
        "Logitech MX Keys",
        "Razer BlackWidow",
        "Keychron K2"
    ],

    "Microphone": [
        "Blue Yeti",
        "HyperX QuadCast",
        "Fifine A6V"
    ],

    "Cooling Pad": [
        "Cooler Master Notepal",
        "KLIM Wind",
        "Havit HV-F2056"
    ]
}

# ================= SIDEBAR =================

st.sidebar.title("Navigation")

menu = st.sidebar.radio(
    "Select Option",
    [
        "Project Report",
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

# ================= PROJECT REPORT =================

if menu == "Project Report":

    st.title("Full Project Report")

    st.header("Pakistan Institute of Engineering & Applied Sciences")

    st.subheader("AICT LAB PROJECT")

    st.write("A Console-Based Laptop & Accessories Recommendation System")

    st.markdown("---")

    st.subheader("Submitted By")

    st.write("""
• Muhammad Sarfraz  
• Mehwish Bibi
""")

    st.subheader("Project Supervisors")

    st.markdown("""
<h3 style='color:#00BFFF;'>Muhammad Musa</h3>
<h3 style='color:#00BFFF;'>Urwa Rasheed</h3>
""", unsafe_allow_html=True)

    st.markdown("---")

    st.header("1. Introduction")

    st.write("""
Lapify is a smart laptop recommendation system designed to help users select laptops according to their needs and budget.

Many users buy expensive laptops with unnecessary features. This project helps users make better and smarter decisions.
""")

    st.header("2. Objectives")

    st.write("""
• Recommend laptops according to category  
• Show laptop specifications  
• Suggest accessories  
• Provide FAQs and guidance  
• Help users avoid wrong purchases
""")

    st.header("3. Technologies Used")

    st.write("""
• Python  
• Streamlit  
• Dictionaries  
• Conditional Statements  
• Loops  
• Functions
""")

    st.header("4. Features")

    st.write("""
• Laptop Brands  
• Laptop Categories  
• Laptop Suggestor  
• Accessories  
• FAQs  
• About Us  
• Contact Us
""")

    st.header("5. Conclusion")

    st.write("""
Lapify successfully demonstrates a modern laptop recommendation system using Python and Streamlit.
""")

    st.success("Project Report Loaded Successfully")

# ================= HOME =================

elif menu == "Home":

    st.header("Home")

    st.write("""
Many people waste money on laptops they don't actually need.

Lapify helps users choose the best laptop according to their requirements and budget.
""")

# ================= BRANDS =================

elif menu == "Laptop Brands":

    st.header("Laptop Brands")

    for brand in laptop_brands:
        st.write(f"• {brand}")

# ================= CATEGORIES =================

elif menu == "Laptop Categories":

    st.header("Laptop Categories")

    for category in laptops.keys():
        st.write(f"• {category}")

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

    models = laptops[category][brand]

    selected_model = st.selectbox(
        "Select Laptop Model",
        models
    )

    st.subheader("Available Models")

    for model in models:
        st.write(f"• {model}")

    if selected_model in laptop_specs:

        st.subheader("Specifications")

        specs = laptop_specs[selected_model]

        for key, value in specs.items():
            st.write(f"**{key}:** {value}")

    else:
        st.warning("Detailed specifications are not available.")

# ================= ACCESSORIES =================

elif menu == "Accessories":

    st.header("Laptop Accessories")

    accessory_type = st.selectbox(
        "Select Accessory Type",
        list(accessories.keys())
    )

    st.subheader(accessory_type)

    for item in accessories[accessory_type]:
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
margin-bottom:12px;
">
Muhammad Musa
</h3>

<h3 style="
color:#00BFFF;
font-size:30px;
font-weight:700;
font-family:Verdana;
">
Urwa Rasheed
</h3>

</div>

<p style="
font-size:18px;
color:#D6D6D6;
line-height:1.8;
margin-top:25px;
font-family:Arial;
">
Their encouragement, mentorship, and technical guidance played a major role in the successful completion of this project.
</p>

<hr style="border:1px solid #444; margin-top:30px; margin-bottom:30px;">

<h2 style="
color:#FFB000;
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
color:#FFB000;
font-size:32px;
font-weight:700;
font-family:Verdana;
margin-bottom:12px;
">
Muhammad Sarfraz
</h3>

<h3 style="
color:#FFB000;
font-size:32px;
font-weight:700;
font-family:Verdana;
">
Mehwish Bibi
</h3>

</div>

<hr style="border:1px solid #444; margin-top:30px; margin-bottom:30px;">

<h2 style="
color:#FF6347;
font-size:34px;
font-family:Arial;
font-weight:bold;
">
Our Goal
</h2>

<p style="
font-size:19px;
color:#F5F5F5;
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

    st.write("PIEAS Islamabad, Pakistan")
    st.write("Email: msarfraz18897@gmail.com")
    st.write("WhatsApp: +92 304 9476304")
