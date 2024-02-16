from utils.api_utils import send_request

discount_group_ids = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
discounts = [ '25', '0', '0', '25', '25', '16', '15', '30', '20', '20', '20', '20']
csv = 'customers.csv'

BEARER_TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIzIiwianRpIjoiN2VhMjkyNWQyNDJlMWVmZDY2OTk0OWUzNDhmYmFjZjc2NmQ0NmM5ODkwMmM0NGZmODQ5YjViNTZjZGE5MWE5ODgwMWUyMWExMjYwM2EzYzkiLCJpYXQiOjE2ODM3MDQ0ODUuMjc3NTU1LCJuYmYiOjE2ODM3MDQ0ODUuMjc3NTYxLCJleHAiOjE5OTkzMjM2ODUuMjU4OTgyLCJzdWIiOiIxNTM1NSIsInNjb3BlcyI6W119.cvNLKXn6XFeFE8PGd-TC7MT6Z0HNiOStzjcKhXfjfWVbzP2G2A0efsoySu20Fvs01mfx2UorQ6tueReHwEa9dJDIwQUtpOoyZxNYZnvYptl1QAfwZDrXZ6rTUOfS2eM_OUvcdG207jvffbDOYYGPp22kp6Fh8WL_naMNAhM1WsLPSB4WOnm6RSOR2F1cXwraVYHzR6bkL6XfkzN2iVgPxb7Yw2sCCBhjHudg4ZR4hMiYNvh2_EJpZEDGVNUvP0oAiieOJn_DHzAjbf-C143eBnILIdwapeb6KjaMFG2oh6rsEGG4lvWPY4ch1CIhY-Y_Jjie4klCO0SURBBg2Bf41NAxjeAo-DAhligYliJV3jfNYAxXrM1ueTbjQrb3UBjR5NO3E7zNpTeU5tQ60K9E5U7wMF7zCNTF_5sRZaxULMuxZV2-J49er-Ql95eXg9-3BYvP3_FuTp_Ff_ZdYXSEQbBWlwpsE5prFhm4b7xtVNxmt0F5e9VMKshZXCQITvpMJIZkwHLjb8cTqZkfxefYk9wBmvtGmBVFVKa_ADvtnOOpxqVuDxDZYtnr0ncIEm2eGXyWRqt4aktnbbKNbwpwX5fJA0wweVw1WTzoOvrSxbVo3fCQNxitWr-NKeyoLcbCC-F4R4Y81S0MED1P-WZbuyxRiMuWsbYXigMZ8Oq9Y3c'

# read all customers from the CSV file:
def read_customers_from_csv(csv):
    customers = []
    with open(csv) as f:
        for line in f:
            customer = line.split('\n')
            customers.append({
                'number': customer[0],
            })
    return customers

def update_customer_discount_groups():
    customers = read_customers_from_csv(csv)
    headers = {
    'Authorization': f'Bearer {BEARER_TOKEN}',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
    }

    for customer in customers:
        for discount_group in discount_group_ids:
            for discount in discounts:
                payload = {
                       "override_discount_percentage": discount
                }
                endpoint = f"customers/{customer['number']}/discount-groups/{discount_group}"
                print(endpoint)
                # update the customer discount group
                response = send_request(endpoint, 'POST', headers=headers)
                if response.status_code == 403:
                    print(f"❌ Customer {customer['number']} is already part of discount group {discount_group}")
                    print(response.text)
                    pass
                if response.status_code != 200:
                    print(f"❌ Failed to update customer {customer['number']} discount group to {discount_group}")
                    print(response.text)
                    pass
                else:
                    print(f"✅ Customer {customer['number']} discount group updated to {discount_group}")
                update = send_request(endpoint, 'PUT', headers=headers, data=payload)
                if update.status_code != 200:
                    print(f"❌ Failed to update customer {customer['number']} discount group to {discount_group}")
                    print(update.text)
                    pass
                else:
                    print(f"✅ Customer {customer['number']} discount group {discount_group} updated discount percentage to")
    return        

if __name__ == '__main__':
    update_customer_discount_groups()
