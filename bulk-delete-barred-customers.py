from utils.api_utils import (delete_request, print_results, process_csv,
                             send_request)


def check_if_barred(row):
    endpoint = f"customers/{row[0]}?fields=meta,is_barred"
    response = send_request(endpoint)
    barred = response.json()["customer"]["is_barred"]

    if response.status_code == 200:
        if barred == True:
            print(f"☠️⚰️ Customer {row[0]} is outta here - cya!")
            delete_request(endpoint)
        else:
            print(f"🍀 Customer {row[0]} is not barred so they're safe - for now!")
        print("-----------------------")
    else:
        print(f"Failed to get customer {row[0]}")
        print("Status code:", response.status_code)
        print("")


if __name__ == "__main__":
    process_csv(check_if_barred)
    print_results()
