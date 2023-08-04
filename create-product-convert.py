import requests
import os
from dotenv import load_dotenv

load_dotenv()

ERRS = 0
FAILURES = []
SUCCESSES = 0

# Set your bearer token
bearer_token = os.getenv("BEARER_TOKEN")

# Array of BOMS values
BOMS = [
    "50", "51", "52", "53", "54", "55", "56", "80", "81", "82", "83", "84", "85", "86", "94", "95", "96",
    "100", "101", "102", "103", "104", "105", "106", "107", "108", "109", "112", "113", "114", "150",
    "151", "152", "153", "154", "155", "156", "157", "158", "159", "162", "163", "164", "200", "201",
    "202", "203", "204", "205", "206", "207", "208", "209", "212", "213", "214", "250", "251", "252",
    "253", "254", "255", "256", "257", "258", "259", "262", "263", "264", "300", "301", "302", "303",
    "304", "305", "306", "307", "308", "309", "312", "313", "314", "560", "AH100", "AH101", "AH102",
    "AH103", "AH104", "AH105", "AH106", "AH107", "AH108", "AH109", "AH113", "AH114", "AH150", "AH151",
    "AH152", "AH153", "AH154", "AH155", "AH156", "AH157", "AH158", "AH159", "AH163", "AH164", "AH200",
    "AH201", "AH202", "AH203", "AH204", "AH205", "AH206", "AH207", "AH208", "AH209", "AH213", "AH214",
    "AH250", "AH251", "AH252", "AH253", "AH254", "AH255", "AH256", "AH257", "AH258", "AH259", "AH263",
    "AH264", "AH300", "AH301", "AH302", "AH303", "AH304", "AH305", "AH306", "AH307", "AH308", "AH309",
    "AH313", "AH314", "D100", "D101", "D102", "D103", "D104", "D105", "D106", "D107", "D108", "D109",
    "D110", "D112", "D113", "D114", "D150", "D151", "D152", "D153", "D154", "D155", "D156", "D157",
    "D158", "D159", "D160", "D162", "D163", "D164", "D200", "D201", "D202", "D203", "D204", "D205",
    "D206", "D207", "D208", "D209", "D212", "D213", "D250", "D251", "D252", "D253", "D254", "D255",
    "D256", "D257", "D258", "D259", "D262", "D263", "D264", "D300", "D301", "D302", "D303", "D304",
    "D305", "D306", "D307", "D308", "D309", "D312", "D313", "D50", "D51", "D52", "D53", "D54", "D55",
    "D56", "D57", "D58", "D59", "D62", "D63", "D64", "DOB100", "DOB101", "DOB102", "DOB103", "DOB104",
    "DOB105", "DOB106", "DOB109", "DOB110", "DOB114", "DOB120", "DOB130", "DOB200", "DOB201", "DOB202",
    "DOB203", "DOB204", "DOB205", "DOB206", "DOB209", "DOB210", "DOB214", "DOB220", "DOB230", "DOB300",
    "DOB301", "DOB302", "DOB303", "DOB304", "DOB305", "DOB306", "DOB309", "DOB310", "DOB314", "DOB320",
    "DOB400", "DOB401", "DOB402", "DOB403", "DOB404", "DOB405", "DOB406", "DOB409", "DOB410", "DOB414",
    "DOB420", "DW103", "DW153", "DW203", "DW253", "DW303", "DW53", "FL150", "FL151", "FL152", "FL153",
    "FL154", "FL155", "FL156", "FL157", "FL158", "FL159", "FL160", "FL162", "FL163", "G100", "G150",
    "G200", "H100", "H101", "H102", "H103", "H104", "H105", "H106", "H107", "H108", "H109", "H112",
    "H113", "H114", "H150", "H151", "H152", "H153", "H154", "H155", "H156", "H157", "H158", "H159",
    "H162", "H163", "H164", "H170", "H171", "H200", "H201", "H202", "H203", "H204", "H205", "H206",
    "H207", "H208", "H209", "H212", "H213", "H214", "H220", "H221", "H250", "H251", "H252", "H253",
    "H254", "H255", "H256", "H257", "H258", "H259", "H262", "H263", "H264", "H300", "H301", "H302",
    "H303", "H304", "H305", "H306", "H307", "H308", "H309", "H312", "H313", "H314", "W100", "W101",
    "W102", "W103", "W104", "W105", "W106", "W107", "W108", "W109", "W113", "W114", "W150", "W151",
    "W152", "W153", "W154", "W155", "W156", "W157", "W158", "W159", "W163", "W164", "W200", "W201",
    "W202", "W203", "W204", "W205", "W206", "W207", "W208", "W209", "W213", "W214", "W250", "W251",
    "W252", "W253", "W254", "W255", "W256", "W257", "W258", "W259", "W263", "W264", "W300", "W301",
    "W302", "W303", "W304", "W305", "W306", "W307", "W308", "W309", "W313", "W314"
]

# API endpoint URL
url = "https://app.rackbeat.com/api/products/{}/convert"

# Iterate over each BOMS value and make the API call
for product_number in BOMS:
    # Create the complete URL with the current product number
    endpoint_url = url.format(product_number)
    
    # Set the headers
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json"
    }
    
    # Make the API call
    response = requests.post(endpoint_url, headers=headers)
    
    # Check the response status code
    if response.status_code == 200:
        print(f"Conversion successful for product number: {product_number}")
        SUCCESSES += 1

    else:
        print(f"Conversion failed for product number: {product_number}")
        print(f"Error message: {response.text}")
        if response.text.__contains__("used in lines"):
            FAILURES.append(product_number)
            ERRS += 1

print(f"Conversion of products to BOMs finished!")
print(f"Total products converted: {SUCCESSES}")
print(f"Total products failed: {ERRS}")
print(f"Failed products: {FAILURES}")
