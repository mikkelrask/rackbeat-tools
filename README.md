# 📦 Rackbeat WMS API utils

A small collection of python scripts to perfom actions on a Rackbeat inventory.

In its simple form, it's an easy way to perform automated tasks through the Rackbeat API.  
Its intented for use on Windows, but the python scripts themselves should work regardless of OS.

## Current tools

- Create Product Groups
- Create Unit Types
- Import products
- Import changes to existing product

## Installing

The toolbox scripts are made in Python, which is of course required.
They also depend on different libraries to function as well. A install script has been provided in `install-toolbox-deps.ps1`, that will verify that `python`, `pip` and the nessecary python libraries are available. To run this, your user needs to have a `unrestricted` execution policy. If you are able to run scripts, you can skip step 2:

1. Open a Powershell terminal  
   Click the start menu, and type `Poweshell` and click the [`Run as administrator`](./img/adminstrator.png) option.
1. Set the Powershell execution restrictions as `unrestricted` *  
   Type `set-executionpolicy unrestricted` in the terminal and hit `Enter`
1. Clone this Github repo locally with the command:  
   copy the following command `git clone https://github.com/mikkelrask/rackbeat-tools.git ` and paste it to the terminal
1. Navigate into the local repo
   type `cd rackbeat-tools` and press `Enter`   
1. Install requirements and dependencies with:  
   `& .\install-toolbox-deps.ps1`

This will install the latest verion of `python`, `pip` and the libraries `requests` and `python-dotenv`

## Updating the toolbox

When new tools are added, or current ones are updated, you can update your repo to get the latest changes. When in your project folder, open a Terminal (i.e Right click, and click "Open in Terminal")

Type `git pull` and hit `Enter`.
Your local repo now has the latest changes.

---

## Bearer token 🧸

To use the utilities, you need to provide a valid API key as your `Bearer` token to be able to make requests.

This token acts as a password to ensure that you have the privilege to perform actions on the account.
API keys are personal, and all actions performed with the utilities will be linked to the user who created it.

To generate an API key, follow these steps:

1. Go to [app.rackbeat.com/settings/api](https://app.rackbeat.com/settings/api).
2. Click the `Create new` button.
3. Give the API key a fitting name.
4. Confirm the creation of the new API key by clicking `Create new`.

After generating the API key, you will receive a base64url encoded JSON key, which should look like this:

![It should provide you a [base64url encoded json](https://www.rfc-editor.org/rfc/rfc7519#3.0) key like so](image.png)  
It should provide you with a [base64url encoded json](https://www.rfc-editor.org/rfc/rfc7519#3.0) like this (no worries, this isnt an active key)

Please note that the API key will not be displayed again, so make sure to store it properly.

---

## Environment variables

To make sure that you don´t have to edit and save all utils with the correct Bearer token on each run, an environment file has been created, which all utilities then refers to, when looking for the API key.

To use the API key in your Python project, follow these steps:

1. Locate the `.env` file in the root folder of your project.
2. Copy and paste the generated API key between the quotes of the `BEARER_TOKEN`, like this:

```json
BEARER_TOKEN="eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIzIiwianRpIjoiYzRhODIwNWRiNTJlMGU3NGVkODRhNjk0MjY4YWE4MDQ5MDQzNzY2MTFlNWQ5YmU3ZDVlMTY2NGQ2ZDgzMGQ2ODNiNzc5ZDA3MTgxZWE0NjIiLCJpYXQiOjE2ODc1OTc3MjAuMjc3MDMzLCJuYmYiOjE2ODc1OTc3MjAuMjc3MDM3LCJleHAiOjIwMDMyMTY5MjAuMjY1Mzk2LCJzdWIiOiIxNTM1NSIsInNjb3BlcyI6W119.DY_cZP-bpRZTGVOEAZwehmuSWsZVozSfW8QPeMZyVveeTvzB6TML9TkNRut_fYjiJ5uQvsN7MQcv7XjSiRnCT89Latx70Cq1qGqf6BtEVWwvMlO90nWwL7LBfCOwHADQMyRMsBEOpMKXfPiTSbY6CAYAEhn26BCfsi24Qh_1xSb-wMhqxaHkk2_9S9nh8KXlxpbDVCrpGMS04aUVcVudzVztSbjoIjNlsCPO8H8TD4VfqcV9zbKQy3IAe-1eUPTdilQaty2vbK-vl0qsSLvIT32SiY-fAtTu8Ya7_x5xZKG5Hpfw1ol1PBjHfrD2NH1xqLacCyGmynna7HAAFV5xNoNKhoP-tHvh1ZW0PnJP5iXHr9O0FYEidIqm0YSwqP7V43O1m1hkRnnvfEFxwZMwya8W81f1JbmDJSOUv2iKnbKAR4lUvmggpAB7S4OvRUWD5_V8uScyVynDO07CJKfwEhKttfKpAbAzQeHBCtYqa5HdpGpy4vRqfvm4rGeA2VNAEtz1uV4KT-Dw9dIwYMb20sGw2Vm-vNvx3-qNlJq2WJlTaCd5gnajN3TS8ZjATMrTdylbLXmj9cuJFf0N8nBL8C_IfkYGXgwWez_XrF6Wq43NFgeY69N1cFrX7K-b--9ZKUoZU5He0y7FrTraXKXfdOviu2Z7hSXDPejtJXhrhZI"
(no worries, this is **not** an active key)
```

3. Save the file.

---

## Import file

For each customer, start out by creating a copy of the `import-template.csv` file. This file has custom named table headers, that the import/update scripts map with what the API endpoints expects. To prevent mishaps, when managing multiple Rackbeat accounts, sticking to a naming convention i.e like `{account}-{date}.csv`, could help minimize wrongful imports, but has no other function than that.

1. Open the `.env` file again
2. Put the import files local path in the `IMPORT_FILE` variable in the `.env` file. So if the import file was located in the same directory as eht `.env` file, it would look like this:  
   `IMPORT_FILE="./7235-24062023.csv"`
3. Save the `.env` file.

---

## Use the Toolbox

To run the toolbox, execute the RB-Toolbox script:   
1. Open the Repo folder in your File Explorer
2. Right click the folder and click `Open in Terminal`
3. Type `python .\RB-Toolbox.py` and press `Enter`.
4. Follow the instructions on the screen.

Please always remember to verify the company and agreement number, shown in the top!

## Create groups

With the Bearer token set in the `.env` file, often times the first thing youd want to do is to quickly create some item/product groups.

1. Execute `python .\create-groups.py` in a terminal emulator.
2. Fill out `Group name: ` when prompted
3. Fill out `Group ID:` when prompted
4. Fill out VAT informations for domestic, EU, abroad and domestic tax-exempt
5. Set weather the products in this group has an inventory
6. Set weather the products in this group are able to be sold (y/n)

---

## Import Products

With both the `.env` file populated, and and the `groups` created, we are ready to rock and/or roll!

`python .\import-products.csv` will look in the `.env` file for the `BEARER_TOKEN`/api key and what file it needs to process.

Note! This script iterates through each line of the csv file, creating the products one by one. This can potentially be a lot of calls, and is not at all effecient. But it does make sure we don´t hit any speed limits, just as it will still create what ever products it can from the import sheet, rather than to abort the complete import if theres was found an error on one or more of the lines in the product sheet. The lines that wasnt importable will be skipped, and an exlanation/error message will be output in the terminal window.

---

## Update Products

When products have been populated to your Rackbeat inventory, sometimes minor changes are needed. Make multiple of those, by importing product updates.

1. Edit the `7235-24062023.csv` file (or whatever your import file was named) with the wanted changes
2. execute `python update-products.py`
3. ...?
4. Profit! 🤑
