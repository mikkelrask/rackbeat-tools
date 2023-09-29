import requests

baseurl = "https://aqua-rock-flea.rackbeat-testing.link/api"
bearer = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiMGY1ZTVjNjQxZTA5NjMyM2UxZWExOTExZWY5NGU1MTFjMzdlOGJlNTc0YTZiMTY3YTFlNzFjNzIzODVhYWYzOWQxOWMzYmVmMzUzOTU5ZjkiLCJpYXQiOjE2OTU5MTc0NDkuMjA4MDQ4LCJuYmYiOjE2OTU5MTc0NDkuMjA4MDUzLCJleHAiOjIwMTE1MzY2NDkuMTkwOTI1LCJzdWIiOiIxIiwic2NvcGVzIjpbXX0.BLchDfN-BkTkNsgBzYi7SmuvHaWa-iiWcbREI6gqtbQL0CIKubyy1-6xF3vXZ1aenNzcJ2OmTqgNrd3iPHmSt2_Ek7nVNiugnGklEJzo6F-b9VvhrgfJ--Oo7bWVzpMaxARXqJNqk0K2m5inFj69Rd_8kLYbnentFRhrOeYn-i8R9aKveiNY0gRgeIMvgyicdLV7G8RJHQiiZydOOfaRD5uVZH_eWivOQ-L-vVWaDHK2dHnCscCB3ury35G12GsDGJxj9WDw7kXzZ6dPjcDM0SGM3XbbRDH0Ce_nFkosxbGkSqkS-Mp_6oIv3-tWufO4Z8MHWe_WpbToXux4P1neuUSZkfw95RqKYPYlcTPM8buETmpZsf65UYOGKbonTM4P6d4C-hMwddqBZ2Fj_tZRc4h0CwSilsjA8PNMoZtKE9AP1WxSrIzf-R_M-sh8LiLXbU1PRn3aUkPjrQ6G0A8agvVwTXCJ3hpYbimkaVvlFI0JtqIijMdesRtLKXKL1rx45zki9JDs4B2BGF2HZ4_6FY7mTddsanV1d22HMzQ_tL3VQXl4qCumRRYCQM_Y8F3uIyoJU2JT35DGNODs7kdMasjCwMKbNNC51iE0N8_5XyaFlJUD1SJEkmdqBwl3JRxLMNwnPNXzTELDdTxn3RLjhptCamrh5cB4PU31LOW7grk"
field_types = ["checkbox", "text", "textarea", "dropdown"]
available_for = ["customer", "item", "supplier", "sales", "purchasing"]

errors = 0
supplier_id = 0
purchase_id = 0
customer_id = 75142194
product_id = "SBV-5108"
lot_id = "lot-1"

def create_checkbox(avail_for):
    print("Creating checkbox...")
    global errors
    url = baseurl + "/fields"

    data = {
        'name': f'{avail_for}-checkbox',
        'type': 'checkbox',
        'available_for': avail_for,
        'use_in_layouts': 'true'
    }  

    headers = {
    'Authorization': f'Bearer {bearer}'
    }

    response = requests.post(url, headers=headers, json=data)
    # if 201 then succes, else print response.text
    if response.status_code != 201:
        print("❌ Status code:", response.status_code)
        print("❌ Error message:", response.text)
        errors = errors + 1
    else:
        print(f'✅ Status 201! Created Checkbox, available for {avail_for}.')

def create_text(avail_for):
    print("Creating text...")
    global errors
    url = baseurl + "/fields"

    data = {
        'name': f'{avail_for}-text',
        'type': 'text',
        'available_for': avail_for,
        'use_in_layouts': 'true'
    }  

    headers = {
    'Authorization': f'Bearer {bearer}'
    }

    response = requests.post(url, headers=headers, json=data)
    # if 201 then succes, else print response.text
    if response.status_code != 201:
        print("❌ Status code:", response.status_code)
        print("❌ Error message:", response.text)
        errors = errors + 1
    else:
        print(f'✅ Status 201! Created text, available for {avail_for}.')

def create_textarea(avail_for):
    print("Creating textarea...")
    global errors
    url = baseurl + "/fields"

    data = {
        'name': f'{avail_for}-textarea',
        'type': 'textarea',
        'available_for': avail_for,
        'use_in_layouts': 'true'
    }  

    headers = {
    'Authorization': f'Bearer {bearer}'
    }

    response = requests.post(url, headers=headers, json=data)
    # if 201 then succes, else print response.text
    if response.status_code != 201:
        print("❌ Status code:", response.status_code)
        print("❌ Error message:", response.text)
        errors = errors + 1
    else:
        print(f'✅ Status 201! Created textarea, available for {avail_for}.')

def create_dropdown(avail_for):
    print("Creating dropdown...")
    global errors
    url = baseurl + "/fields"

    data = {
        'name': f'{avail_for}-text',
        'type': 'dropdown',
        'available_for': avail_for,
        'use_in_layouts': 'true',
        'options': [{'id':1, 'label':'XS', 'value': 'xsmall'}, {'id':2, 'label':'XL', 'value': 'xlarge'}]
    }  

    headers = {
    'Authorization': f'Bearer {bearer}'
    }

    response = requests.post(url, headers=headers, json=data)
    # if 201 then succes, else print response.text
    if response.status_code != 201:
        print("❌ Status code:", response.status_code)
        print("❌ Error message:", response.text)
        errors = errors + 1
    else:
        print(f'✅ Status 201! Created dropdown, available for {avail_for}.')

def create_supplier(company_name):
    print("Creating supplier...")
    global supplier_id
    global errors
    url = baseurl + "/suppliers"
    payload = {
        'contact_email': 'mikkel.rask+rbacc@visma.com',
        'company_name': company_name,
        'vat_zone': ' domestic',
        'supplier_group_id': ' 1',
        'payment_terms_id': ' 6'
    }
    headers = {
        "Authorization": f'Bearer {bearer}',
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code != 201:
        print("❌ Status code:", response.status_code)
        print("❌ Error message:", response.text)
        errors = errors + 1
    else:
        response_data = response.json()
        supplier_id = response_data['supplier']['number']
        print(f'✅ Status 201! Created supplier, {company_name} ({id}).')

def create_purchase_draft(supplier_id):
    print("Creating purchase draft...")
    global errors
    url = baseurl + "/purchase-orders/drafts"
    payload = {
        'supplier_id': supplier_id,
        'heading': 'Test PO',
        'book': 'false'
    }

def create_purchase(supplier_id, product_id, lot_id):
    global errors
    url = baseurl + "/purchase-orders"
    payload = {
        'supplier_id': supplier_id,
        'vat_zone': 'domestic',
        'heading': 'Test PO',
        'book': 'false',
        'lines': [
            {
                'item_id': product_id,
                'name': 'Product',
                'quantity': 1,
                'line_price': 10
            },
            {
                'item_id': lot_id,
                'name': 'You call that a lot? THIS is a lot!',
                'quantity': 10000,
                'line_price': 10
            }
        ]
    }
    headers = {
        "Authorization": f'Bearer {bearer}',
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code != 201:
        print("❌ Status code:", response.status_code)
        print("❌ Error message:", response.text)
        errors = errors + 1
    else:
        print(f'✅ Status 201! Created puchase order form {supplier_id}.')

if __name__ == '__main__':
    for i in available_for:
        create_checkbox(i)
        create_text(i)
        create_textarea(i)
        create_dropdown(i)
    create_supplier("Test Supplier")
    create_purchase_draft(supplier_id)