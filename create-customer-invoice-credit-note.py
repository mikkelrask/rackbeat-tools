import requests
import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

BEARER_TOKEN = os.environ.get('BEARER_TOKEN')

headers = {
    'Authorization': f'Bearer {BEARER_TOKEN}',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}


def sendRequest(customerInvoiceNumber):
    url = f'https://app.rackbeat.com/api/customer-invoices/{customerInvoiceNumber}/create-creditnote'
    print(f'POST\'ing to URL: {url}')
    response = requests.post(url, headers=headers)
    print(response.text.encode('utf8'))


def gatherInvoiceNumber():
    invoiceNumber = input("Please enter the invoice number: ")
    sendRequest(invoiceNumber)


gatherInvoiceNumber()
