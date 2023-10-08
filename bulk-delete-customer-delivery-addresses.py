# through our API we find the IDs of the delivery addresses that we want to delete
# store them in a list
# and make a call to the API to delete them

import requests
import json
import csv
import time
import os
from dotenv import load_dotenv

err = 0
success = 0
noaction = 0
failers = []

# API credentials
load_dotenv()
API_KEY = os.getenv("BEARER_TOKEN")
CSV_FILE = os.getenv("IMPORT_FILE")
baseurl = "https://app.rackbeat.com/api/"


def deleteAddress(number, id):
    global err, success, failers, baseurl, API_KEY
    url = baseurl + "customers/" + str(number) + "/addresses/" + str(id)
    headers = {
        "Authorization": "Bearer " + API_KEY,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    response = requests.delete(url, headers=headers)
    if response.status_code == 200:
        print("Deleted address: " + str(id))
        print("-----------------------")
        success = success + 1
    else:
        print("Failed to delete: " + id)
        print("Error message:", response.text)
        print("-----------------------")
        err = err + 1
        failers.append(id)


def getAddresses(number):
    global err, success, failers, noaction, baseurl, API_KEY
    url = baseurl + "customers/" + str(number) + "/addresses"
    headers = {
        "Authorization": "Bearer " + API_KEY,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    print("Getting addresses for: " + number)
    response = requests.get(url, headers=headers)

    if response.status_code == 206:
        response_data = response.json()
        if response_data["total"] > 0:
            for address in response_data["addresses"]:
                # check if type is delivery
                if address["type"] != "delivery":
                    print(
                        "Deleting delivery address "
                        + str(address["id"])
                        + " for customer "
                        + str(number)
                    )
                    deleteAddress(number, address["id"])
                    success = success + 1
                else:
                    print(address["id"] + " is not a delivery address - skipping")
                    print("-----------------------")
                    noaction = noaction + 1
        else:
            print("No addresses found.")
            print("-----------------------")
            noaction = noaction + 1
    else:
        print("Failed to get addresses for: " + str(number))
        print("Error message:", response.text)
        print("-----------------------")
        err = err + 1
        failers.append(number)


if __name__ == "__main__":
    with open(CSV_FILE, "r", newline="") as file:
        csv_reader = csv.DictReader(file, delimiter=";")
        for row in csv_reader:
            if row.get("number"):
                getAddresses(row.get("number"))

    print("Done!")
    print("Errors: " + str(err))
    print("Successes: " + str(success))
    print("No action: " + str(noaction))
    print("Failers: " + str(failers))
