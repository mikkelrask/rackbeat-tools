import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def gather_user_input():
    group_name = input("Group name: ")
    group_id = input("Group id: ")
    domestic_vat = input("Domestic VAT: ")
    vat_eu = input("VAT EU: ")
    vat_abroad = input("VAT Abroad: ")
    vat_domestic_taxfree = input("VAT Domestic (tax-free): ")
    has_inventory = validate_input("Has inventory (y/n): ", ['y', 'n'])
    products_can_be_sold = validate_input("Products can be sold (y/n): ", ['y', 'n'])
    
    return group_name, group_id, domestic_vat, vat_eu, vat_abroad, vat_domestic_taxfree, has_inventory, products_can_be_sold

def validate_input(prompt, valid_options):
    while True:
        user_input = input(prompt)
        if user_input.lower() in valid_options:
            return user_input.lower()
        else:
            print("Invalid input. Please enter a valid option.")

def create_product_group(group_name, group_id, domestic_vat, vat_eu, vat_abroad, vat_domestic_taxfree, has_inventory, products_can_be_sold):
    url = "https://app.rackbeat.com/api/product-groups"

    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {os.getenv('BEARER_TOKEN')}",
        "Content-Type": "application/json"
    }

    payload = {
        "name": group_name,
        "number": group_id,
        "has_inventory": has_inventory == "y",
        "should_spread_cost": False,
        "vat_domestic": vat_domestic_taxfree,
        "vat_eu": vat_eu,
        "vat_abroad": vat_abroad,
        "is_sellable": products_can_be_sold == "y",
        "vat_domestic_exempt": domestic_vat
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 201:
        print("Product group created successfully.")
    else:
        print("Failed to create product group.")
        print("Status Code:", response.status_code)
        print("Response:", response.text)

# Main loop
while True:
    # Gather user input
    group_name, group_id, domestic_vat, vat_eu, vat_abroad, vat_domestic_taxfree, has_inventory, products_can_be_sold = gather_user_input()

    # Create product group
    create_product_group(group_name, group_id, domestic_vat, vat_eu, vat_abroad, vat_domestic_taxfree, has_inventory, products_can_be_sold)

    # Prompt if user wants to create further groups
    create_more = input("Create another group? (y/n): ")
    if create_more.lower() != "y":
        break
