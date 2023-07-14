import requests
import os
from dotenv import load_dotenv

load_dotenv()

ERRS = 0
FAILURES = []
SUCCESSES = 0

# Set your bearer token
bearer_token = os.getenv("BEARER_TOKEN")

# Prompt user for input
print("UNBOOK INVOICE")
print("")
print("Disclaimer: This action will unbook an invoice, which at best is questionable legal. Please make sure you know what you're doing!!")
invoice_number = input("Input the invoice number you want to unbook: ")
