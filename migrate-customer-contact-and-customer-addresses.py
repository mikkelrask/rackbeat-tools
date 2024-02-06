from utils.api_utils import send_request
from dotenv import load_dotenv

from_api_key = ""
to_api_key = ""
option = ""
customer_numbers = []
contacts = []
from_agreement = ""
to_agreement = ""


# function to prompt the user for input for the api key, for the from agreement
def get_api_key_from():
    global from_api_key, from_agreement
    #from_api_key = input("Enter the API key for the 'from' agreement: ")
    print("-----------------------------------")
    return from_api_key

# make a GET to /self to verify the agreement number, that the API key belongs to
def verify_agreement_number(api_key):
    endpoint = "self"
    headers = {
    'Authorization': f'Bearer {api_key}'
    }

    response = send_request(endpoint, headers=headers)
    agreement_number = response.json()['user_account']['id']
    if response.status_code != 200:
        print("Failed to verify agreement number")
        print("Error message:", response.text)
        return
    print("✅ Agreement number: ", agreement_number)
    return agreement_number

# function to prompt the user for input for the api key, for the to agreement
def get_api_key_to():
    global to_api_key, to_agreement
    to_api_key = input("Enter the API key for the 'to' agreement: ")
    print("-----------------------------------")
    return to_api_key

# function that prompt the user, if they want to migrate the customer contact and customer addresses or both
def get_migration_option():
    global option
    print("get options-----------------------------------")
    print("What would you like to migrate?")
    print("1. Customer Contact")
    print("2. Customer Addresses")
    print("3. Both")
    option = input("Enter the number of the option you would like to choose: ")
    return option

# function that makes a GET to /customers to get the customer ids
def get_customer_ids():
    global from_api_key, from_agreement, customer_numbers
    print("get IDS-----------------------------------")
    endpoint = "customers"
    payload = {}
    files={}
    headers = {
    'Authorization': f'Bearer {from_api_key}'
    }
    response = send_request(endpoint,headers=headers, data=payload)
    limit = response.json()['limit']
    total = response.json()['total']
    # make a new call to /customers to get the customer ids at once
    if limit >= 20:
        endpoint = "customers?fields=number&limit=" + str(total)
        response = send_request(endpoint,headers=headers, data=payload)
        customers = response.json()['customers']
        response_code = response.status_code
        if response_code == 206:
            print("✅ Customer numbers are fetched from ", verify_agreement_number(from_api_key))
            print("-----------------------------------")
            # populate the customer_numbers list with the customer ids
            for customer in customers:
                customer_numbers.append(customers)
                return customer_numbers
        else:
            print("❌ Error")
            print("Error message:", response.json)
            print("-----------------------------------")
            return
    else:
        print("✅ Customer numbers are fetched from ", from_agreement)
        print("-----------------------------------")
        # populate the customer_numbers list with the customer ids
        for customer in response.json()['customers']:
            customer_numbers.append(customer['number'])
    return customer_numbers

# function that makes a GET to /customers/{id}/contacts to get the customer contacts
def get_customer_contacts(customer_number):
    print("Getting contacts for customer: ", customer_number['number'])
    global from_api_key, to_api_key, contacts
    endpoint = "customers/" + str(customer_number['number']) + "/contacts"
    headers = {
        'Authorization': f'Bearer {from_api_key}'
    }
    response = send_request(endpoint, 'GET', headers=headers)
    if response.status_code == 206:
        r = response.json()
        if 'customer_contacts' in r:
            endpoint = "customers/" + str(customer_number['number']) + "/contacts"
            for contact in r['customer_contacts']:
                number = contact['number']
                name = contact['name']
                role = contact['role']
                initials = contact['initials']
                contact_email = contact['contact_email']
                contact_phone = contact['contact_phone']
                cc_order = contact['cc_order']
                cc_offer = contact['cc_offer']
                cc_invoice = contact['cc_invoice']
                cc_delivery_note = contact['cc_delivery_note']
                headers = {
                    'Authorization': f'Bearer {to_api_key}'
                }
                payload =  {
                    "number": number,
                    "name": name,
                    "role": role,
                    "initials": initials,
                    "contact_email": contact_email,
                    "contact_phone": contact_phone,
                    "cc_order": cc_order,
                    "cc_offer": cc_offer,
                    "cc_invoice": cc_invoice,
                    "cc_delivery_note": cc_delivery_note
                }
                print("updating contact: ", contact['name'])
                create_customer_contacts(int(customer_number['number']), payload)
        else:
            print("❌ Failed to fetch customer contacts")
        return contacts

# function that makes a GET to /customers/{id}/addresses to get the customer addresses should be basically the same as the get_customer_contacts function

def get_customer_addresses(number):
    global from_api_key, customer_numbers
    addresses = []
    endpoint = "customers/" + str(number)
    headers = {
    'Authorization': f'Bearer {from_api_key}'
    }
    r = send_request(endpoint, headers=headers).json()
    for address in r['addresses']:
        addresses.append(address)
    
    return addresses

# function that makes a POST to /customers/{id}/contacts to create the customer contacts
def create_customer_contacts(number, payload):
    global to_api_key, to_agreement
    to_agreement = verify_agreement_number(to_api_key)
    endpoint = "customers/" + str(number) + "/contacts"
    headers = {
        'Authorization': f'Bearer {to_api_key}'
    }
    response = send_request(endpoint, 'POST', headers=headers, data=payload)
    if response.status_code == 201:
        print("✅ " + str(number) + " was created on " + str(number) + " on agreement " + to_agreement)
        print("-----------------------------------")
        return
    else:
        print("❌ Failed to create customer contacts")
        print("Error message:", response.json())
        print("-----------------------------------")
        return
    
# function that makes a POST to /customers/{id}/addresses to create the customer addresses
def create_customer_addresses(number, addresses):
    global to_api_key, customer_numbers
    endpoint = "customers/" + str(number) + "/addresses"
    payload = { }
    headers = {
    'Authorization': f'Bearer {to_api_key}'
    }
    response = send_request(endpoint, 'POST', headers, payload)
    if response.status_code == 201:
        print("✅ Successfully created customer addresses on customer " + str(number))
        print("-----------------------------------")
        return
    else:
        print("❌ Failed to create customer addresses")
        print("Error message:", response.json())
        print("-----------------------------------")
        return

if __name__ == "__main__":
    get_api_key_from()
    verify_agreement_number(from_api_key)
    get_customer_ids()
    for customer in customer_numbers[0]:
        get_customer_contacts(customer)
        #get_customer_addresses(customer)
        #create_customer_contacts(customer, contacts)
    # print the customer number values, not the key, only the values
    # print(customer_numbers)
    # for customer in customer_numbers:
    #     contacts = get_customer_contacts(customer)
    #     create_customer_contacts(customer, contacts)
    #     addresses = get_customer_addresses(customer)
    #     create_customer_addresses(customer, addresses)

# option = get_migration_option()
    # if option == "1":
    #     print("You chose to migrate customer contacts")
    #     get_customer_ids(from_api_key)
    #print("ij")