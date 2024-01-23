import requests
import csv

url = "https://app.rackbeat.com/api/inventory-movements"

headers = {
  'Authorization': 'Bearer '
}

def bulk_book_internal_movements(url, headers):
    try:
        # Open the CSV file outside the loop
        with open('movement_ids.csv', 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['Movement ID'])  # Write the header

            page = 1
            while True:
                response = requests.get(url, headers=headers, params={'page': page})

                if response.status_code == 206:
                    data = response.json()

                    # Write the movement IDs to the CSV file
                    for movement in data.get('inventory_regulations', []):
                        movement_id = movement.get('id')
                        csv_writer.writerow([movement_id])

                    # Check if there are more pages
                    if page >= data.get('pages'):  
                        break

                    # Go to the next page
                    print(f"✅ Done parsing {page}. Going to page {page + 1}")
                    page += 1

                else:
                    print(f"❌ Error in API call. Status code: {response.status_code}")
                    print(response.text)
                    break

        print("✅ CSV file has been created with movement IDs.")
    except Exception as e:
        print(f"❌ An error occurred: {str(e)}")

    print("✅ CSV file has been created with movement IDs.")

def iterate_and_book_movements(baseurl, headers):
    try:
        with open('movement_ids.csv', 'r') as csvfile:
            print("✅ Iterating over movement IDs and booking.")
            csv_reader = csv.reader(csvfile)
            next(csv_reader)  # Skip the header

            for row in csv_reader:
                movement_id = row[0]
                book_url = f"{url}/{movement_id}/book"
                print(f"📚 {book_url}")

                response = requests.post(book_url, headers=headers)

                if response.status_code == 200:
                    print(f"✅ Successfully booked movement {movement_id}")
                else:
                    print(f"❌ Failed to book movement {movement_id}. Status code: {response.status_code}")

    except Exception as e:
        print(f"❌ An error occurred: {str(e)}")

if __name__ == '__main__':
    bulk_book_internal_movements(url, headers)
    iterate_and_book_movements(url, headers)

