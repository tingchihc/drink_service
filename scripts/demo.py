import json
import os

current_dir = os.getcwd()

# read the menu file
MENU_FILENAME = os.path.join(current_dir, 'docs', 'menu.json')
with open(MENU_FILENAME, 'r') as file:
    menu = json.load(file)

# read admin docs
admin_docs = os.path.join(current_dir, 'admin', 'info.json')
with open(admin_docs, 'r') as file:
    admin = json.load(file)

# read custormer docs
customer_docs = os.path.join(current_dir, 'customer', 'member.json')
with open(customer_docs, 'r') as file:
    member = json.load(file)

user_input = input("Enter username: ")
if user_input == admin["user"]:
    password = input("Enter password: ")
    if password == admin["password"]:
        print("Welcome admin")
        print("Menu: ", menu)

    else:
        print("Invalid password")

else:
    password = input("Enter password: ")
    for k, v in member.items():
        if user_input == v["user"] and password == v["password"]:
            print("Welcome", v["user"])
            print("Menu: ", menu)
            break
