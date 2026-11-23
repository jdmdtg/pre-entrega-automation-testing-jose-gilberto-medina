import csv
import json

def read_login_csv():
    with open("data/login.csv",newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)

def read_productos_json():
    with open("data/products.json") as file:
        return json.load(file)

