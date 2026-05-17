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
        "Full Project Report",
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

if menu == "Full Project Report":

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

elif menu == "FAQs":

    st.header("Frequently Asked Questions")

    for question, answer in faq_list.items():

        with st.expander(question):
            st.write(answer)

# ================= ABOUT =================

elif menu == "About Us":

    st.header("About Us")

    st.write("""
Lapify is a smart laptop recommendation system developed to help users choose the right laptop according to their needs and budget.
""")

    st.markdown("""
<div style='padding:20px;border-radius:15px;background-color:#1e1e1e'>

<h2 style='color:#00FFFF;'>AICT Lab Project</h2>

<p style='font-size:18px;color:white;'>
This project was developed under the guidance and support of our respected instructors.
</p>

<h2 style='color:#FFD700;'>Project Supervisors</h2>

<h3 style='color:#00FF7F;'>Muhammad Musa</h3>

<h3 style='color:#FF69B4;'>Urwa Rasheed</h3>

<p style='font-size:17px;color:#D3D3D3;'>
Their encouragement and technical guidance played a major role in the successful completion of this project.
</p>

<h2 style='color:#00BFFF;'>Developed By</h2>

<h3 style='color:#FFA500;'>Muhammad Sarfraz</h3>

<h3 style='color:#7CFC00;'>Mehwish Bibi</h3>

<h2 style='color:#FF6347;'>Our Goal</h2>

<p style='font-size:17px;color:white;'>
To help users make smarter and more informed laptop purchasing decisions.
</p>

</div>
""", unsafe_allow_html=True)

# ================= CONTACT =================

elif menu == "Contact Us":

    st.header("Contact Us")

    st.write("PIEAS Islamabad, Pakistan")
    st.write("Email: msarfraz18897@gmail.com")
    st.write("WhatsApp: +92 304 9476304")
