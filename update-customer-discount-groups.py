from utils.api_utils import send_request, process_csv, delete_request

discount_group_ids = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
discounts = [ '25', '0', '0', '25', '25', '16', '15', '30', '20', '20', '20', '20']

# Purge existing discount groups
def purge_current_discount_groups(number=None):
    customer = number[0]
    print(f"🔎 Processing customer {customer}")
    endpoint = f"customers/{customer}/discount-groups"
    response = send_request(endpoint)
    for discount_group in response.json()['customer_discount_groups']:
        number = discount_group['number']
        if number not in discount_group_ids:
            name = discount_group['name']
            group = f"customers/{customer}/discount-groups/{number}"
            response = delete_request(group)
            if response.status_code != 200:
                print(f"❌ Failed to remove discount group {name} from customer {customer}", response.status_code)
                pass
            print(f"✅ discount group {name} removed")

def update_customer_discount_groups(number=None):
    customer = number[0]
    print(f"Processing customer {customer} 🔎")
    for discount_group in discount_group_ids: 
        endpoint = f"customers/{customer}/discount-groups/{discount_group}"
        response = send_request(endpoint, 'POST')
        if response.status_code == 403:
            print(f"ℹ️  already part of discount group {discount_group} - skipping")
            print(response.text)
            pass
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
        update = send_request(endpoint, 'PUT', data=payload)  # Use correct endpoint
        if update.status_code != 200:
            print(f"❌ Failed to update customer {customer} discount group {discount_group} discount percentage to {percentage}")
            print(update.text)
            pass
        else:
            print(f"✅ discount group {discount_group} percentage set to: {percentage}")
        print("")
    print("")

if __name__ == '__main__':
#    process_csv(purge_current_discount_groups)
    process_csv(update_customer_discount_groups)
