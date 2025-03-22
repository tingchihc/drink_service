FROM python:3.9-slim

WORKDIR /app
COPY . /app


CMD ["python", "scripts/items_setup.py", "--add", "True", "--product", "milk", "--cost", "20"]
CMD ["python", "scripts/items_setup.py", "--add", "True", "--product", "tea", "--cost", "50"]
CMD ["python", "scripts/items_setup.py", "--add", "True", "--product", "bubble_tea", "--cost", "60"]
CMD ["python", "scripts/items_setup.py", "--update", "True", "--product", "tea", "--cost", "40"]
CMD ["python", "scripts/items_setup.py", "--update", "True", "--product", "green_tea", "--cost", "70"]
CMD ["python", "scripts/items_setup.py", "--remove", "True", "--product", "milk"]
CMD ["python", "scripts/items_setup.py", "--remove", "True", "--product", "black_tea"]


CMD ["python", "scripts/special_setup.py", "--item", "green_tea", "--amount", "5", "--cost", "330"]
CMD ["python", "scripts/special_setup.py", "--item", "tea", "--amount", "4", "--cost", "150"]
CMD ["python", "scripts/special_setup.py", "--item", "bubble_tea", "--amount", "3", "--cost", "150"]
