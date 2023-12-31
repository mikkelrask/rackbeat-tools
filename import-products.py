import csv
import requests
import sys
import os
import time
from dotenv import load_dotenv

load_dotenv()

BEARER_TOKEN = os.getenv("BEARER_TOKEN")
errors = 0
successes = 0

def create_product(row):
    global errors, successes
    url = "https://app.rackbeat.com/api/products/"
    payload = {
        "number": row.get("number"),
        "group": row.get("group"),
        "name": row.get("name"),
        "sales_price": row.get("sales_price"),
        "recommended_cost_price": row.get("suggested_cost_price"),
        "extra_cost": row.get("extra_cost"),
        "unit_id": row.get("unit_id"),
        "stock_quantity": row.get("stock_quantity"),
        "description": row.get("description"),
        "min_inventory_quantity": row.get("min_inventory_quantity"),
        "min_sales_quantity": row.get("min_sales_quantity"),
        "min_purchase_quantity": row.get("min_purchase_quantity"),
        "barcode": row.get("barcode"),
        "default_location_id": row.get("default_location_id"),
        "variation_id": row.get("variation_id"),
        "physical": {
            "weight": row.get("weight"),
            "weight_unit": row.get("weight_unit"),
            "width": row.get("width"),
            "height": row.get("height"),
            "depth": row.get("depth"),
            "size_unit": row.get("size_unit"),
        },
        "supplier_product_number": row.get("supplier_product_number"),
        "is_barred": row.get("is_barred"),
        "discount_group": row.get("discount_group"),
        "image_url": row.get("image_url"),
        "default_supplier_id": row.get("default_supplier_id")
    }
    headers = {
        "Authorization": "Bearer " + BEARER_TOKEN,
        "Content-Type": "application/json",
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 201:
        print("Successfully created product: " + row.get("number"))
        print("-----------------------------------")
        successes = successes + 1
    else:
        print("Failed to create product: " + row.get("number"))
        print("Error message:", response.text)
        print("-----------------------------------")
        errors = errors + 1

# Get the CSV file path from the command line argument
csv_file = os.getenv("IMPORT_FILE")

# Define the required fields in the CSV
required_fields = ["number", "group", "name", "sales_price"]

# Iterate through the CSV file
with open(csv_file, "r", newline="") as file:
    csv_reader = csv.DictReader(file, delimiter=";")
    for row in csv_reader:
        # Check if the essential fields have non-empty values
        if all(row.get(field) for field in required_fields):
            create_product(row)
            time.sleep(0.125)  # Pause for 0.125 seconds (1/8th of a second) between requests
        else:
            print("Skipping row: Missing 1 or more required fields (number, group, name, sales_price)")
            print("-----------------------------------")

print("")
print("Import of product complete! Here's how it went:")
print("Total products imported: " + str(successes))
print("Total products failed: " + str(errors))
print("")
