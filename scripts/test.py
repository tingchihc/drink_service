import os

current_dir = os.getcwd()

os.system(f"python {current_dir}/scripts/items_setup.py --add True --product milk --cost 50")
os.system(f"python {current_dir}/scripts/items_setup.py --add True --product tea --cost 20")
os.system(f"python {current_dir}/scripts/items_setup.py --add True --product bubble_tea --cost 60")
os.system(f"python {current_dir}/scripts/items_setup.py --update True --product tea --cost 40")
os.system(f"python {current_dir}/scripts/items_setup.py --update True --product green_tea --cost 70")
os.system(f"python {current_dir}/scripts/items_setup.py --remove True --product milk")
os.system(f"python {current_dir}/scripts/items_setup.py --remove True --product black_tea")

os.system(f"python {current_dir}/scripts/special_setup.py --item green_tea --amount 5 --cost 330")
os.system(f"python {current_dir}/scripts/special_setup.py --item tea --amount 4 --cost 150")
os.system(f"python {current_dir}/scripts/special_setup.py --item bubble_tea --amount 3 --cost 150")


#print(f"python {current_dir}/scripts/items_setup.py --add True --product milk --cost 50")