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

    st.markdown("---")

    st.subheader("Laptop Specifications")

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
            'Display': '13.6-inch Liquid Retina'
        },

        'MacBook Pro 13': {
            'Processor': 'Apple M2',
            'RAM': '8GB',
            'Storage': '512GB SSD',
            'Display': '13.3-inch Retina'
        },

        'Omen 16': {
            'Processor': 'AMD Ryzen 7',
            'RAM': '16GB',
            'Storage': '1TB SSD',
            'Graphics': 'RTX 4060'
        },

        'Alienware m15': {
            'Processor': 'Intel Core i7',
            'RAM': '16GB',
            'Storage': '1TB SSD',
            'Graphics': 'RTX 3070'
        }
    }

    if selected_model in laptop_specs:

        specs = laptop_specs[selected_model]

        for key, value in specs.items():
            st.write(f"**{key}:** {value}")

    else:

        st.warning("Specifications not available for this model.")
