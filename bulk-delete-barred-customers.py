from utils.api_utils import process_csv, delete_request, send_request, print_results
customers
def check_if_barred(row):
    endpoint = f"customers/{row[0]}"
    response = send_request(endpoint)

    if response.status_code == 200:
        product = response.json()
        if product['customers']['is_barred'] == True:
            print(f"Customer {row[0]} is barred - deleting")
            delete_request(endpoint)
        else:
            print(f"Customer {row[0]} is not barred - skipping")
        print("-----------------------")
    else:
        print(f"Failed to get customers {row[0]}")
        print("Status code:", response.status_code)
        print("-----------------------")

if __name__ == "__main__":
    process_csv(check_if_barred)
    print_results() 
