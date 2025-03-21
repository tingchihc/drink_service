import json
import os
from distutils.util import strtobool
import argparse

def str_to_bool(value):
    return bool(strtobool(value))

def main():
    
    parser = argparse.ArgumentParser(description="Function to add, remove, and update menu.")
    parser.add_argument('--add', type=str_to_bool, required=False)
    parser.add_argument('--remove', type=str_to_bool, required=False)
    parser.add_argument('--update', type=str_to_bool, required=False)
    parser.add_argument('--product', type=str, required=False)
    parser.add_argument('--cost', type=int, required=False)

    args = parser.parse_args()
    actions = {
        'add' : args.add,
        'remove' : args.remove,
        'update' : args.update,
    }
    cost, product = args.cost, args.product

    current_dir = os.getcwd()    
    MENU_FILENAME = os.path.join(current_dir, 'docs', 'menu.json')
    if os.path.exists(MENU_FILENAME) == False:
        data = {}
        for k, v in actions.items():
            if k == 'add' and v == True:
                data[product] = cost
            elif k == 'remove' and v == True:
                data.pop(product, None)
            elif k == 'update' and v == True:
                data[product] = cost
        
    else:
        with open(MENU_FILENAME, "r") as file:
            data = json.load(file)
        for k, v in actions.items():
            if k == 'add' and v == True:
                data[product] = cost
            elif k == 'remove' and v == True:
                data.pop(product, None)
            elif k == 'update' and v == True:
                data[product] = cost

        
    with open(MENU_FILENAME, "w") as file:
        json.dump(data, file, indent=4)

    

if __name__ == '__main__':
    main()

"""
python scripts/menu_setup.py --add True --product milk --cost 20
python scripts/menu_setup.py --add True --product tea --cost 30
python scripts/menu_setup.py --update True --product tea --cost 50
python scripts/menu_setup.py --update True --product green_tea --cost 70
python scripts/menu_setup.py --remove True --product milk
python scripts/menu_setup.py --remove True --product black_tea
"""
