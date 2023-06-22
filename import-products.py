import csv
import requests
import sys

# Api key "August"
BEARER_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIzIiwianRpIjoiYTI2YjI0ODZlOWE0YjVjNzZlMThiNWM1MzM4NjIwYzQ1NzI5MWNiNDNlOWE4MDQ5ZTc1ZjMxMjEzYjYwYzM2YjM5OGY1Mjg4ZTU4MzA1ZDYiLCJpYXQiOjE2ODcyODUwNDMuNDcxNDIzLCJuYmYiOjE2ODcyODUwNDMuNDcxNDI3LCJleHAiOjIwMDI5MDQyNDMuNDU0NDgxLCJzdWIiOiIxNTM1NSIsInNjb3BlcyI6W119.To_srQ0jlDVrV0ZoyHxOuF5reGcu2dOAAVQWlxGBxfLnTzEJYZJk6HspQ4jBdvdnsqFA8gj9cwNzyBkl_DQ0pabrnuqQt9ylUqsWqn4WhYeNJa1L0zpogLQazG-2AeCfljSjN7hBR-SZnjrV4fN9fpBn-7mjhGHNP82dfQ02EN07rYjfPcfB-dDN-1PAMXh088qRSrx92vqs8hHIf8BOsN9DCvaUN3Sd5AVYPjLZY5QfJOzE1xLPO9zJwiV_R4b9mf6EJl_yaiBDfD1vZ2u7_VgE_IbHv5HEn88wx4-zTSCqUGY7SXHt11T8BZwPexjbqp8N1xRajvgeKjWLdXlYN0lJYc9D0kk6TgiJ7gZqthxl1n76FgkNpAQM89sg5GC6VeWQyLDKuLqZxCEnVQgONfvrjZ7bmudhMZluyPndYkjBtOiYj3VOncxP2Ft5qsd22dT5RQOCxmBPW67eSDJ4uK5cbsBlqP2Jr6xrhBJWHtiyTlmcvCAWfUkGHFt4GRNj6jH_wnvPZ_pNxikBur8qkxZ1cqDW3uchbS86_p4rK5xvLmhS1QgaFGamB0t_tOvBMkiCLbpVb5caIE8nYs_1USXLwEzAF_E6WfSOw5A-XdEUWRmeKlKU1dCg-2l_8YfeZOJgecwmk6CHGmv1p0UHJlE8CUGGdS0esYu7l7YV9JE"


def create_product(row):
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
    }
    headers = {
        "Authorization": "Bearer " + BEARER_TOKEN,
        "Content-Type": "application/json",
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 20:
        print("Successfully created product: " + row.get("number"))
        print("-----------------------------------")
    else:
        print("Failed to create product: " + row.get("number"))
        print("Error message:", response.text)
        print("-----------------------------------")


# Check if the CSV file path argument is provided
if len(sys.argv) < 2:
    print("Please provide the path to the CSV file as an argument.")
    sys.exit(1)

# Get the CSV file path from the command line argument
csv_file = sys.argv[1]

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
