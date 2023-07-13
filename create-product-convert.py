import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Set your bearer token
bearer_token = os.getenv("BEARER_TOKEN")

# Array of BOMS values
BOMS = ["1", "2", "3"]  # Replace with your actual array values

# API endpoint URL
url = "https://app.rackbeat.com/api/products/{}/convert"

# Iterate over each BOMS value and make the API call
for product_number in BOMS:
    # Create the complete URL with the current product number
    endpoint_url = url.format(product_number)
    
    # Set the headers
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json"
    }
    
    # Make the API call
    response = requests.post(endpoint_url, headers=headers)
    
    # Check the response status code
    if response.status_code == 200:
        print(f"Conversion successful for product number: {product_number}")
    else:
        print(f"Conversion failed for product number: {product_number}")
        print(f"Error message: {response.text}")
