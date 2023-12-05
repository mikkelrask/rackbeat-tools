import os
from dotenv import load_dotenv
from utils.api_utils import process_csv, print_results, send_request, FILE_PATH

load_dotenv()

BEARER_TOKEN = os.getenv("BEARER_TOKEN")
STATUS_CODES = {
    404: "Product {0} was not found. Please check the product exists.",
    422: "Product {0} could not be updated. Please check the department_id is valid.",
}

def update_product(row):
    global FILE_PATH
    if len(row) < 2:
        print(f"CSV file {FILE_PATH} does not have the nessecary rows (number;department_id).")
        exit()

    url = "https://app.rackbeat.com/api/products/" + row[0]
    payload = {
        "number": row[0],
        "department_id": row[1]
    }
    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}",
        "Content-Type": "application/json",
    }
    response = send_request(url, 'PUT', headers, payload)
    if response.status_code == 200:
        print(f"Updated product {row[0]}'s default department ID: {row[1]}")
    else:
        message = STATUS_CODES.get(response.status_code, "Product {0} could not be updated. Error: {1}")
        print(message.format(row[0], response.status_code))

    return response

if __name__ == "__main__":
    process_csv(update_product)
    print_results()