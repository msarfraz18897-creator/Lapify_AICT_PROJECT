print()  # spacing from the above text at the starting
print("\033[31m A console-based Laptop Suggester\033[0m")
print("============================================================")
print("\033[33m \t\t\t--> Lapify <--\033[0m")
print("============================================================")

print()
print("\033[31m Here is the overview of the store \033[0m")
print("\033[35m Overview:\n \033[0m")
print("\033[33m Many people waste money on the wrong devices because they follow trends instead of their real needs, \n ending up with features they never use and performance they don’t get. We want to help them by suggesting \n the right device so their money is spent wisely.")
print()
print(" This laptop suggester will allow you to view laptops, categories, accessories and display product details. \033[0m")
print("="*110)
print("")

def main_menu():
    menu = ["View Laptop Brands","View Laptop Categories","Laptop Suggestor","View Accessories","FAQs","About Us","Contact Us","Exit Program"]
    print()
    print("\033[32m Please select your choice: \033[0m")
    for i in range(len(menu)):
        print(f"{i+1}.{menu[i]}")
       
main_menu()

laptop_brands = ["1.Apple","2.HP","3.Dell","4.Lenovo","5.Asus","6.Acer","7.Samsung","8.Huawei","9.Microsoft"]
laptop_accessories = ["1.Keyboard","2.Mic","3.Cooling pad"]

laptop_categories = {
    "1. Business Laptops": {"info": "Slim, lightweight, portable, Long battery life"},
    "2. Gaming Laptops": {"info": "High-performance CPUs & GPUs, High-refresh-rate displays"},
    "3. Workstation Laptops": {"info": "Very powerful hardware, For 3D modeling, video editing, engineering, AI/ML"},
    "4. 2-in-1 / Convertible Laptops": {"info": "Can be used as both laptop and tablet, Touchscreen + stylus support"},
    "5. Budget / Entry-Level Laptops": {"info": "Affordable, Good for basic tasks like browsing, office apps, and online classes"},
}



#function for the laptop accessories
def accessories():
    import json
    with open("laptop_accessories.json","r") as file:
        accessory_data = json.load(file)
            
    while True:
        try:
            Laptop_Accessories()
            accessory_choice = int(input(f"\033[36mEnter your choice for the required accessory (1-3 only): \033[0m"))
            if 1 <= accessory_choice <= 3:
                break
            else:
                print("Wrong choice!")
        except ValueError:
            print("Please enter only numbers (1-3)")
    
    category_map = {1: "keyboard", 2: "microphone", 3: "cooling_fan"}
    selected_category = category_map[accessory_choice]

    print(f"\nOptions for {selected_category.capitalize()}s:\n")
    
    for brand, items in accessory_data[selected_category].items():
        print(f"\033[35m{brand}:\033[0m")
        for item in items:  # for printing the items of the brand
            print(f"  - {item}")
        print()  #spacing between brands
        

#function for the laptop brands
def Laptop_Brands():
    print()
    print("="*30)
    print("\033[31mThese are the laptop brands\033[0m")
    for brands in laptop_brands:
        print(f"\033[33m {brands} \033[0m")
    print("="*30)
    
#function for the laptop categories
def Laptop_Categories():
    print()
    print("="*30)
    print("\033[31mThese are the laptop categories\033[0m")
    for category, details in laptop_categories.items():
        print(f"\033[33m{category}: \033[0m\033[32m{details['info']}\033[0m")
    print("="*30)


#function for the laptop accessories menu
def Laptop_Accessories():
    print("="*30)
    print("\033[31mThese are the laptop accessories\033[0m")
    for items in laptop_accessories:
        print(f"\033[33m {items} \033[0m")
    print("="*30)

def about_us():
    print("="*120)
    print("\033[35m1. Deliver a reliable and transparent laptop buying platform\n\n2. Offer clear, need-based recommendations and comparisons\n\n3. Help customers make informed purchasing decisions\n\n4. Maximize value while eliminating post-purchase regret\033[0m")
    print("="*120)

def contact_us():
    print("="*50)
    print("This is how you can contact us")
    print("\033[31mLocation: Lapify, 58-B, 3rd Floor, Hafeez Center, Gulberg 3, Lahore\033[0m")
    print("\033[31mPhone: 062-2733980\033[0m")
    print("\033[31mEmail: support@lapify.com\033[0m")
    print("="*50)


import json
with open("laptops.json","r") as file:
    laptops = json.load(file)


import json
with open("laptop_specifications.json","r") as file:
    laptop_specs = json.load(file)



def laptop_suggest():
    categories = list(laptops.keys())

    for i, category in enumerate(categories, 1):
        print(f"\033[33m{i}. {category}\033[0m")

    choice = int(input("\nSelect a category (1-5): ")) - 1

    if 0 <= choice < len(categories):
        selected_category = categories[choice]
        print(f"\033[31m\n --> {selected_category} <-- \n\033[0m")

        for company, models in laptops[selected_category].items():
            print(f"\033[36m{company}:\033[0m")

            for model in models:
                print(f"  -\033[35m {model}\033[0m")

                if model in laptop_specs:
                    specs = laptop_specs[model]
                    for key, value in specs.items():
                        print(f"      {key}: {value}")
                else:
                    print("      \033[31mSpecifications accessible with a paid plan\033[0m")
                    print("      Contact us for paid plan!")

            print()
    else:
        print("\033[31m Invalid choice \033[0m")


def FAQs():    
    import json
    with open("faq.json","r") as file:
        faq_list = json.load(file)
    
    print("="*130)
    for key,value in faq_list.items():
        print(f"\033[31m {key} \033[0m:- \n {value}")
        print()
    print("="*130)






def get_choice():
    while True:
        try:
            print()
            choice = int(input("\033[36mEnter your choice from the above menu:\033[0m "))

            if 1 <= choice <= 8:
                if choice == 1:
                    Laptop_Brands()
                elif choice == 2:
                    Laptop_Categories()
                elif choice == 3:
                    laptop_suggest()
                elif choice == 4:
                    # Laptop_Accessories()
                    
                    accessories()
                elif choice == 5:
                    FAQs()
                elif choice == 6:
                    about_us()
                elif choice == 7:
                    contact_us()
                elif choice == 8:
                    print("\033[32mThanks for using Lapify. Goodbye!\033[0m")
                    break

                main_menu()

            else:
                print("="*20)
                print("\033[31mPlease re-enter your choice (1 to 8).\033[0m")
                main_menu()

        except ValueError:
            print("="*20)
            print("\033[31mPlease enter only integer (1 to 7) values.\033[0m")
            main_menu()

# The program will start from here 
get_choice()
