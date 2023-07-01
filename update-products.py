import csv
import requests
import sys
import os
from dotenv import load_dotenv

load_dotenv()

BEARER_TOKEN = os.getenv("BEARER_TOKEN")

errors = 0
successes = 0


def create_product(row):
    global errors, successes
    url = "https://app.rackbeat.com/api/products/" + row.get("number")
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
    }
    headers = {
        "Authorization": "Bearer " + BEARER_TOKEN,
        "Content-Type": "application/json",
    }
    response = requests.put(url, headers=headers, json=payload)
    if response.status_code == 200:
        print("Updated product: " + row.get("number"))
        print("-----------------------")
        successes = successes + 1
    else:
        print("Failed to update: " + row.get("number"))
        print("Error message:", response.text)
        print("-----------------------")
        errors = errors + 1


# Get the CSV file path from the command line argument
csv_file = os.getenv("IMPORT_FILE")

# Define the required fields in the CSV
required_fields = ["number", "group", "name", "sales_price", "unit_id"]

# Iterate through the CSV file
with open(csv_file, "r", newline="") as file:
    csv_reader = csv.DictReader(file, delimiter=";")
    for row in csv_reader:
        # Check if the essential fields have non-empty values
        if (
            row.get("number")
            and row.get("group")
            and row.get("name")
            and row.get("sales_price")
            and row.get("unit_id")
        ):
            create_product(row)
        else:
            print("Skipping row: Missing required fields")
            print("-----------------------------------")

print("")
print("Import of product updates complete!")
print("Total products updated: " + str(successes))
print("Total products failed: " + str(errors))
print("")