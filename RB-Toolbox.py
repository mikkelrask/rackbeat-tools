import os
import sys
import time
import requests
import msvcrt
from dotenv import load_dotenv

load_dotenv()
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
IMPORT_FILE = os.getenv("IMPORT_FILE")

def fetch_company_info():
    global BEARER_TOKEN
    url = "https://app.rackbeat.com/api/self"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer " + BEARER_TOKEN
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        company_name = response.json()['user_account']['company_name']
        account_number = response.json()['user_account']['id']
        return company_name, account_number
    else:
        print("Failed to fetch company info. Please check the BEARER_TOKEN environment variable in .env file.")
        print("Status Code:", response.status_code)
        print("Response:", response.text)
        exit()

def show_menu(company_name, account_number):
    global BEARER_TOKEN
    print("================================================================================")
    print('    ___       ___       ___       ___       ___       ___       ___       ___   ')
    print('   /\  \     /\  \     /\  \     /\__\     /\  \     /\  \     /\  \     /\  \  ')
    print('  /::\  \   /::\  \   /::\  \   /:/ _/_   /::\  \   /::\  \   /::\  \    \:\  \ ')
    print(' /::\:\__\ /::\:\__\ /:/\:\__\ /::-"\__\ /::\:\__\ /::\:\__\ /::\:\__\   /::\__\ ')
    print(' \;:::/  / \/\::/  / \:\ \/__/ \;:;-",-" \:\::/  / \:\:\/  / \/\::/  /  /:/\/__/')
    print('  |:\/__/___ /:/  /___\:\__\ ___|:|  | ___\::/  /___\:\/  /___ /:/  /___\/__/   ')
    print('   \|__|/\  \\/__//\  \\/__//\  \\|__|/\__\\/__//\  \\/__//\  \\/__//\__\       ')
    print('        \:\  \   /::\  \   /::\  \   /:/  /    /::\  \   /::\  \   |::L__L      ')
    print('        /::\__\ /:/\:\__\ /:/\:\__\ /:/__/    /::\:\__\ /:/\:\__\ /::::\__\     ')
    print('       /:/\/__/ \:\/:/  / \:\/:/  / \:\  \    \:\::/  / \:\/:/  / \;::;/__/     ')
    print('       \/__/     \::/  /   \::/  /   \:\__\    \::/  /   \::/  /   |::|__|      ')
    print('                  \/__/     \/__/     \/__/     \/__/     \/__/     \/__/       ')
    print("================================================================================")
    print(f"Company: {company_name} ({account_number})")
    print("")
    print("Please choose an option:\n")
    print("  1. Create Product Groups")
    print("  2. Create Unit Types")
    print("  3. Import products")
    print("  4. Update products\n")

    print("q. Quit\n")

def run_create_groups():
    print("Importing products...")
    os.system("python create-groups.py")

def run_create_unit_types():
    print("Running create-unit-types.py...")
    os.system("python create-unit-types.py")

def run_import_products():
    global IMPORT_FILE
    print("You are about to import products using the following CSV file: " + IMPORT_FILE)
    confirmation = input("Do you want to continue? (y/n): ")
    if confirmation.lower() == 'y':
        os.system("python create-products.py")
    else:
        print("Update canceled.")

def run_update_products():
    global IMPORT_FILE
    print("You are about to update products using the following CSV file: " + IMPORT_FILE)
    confirmation = input("Do you want to continue? (y/n): ")
    if confirmation.lower() == 'y':
        os.system("python update-products.py")
    else:
        print("Update canceled.")


def getch():
    # Read a single character from the user input
    if os.name == 'posix':
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    else:
        ch = msvcrt.getch().decode()
    return ch

while True:
    company_name, account_number = fetch_company_info()
    show_menu(company_name=company_name, account_number=account_number)
    choice = getch()

    if choice == '1':
        run_create_groups()
    elif choice == '2':
        run_create_unit_types()
    elif choice == '3':
        run_import_products()
    elif choice == '4':
        run_update_products()
    elif choice == 'q':
        break
    else:
        print("Invalid choice. Please select a valid option.\n")
        time.sleep(0.75)
