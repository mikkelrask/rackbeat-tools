# this script will gather a list of all available BOMs, and set the checkmark for "Adjust negative lines to 0" for each.
# It will first generate an CSV file with the product number for all BOMs, and iterate through that list to set the value.

from utils.api_utils import send_request, print_results
import time
import csv


headers = {
    'Authorization': f'Bearer {BEARER_TOKEN}', # insert your bearer token here, omitting the brackets
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}


def get_all_boms():
    global headers
    print('Gathering all BOMs...')
    endpoint = "lots"
    response_json = send_request(endpoint, 'GET', headers=headers).json()
    lots = response_json.get('lots', [])
    pages = response_json.get('pages', 1)
    
    with open('boms.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['number'])
        
        for page in range(1, pages + 1):
            print(f'Gathering page {page} of {pages}...')
            response_json = send_request(endpoint, 'GET', headers=headers, data={'page': page}).json()
            lots = response_json.get('lots', [])
            
            for lot in lots:
                number = lot.get('number')
                writer.writerow([number])
    
    print(f'Done. Written to boms.csv')

def set_adjust_negative_lines_to_0():
    global headers
    print('Setting adjust negative lines to 0 as \'true\'..')
    with open('boms.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            number = row[0]
            endpoint = f"lots/{number}"
            data = {
                'adjust_to_zero': 'true'
            }
            if number == 'number':
                continue
            else:
                response = send_request(endpoint, 'PUT', headers=headers, data=data)

            width = 78  # adjust this to the width of your console
            if response.status_code in range(200, 299):
                print("{:<20} {:>20}".format(number, "✅"))
            else:
                print(f'Error updating BOM {number} - {response.status_code} ❌')
                print(response.status_code, response.text)
            time.sleep(0.5)

if __name__ == '__main__':
    print('Starting to update bill of materials 📦')
    get_all_boms()
    set_adjust_negative_lines_to_0()
    print_results()
