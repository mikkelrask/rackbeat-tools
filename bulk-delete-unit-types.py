from utils.api_utils import send_request, delete_request
import requests

min_unit_id = 12


def list_unit_types():
    endpoint = "units"
    try:
        response = send_request(endpoint, 'GET')
        print("Unit types:")
        print(response.json())
        for unit in response.json()['units']:
            if unit['number'] > min_unit_id:
                deleteUnitID(unit['number'])
            else:
                print(unit['name'] + " (" + str(unit['number']) + ") skipped.")
    except requests.HTTPError:
        print("Failed to list unit types.")
        print("Status Code:", response.status_code)
        print("Response:", response.text)

def deleteUnitID(id):
    endpoint = "units/" + str(id)
    try:
        response = delete_request(endpoint)
        print("Unit " + str(id) + " deleted successfully.")
    except requests.HTTPError:
        print("Failed to delete unit " + id + ".")
        print("Status Code:", response.status_code)
        print("Response:", response.text)

if __name__ == "__main__":
    iterations = 0
    max_iterations = 70
    for i in range(max_iterations):
        while iterations < max_iterations:
            list_unit_types()
            iterations += 1
            print("Page " + str(iterations))