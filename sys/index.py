import os
import json

def get_admin_info():
    current_dir = os.getcwd()
    ADMIN_INFO = os.path.join(current_dir, "admin", "info.json")
    with open(ADMIN_INFO, "r") as f:
        admin = json.load(f)
    return admin["user"], admin["password"]

def get_customer_info():
    current_dir = os.getcwd()
    CUSTOMER_MEMBER = os.path.join(current_dir, "customer", "member.json")
    with open(CUSTOMER_MEMBER, "r") as f:
        member = json.load(f)
    
    DATA = {}
    for id_, info_ in member.items():
        DATA[info_]["user"] = DATA[info_]["password"]
    
    return DATA
    
