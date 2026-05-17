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
        'Graphics': 'RTX 3070'
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
        "Choose according to your requirements such as gaming, business, or studies.",

    "How much RAM do I need?":
        "8GB is enough for normal users while 16GB or more is recommended for gaming and professional work.",

    "What is SSD?":
        "SSD is faster and more reliable than traditional HDD storage."
}

accessories = {

    "Keyboard": [
        "Logitech MX Keys",
        "Razer BlackWidow"
    ],

    "Microphone": [
        "Blue Yeti",
        "HyperX QuadCast"
    ],

    "Cooling Pad": [
        "Cooler Master Notepal",
        "KLIM Wind"
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

# ================= FULL PROJECT REPORT =================

if menu == "Project Report":

    st.title("Project Report")

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
<h3 style='color:#00FF7F;'>Muhammad Musa</h3>

<h3 style='color:#FF69B4;'>Urwa Rasheed</h3>
""", unsafe_allow_html=True)

    st.markdown("---")

    st.header("1. Introduction")

    st.write("""
In today’s fast-paced digital world, choosing the right laptop has become a challenging task due to the vast number of brands, models, and specifications available.

Many users end up purchasing laptops that do not meet their actual requirements, resulting in wasted money and dissatisfaction.

Lapify is a Python-based laptop recommendation system designed to help users choose suitable laptops and accessories according to their needs.
""")

    st.header("2. Problem Statement")

    st.write("""
Many customers follow market trends instead of understanding their personal requirements while buying laptops.

This often leads to purchasing devices with unnecessary features or insufficient performance.
""")

    st.header("3. Objectives of the Project")

    st.write("""
• To guide users in selecting laptops according to categories  
• To provide laptop brand and specification details  
• To recommend accessories such as keyboards, microphones, and cooling pads  
• To create an interactive recommendation system  
• To minimize wrong purchasing decisions
""")

    st.header("4. Scope of the Project")

    st.write("""
• Laptop recommendations  
• Laptop specifications  
• Accessories suggestions  
• FAQs and project information
""")

    st.header("5. Technologies Used")

    st.write("""
• Python  
• Streamlit  
• JSON Data Handling  
• File Handling  
• Functions  
• Conditional Statements  
• Loops
""")

    st.header("6. Project Workflow")

    st.write("""
1. User opens the application  
2. User selects desired option  
3. System processes the request  
4. Results are displayed interactively
""")

    st.header("7. Main Features")

    st.write("""
• Laptop Brands  
• Laptop Categories  
• Laptop Suggestor  
• Accessories  
• FAQs  
• About Us  
• Contact Us
""")

    st.header("8. Conclusion")

    st.write("""
Lapify successfully demonstrates a laptop and accessories recommendation system using Python and Streamlit.

The project helps users make informed purchasing decisions through an interactive and user-friendly interface.
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
        st.warning("Detailed specifications available in premium version.")

# ================= ACCESSORIES =================

elif menu == "Accessories":

    st.header("Laptop Accessories")

    accessory_type = st.selectbox(
        "Select Accessory Type",
        list(accessories.keys())
    )

    for item in accessories[accessory_type]:
        st.write(f"• {item}")

# ================= FAQ =================

faq_list = {

    "1. How do I choose the right laptop?":
    "Consider your usage: business, gaming, or basic tasks. Look at specs like RAM, storage, CPU, and battery life.",

    "2. What is the best laptop for students?":
    "Business or student laptops with long battery life, portability, and moderate performance are ideal.",

    "3. Can I upgrade the RAM or storage later?":
    "Depends on the model. Some laptops have soldered RAM or SSDs, so check specifications before buying.",

    "4. How often should I replace my laptop?":
    "Typically every 3-5 years depending on usage, software requirements, and performance needs.",

    "5. Do you provide warranty or support info?":
    "Yes, always check the manufacturer warranty and available support plans.",

    "6. What is the difference between SSD and HDD?":
    "SSD is faster, quieter, and more durable than HDD. HDD is cheaper and offers larger storage.",

    "7. What is a 2-in-1 laptop?":
    "A 2-in-1 laptop can function as both a laptop and a tablet with touchscreen support.",

    "8. How much RAM do I need?":
    "8GB is enough for normal users while 16GB or more is recommended for gaming and professional work.",

    "9. How long does a laptop battery last?":
    "Battery life varies from 4 to 20 hours depending on model and usage.",

    "10. Are gaming laptops suitable for work tasks?":
    "Yes, gaming laptops are powerful enough for professional tasks but are usually heavier.",

    "11. What is the difference between Intel and AMD processors?":
    "Intel provides strong single-core performance while AMD offers excellent multi-core performance.",

    "12. Should I prioritize CPU, GPU, or RAM?":
    "It depends on your needs: Gaming = GPU, Workstation = CPU + RAM, Basic Use = balanced specifications.",

    "13. Do I need a touchscreen laptop?":
    "Only if you plan to use touch features or stylus input. Otherwise it is optional.",

    "14. Can I use a laptop for gaming on a budget?":
    "Yes, but budget gaming laptops may require lower graphics settings.",

    "15. How do I clean and maintain my laptop?":
    "Keep it dust-free, avoid liquids, use a cooling pad, and clean the screen with a microfiber cloth."
}

# ================= ABOUT =================

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
color:#00FF99;
font-size:30px;
font-weight:700;
font-family:Verdana;
margin-bottom:12px;
">
Muhammad Musa
</h3>

<h3 style="
color:#FF66C4;
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
color:#00BFFF;
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
color:#FFA500;
font-size:32px;
font-weight:700;
font-family:Verdana;
margin-bottom:12px;
">
Muhammad Sarfraz
</h3>

<h3 style="
color:#7CFC00;
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
