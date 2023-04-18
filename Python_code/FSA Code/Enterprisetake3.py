#!/bin/usr/env python3
from ast import Delete
import re
from unittest import result
import requests
import json
import pprint

studentname = input("What is your first name? ")
url = f"https://api.agify.io/?name={studentname}"
user_data = requests.get(url).json()
with open("my_agify_info.json", "w") as file:
    file.write(json.dumps(user_data))

url1 = f"https://releases.hashicorp.com/terraform/index.json"
json_data = requests.get(url1).json()
for version in json_data['versions'].keys():
    for build in json_data['versions'][version]['builds']:
        print(result)

        # with open('results.json', "w") as file1:
        #   file1.write(build['url'])


username = input("Please Enter Github Account Name: ")
url = f"https://api.github.com/users/{username}"
user_data = requests.get(url).json()
if requests.status_codes.codes.ok == 200:
    pprint(user_data)
    time.sleep(5)


def clrscr():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

    print("Screen Cleared")


clrscr()
