import re

# Read the contents of the .md file
with open("airsoft.md", "r") as file:
    content = file.read()

# Define a regex pattern to match the invoice number
invoice_pattern = r"customer_invoice_key-(\d+)"

# Define a regex pattern to match the product error message
product_pattern = r"Product '([^']*)' is barred."

# Find all matches for invoice numbers and product error messages
invoices = re.findall(invoice_pattern, content)
products = re.findall(product_pattern, content)

# Combine the results into a list of tuples
result = list(zip(invoices, products))

# Write the results to a new file
output_filename = "airsoft_parsed.md"
with open(output_filename, "w") as output_file:
    for invoice, product in result:
        output_file.write(f"Invoice: {invoice}\n")
        output_file.write(f"Product Error: {product}\n\n")

print(f"Results have been saved to {output_filename}")
