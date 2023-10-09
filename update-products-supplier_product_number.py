import csv
import requests
import sys
import os
from dotenv import load_dotenv

load_dotenv()

BEARER_TOKEN = os.getenv("BEARER_TOKEN")

errors = 0
successes = 0
failers = []


# Save results as log file
def log_results():
    global errors, successes, failers
    with open("update-products-log.txt", "w") as f:
        f.write("Errors: " + str(errors) + "\n")
        f.write("Successes: " + str(successes) + "\n")
        f.write("Failers: " + str(failers) + "\n")

def create_product(row):
    global errors, successes, failers
    url = "https://app.rackbeat.com/api/products/" + row.get("number")
    payload = {
        "number": row.get("number"),
        "group": row.get("group")
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
        failers.append(row.get("number"))


# Get the CSV file path from the command line argument
csv_file = os.getenv("IMPORT_FILE")

# Define the required fields in the CSV
required_fields = ["number"]

# Iterate through the CSV file
with open(csv_file, "r", newline="") as file:
    csv_reader = csv.DictReader(file, delimiter=";")
    for row in csv_reader:
        # Check if the essential fields have non-empty values
        if (
            row.get("number")
        ):
            create_product(row)
        else:
            print("Skipping row: Number is required")
            print("-----------------------------------")

print("")
print("Update of products supplier complete!")
print("Total products updated: " + str(successes))
print("Total products failed: " + str(errors))
print("Failed products: " + str(failers))
print("")