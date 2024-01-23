# api_utils.py
import os
import requests
import csv
from dotenv import load_dotenv

load_dotenv()

BEARER_TOKEN = os.environ.get('BEARER_TOKEN')
FILE_PATH = os.environ.get('IMPORT_FILE')

headers = {
    'Authorization': f'Bearer {BEARER_TOKEN}',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

err = 0
success = 0

BASE_URL = "https://app.rackbeat.com/api/"

def send_request(endpoint, method='GET', headers=None, data=None):
    global err, success, BEARER_TOKEN, FILE_PATH
    if headers==None:
        headers = {
            'Authorization': f'Bearer {BEARER_TOKEN}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
    url = BASE_URL + endpoint
    if method == 'POST':
        response = requests.post(url, headers=headers, json=data)
    elif method == 'PUT':
        response = requests.put(url, headers=headers, json=data)
    else:
        response = requests.get(url, headers=headers)

    if response.status_code in range(200, 299):
        success += 1
    else:
        err += 1

    return response

def delete_request(endpoint):
    global err, success, headers
    url = BASE_URL + endpoint
    response = requests.delete(url, headers=headers)

    if response.status_code in range(200, 299):
        success += 1
    else:
        err += 1

    return response

def process_csv(process_function):
    with open(FILE_PATH, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            process_function(row)

def print_results():
    print(f"Successful requests: {success}")
    print(f"Failed requests: {err}")