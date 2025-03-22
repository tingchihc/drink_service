import json
import os
import argparse


def main():
    
    parser = argparse.ArgumentParser(description="Function to setup the special in menu.")
    parser.add_argument('--item', type=str, required=False)
    parser.add_argument('--amount', type=int, required=False)
    parser.add_argument('--cost', type=int, required=False)
    args = parser.parse_args()

    item, cost, amount = args.item, args.cost, args.amount

    current_dir = os.getcwd()
    
    ITEMS_FILENAME = os.path.join(current_dir, 'docs', 'items.json')    
    SPECIAL_FILENAME = os.path.join(current_dir, 'docs', 'special.json')
    
    with open(ITEMS_FILENAME, "r") as file:
        items = json.load(file)
    
    if os.path.exists(SPECIAL_FILENAME) == False:
        specials = {
            item : {
                'cost' : cost,
                'amount' : amount
            }
        }

    else:
        with open(SPECIAL_FILENAME, "r") as file:
            specials = json.load(file)

        specials[item] = {
            'cost' : cost,
            'amount' : amount
        }

    with open(SPECIAL_FILENAME, "w") as file:
            json.dump(specials, file, indent=4)

    MENU_FILENAME = os.path.join(current_dir, 'docs', 'menu.json')
    menu = {
        'items' : items,
        'specials' : specials
    }

    with open(MENU_FILENAME, "w") as file:
        json.dump(menu, file, indent=4)
    

if __name__ == '__main__':
    main()

