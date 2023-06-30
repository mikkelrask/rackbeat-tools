import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def gather_user_input():
    unit_id = input("Unit ID: ")
    unit_name = input("Unit name: ")
    return unit_id, unit_name

def create_unit(unit_id, unit_name):
    url = "https://app.rackbeat.com/api/units"

    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {os.getenv('BEARER_TOKEN')}",
        "Content-Type": "application/json"
    }

    payload = {
        "id": unit_id,
        "name": unit_name
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 201:
        print("Unit created successfully.")
    else:
        print("Failed to create unit.")
        print("Status Code:", response.status_code)
        print("Response:", response.text)

# Main loop
while True:
    # Gather user input
    unit_id, unit_name = gather_user_input()

    # Create unit
    create_unit(unit_id, unit_name)

    # Prompt if the user wants to create another unit
    create_more = input("Create another unit? (y/n): ")
    if create_more.lower() != "y":
        break
