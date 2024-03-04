from utils.api_utils import send_request
import sys

# Get passed invoice number
invoice_number = str(sys.argv[1])

# Call API to get invoice details
invoice_details = send_request("get", "/invoices" + invoice_number)

# Check if invoice has been returned to stock
if invoice_details["stock_returned"]:
    print("Invoice has been returned to stock")
else:
    print("Invoice has not been returned to stock")invoice_number = input("Enter invoice number: ")
