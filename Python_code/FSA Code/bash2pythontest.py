#!/bin/usr/env python3
from sre_constants import SUCCESS
from urllib import response
import requests
import json
import os
from pprint import pprint
from urllib.request import urlopen
'''
url = 'https://api.agify.io/?name=$' + \
    input("What is your first name? ") + '.json'
response = urlopen(url)
data_json = json.loads(response.read())
print(data_json)
json_output = json.dumps(data_json, indent=4)
with open("my_agify_info.json", "w") as outfile:
    outfile.write(json_output)
'''
result = os.popen(
    "curl https://api.agify.io/?name=$'" + input("What is your first name? ") + "'.json'").read()
with open("my_agify_info.json", "w") as file:
    file.write(json.dumps(result))
# ---------------------------------------------cURL and jq sort
result = os.popen(
    "curl https://releases.hashicorp.com/terraform/index.json").read()
with open("results1.json", "w") as file:
    file.write(json.dumps(result))

print(pyjq.all(".versions[].builds[].url", result))
