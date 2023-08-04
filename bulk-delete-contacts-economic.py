import requests
import json
import csv
import time

base_url = "https://restapi.e-conomic.com"
url_template = "https://restapi.e-conomic.com/customers/{CUSTOMER_NUMBER}/contacts/{CONTACT_NUMBER}"

err = 0
success = 0 
failed_customers = []
 
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'X-AppSecretToken': '', # change me
    'X-AgreementGrantToken': '' # change me
}

def make_api_call(customer_number, contact_number):
    url = url_template.replace("{CUSTOMER_NUMBER}", str(customer_number)).replace("{CONTACT_NUMBER}", str(contact_number))
    response = requests.delete(url, headers=headers)
    return response

def main():
    global err, success, failed_customers
    csv_file_path = 'Contact.csv' 

    with open(csv_file_path, 'r', newline='') as csv_file: 
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        for row in csv_reader:
            customer_number = row['CustomerNo']
            contact_number = row['ContactNo']
            response = make_api_call(customer_number, contact_number)
            if response.status_code == 204:
                print(f"Deleted contact {contact_number} on customer {customer_number}")
                success += 1
            else:
                print(f"Failed to delete contact {contact_number} for customer {customer_number}. Status code: {response.status_code}")
                err += 1
                failed_customers.append(customer_number)
            time.sleep(0.150)  # Sleep a bit to avoid hitting the rate limit (5.something requests per second ~=300req/min)

if __name__ == "__main__":
    main()