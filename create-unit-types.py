# create_unit_types.py
from utils.api_utils import send_request

def gather_user_input():
    unit_name = input("Unit name: ")
    unit_id = input("Unit number: ")
    return unit_id, unit_name

def create_unit(unit_id, unit_name):
    endpoint = "units"
    payload = {
        "number": unit_id,
        "name": unit_name
    }
    try:
        response = send_request(endpoint, 'POST', payload)
        print("Unit created successfully.")
    except requests.HTTPError:
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