from utils.api_utils import send_request, process_csv

discount_group_ids = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
discounts = [ '25', '0', '0', '25', '25', '16', '15', '30', '20', '20', '20', '20']

# Purge existing discount groups


def update_customer_discount_groups(number=None):
    customer = number[0]
    print(f"Processing customer {customer} 🔎")
    for discount_group in discount_group_ids:
        endpoint = f"customers/{customer}/discount-groups/{discount_group}"
        # Update the customer discount group
        response = send_request(endpoint, 'POST')
        if response.status_code == 403:
            print(f"ℹ️ already part of discount group {discount_group} - skipping")
            print(response.text)
            pass
        elif response.status_code == 404:
            print(f"❌ customer {customer} not found")
            # break out of the function
            return
        elif response.status_code != 200:
            print(f"❌ Failed to add customer {customer} to discount group {discount_group}: {response.status_code}")
            print(response.text)
            pass
        else:
            print(f"✅ discount group added {discount_group}")
        
        # Set the discount percentage for this discount group
        group = int(discount_group)
        percentage = int(discounts[group - 1])
        payload = {
            "override_discount_percentage": percentage
        }
        update_endpoint = f"customers/{customer}/discount-groups/{discount_group}"  # Define endpoint here
        update = send_request(update_endpoint, 'PUT', data=payload)  # Use correct endpoint
        if update.status_code != 200:
            print(f"❌ Failed to update customer {customer} discount group {discount_group} discount percentage to {percentage}")
            print(update.text)
            pass
        else:
            print(f"✅ discount group {discount_group} percentage set to: {percentage}")
        print("")
    print("")

if __name__ == '__main__':
    # process the csv file, pass the function to be called. In process_csv the 
    process_csv(update_customer_discount_groups)