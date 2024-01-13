import requests
import csv

baseurl = "https://app.rackbeat.com/api"
url = "https://app.rackbeat.com/api/inventory-movements"

headers = {
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIzIiwianRpIjoiNzNjYjhkNDhiNzcxODczMTc3MTc1MjkxZGQ0NTVkYjE2M2QzN2M4MTZmYTIyY2JlM2Q1ZGJmM2M4ZjM3MTY4NWM4YWZlODA1YmQ2Njk2YjIiLCJpYXQiOjE3MDQ4MTgzNDEuNTE1ODIxLCJuYmYiOjE3MDQ4MTgzNDEuNTE1ODI0LCJleHAiOjIwMjA0Mzc1NDEuNTA3MSwic3ViIjoiMjA4MTAiLCJzY29wZXMiOltdfQ.XKQOLLW-D4UvmAjthkXoHzrp02pqHuFLkFVNwb3XcbNrKoqjJno16v9OMaKFqi_D4Pd3Q20xORQDlm2fYjWSSlb47yuxCCPwZtlJss85NtnmThWM9uk7tKcZ8gbPF1E8MuRgUNiFi8UBhBw0FFFQ7xShul5QiYNOYCsmetszLRebpaWv9o8vOaOnkEOVC8_gsY7EL2RpiruOcuykKXi-zSd6IXGhLInc7IsiUDc834NSp_8OL9U9QmQFN_tYUE_0vjX3UPKL6u6PCyTyP3JIhkk6hgBPNYDjSx7iXT21rNT-23DQ4ZgHJlt405GFGsf8d70f1KZCncKyG3DhFboO75733uYLxOYPvqoufCGxkannnogybh5lgsYiJM3aTNM4bhgH63cC7ACVtrHDAJHb0OJlE9CWfQ-BI2341m-mYg-wJoLJewHhQcwE0yS9kpnZCiGIo8ffcDz7QppRxAQc8s-BUpiPT1pCgYii9a4jRqvrqSR9ToxHOqdGtY5e5c6VvuZ5SwRW5T5Hc3JSLir_08SpfvKqYyeEH_JOQvUryKZZn-ajOIRGXsIFFgndHPMOAhQWfEdVMo9wTfJJqWWP4TLSaBFDrESHRh4Q84gZInoWPVz62uchvbdrM8fxBVeGzeLfHpxEt2KBPbCcwGIuDbqO8dpf69pQ6FfEreJvrtI'
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
        print("✅ Iterating over movement IDs and booking.")

        with open('movement_ids.csv', 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)  # Skip the header

            for row in csv_reader:
                movement_id = row[0]
                book_url = f"{baseurl}/inventory-adjustments/{movement_id}/book"
                print(f"📚 {book_url}")

                response = requests.post(book_url, headers=headers)

                if response.status_code == 200:
                    print(f"✅ Successfully booked movement {movement_id}")
                else:
                    print(f"❌ Failed to book movement {movement_id}. Status code: {response.status_code}")

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
                book_url = f"{baseurl}/inventory-adjustments/{movement_id}/book"
                print(f"📚 {book_url}")

                response = requests.post(book_url, headers=headers)

                if response.status_code == 200:
                    print(f"✅ Successfully booked movement {movement_id}")
                else:
                    print(f"❌ Failed to book movement {movement_id}. Status code: {response.status_code}")

    except Exception as e:
        print(f"❌ An error occurred: {str(e)}")

iterate_and_book_movements(baseurl, headers)

if __name__ == '__main__':
    bulk_book_internal_movements(baseurl, url, headers)
    iterate_and_book_movements(baseurl, headers)