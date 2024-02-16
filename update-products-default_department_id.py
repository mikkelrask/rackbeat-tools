import os
import sys
from utils.api_utils import process_csv, print_results, send_request, FILE_PATH


BEARER_TOKEN = os.getenv("BEARER_TOKEN")
STATUS_CODES = {
    404: "Product was not found. Please check the product exists.",
    422: "Product could not be updated. Please check the department_id is valid.",
}

def update_product(row):
    global FILE_PATH
    if len(row) < 2:
        print(f"CSV file {FILE_PATH} does not have the nessecary rows (number;department_id).")
        exit()

    url = "https://app.rackbeat.com/api/products/" + f'{row[0]}'
    payload = {
        "number": f'{row[0]}',
        "department_id": f'{row[1]}'
    }
    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}",
        "Content-Type": "application/json",
    }
    endpoint = f'products/{row[0]}'
    response = send_request(endpoint, 'PUT', headers=headers, data=payload)
    if response.status_code == 200:
        print(f"Updated product {row[0]}'s default department ID: {row[1]}")
    else:
        message = STATUS_CODES.get(response.status_code, "Product {0} could not be updated. Error: {1}")
        print(message.format(row[0], response.status_code))

    return response

# function that performs a GET to /self
def verify_agreement_number(api_key):
    endpoint = "self"
    headers = {
    'Authorization': f'Bearer {api_key}'
    }

    response = send_request(endpoint, headers=headers)
    agreement_number = response.json()['user_account']['id']
    if response.status_code != 200:
        print("Failed to verify agreement number")
        print("Error message:", response.text)
        return
    print("✅ Agreement number: ", agreement_number)
    correct = input("Is this the correct agreement number? (y/n) ")
    if correct.lower() != 'y':
        sys.exit("Ret venligst .env filen, med den korrekte API nøgle!")
    else:
        return agreement_number



if __name__ == "__main__":
    verify_agreement_number(BEARER_TOKEN)
    process_csv(update_product)
    print_results()
