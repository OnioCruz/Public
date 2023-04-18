#!/bin/usr/env python3
from sre_constants import SUCCESS
from urllib import response
import requests
import pyjq
import json
import sys
import re
import os
from pprint import pprint
from urllib.request import urlopen

# -----------------------------------------------------Curling agify

studentname = input("What is your first name?"):
url = 'https://api.agify.io/?name=$' + studentname + '.json'
response = urlopen(url)
data_json = json.loads(response.read())
print(data_json)

json_output = json.dumps(data_json, indent=4)
with open("my_agify_info.json", "w") as outfile:
    outfile.write(json_output)

# ------------------------------------------------------------
latest_tf_url = url("https://releases.hashicorp.com/terraform/index.json")

txt = latest_tf_url
x = re.findall("re|beta", "linux.*am64", txt)
print(latest_tf_url)

filename = print(latest_tf_url)
if filename is open:
    latest_tf_url > filename
    if SUCCESS:
        print("That's all folks")

# ----------------------------------------------------API call and request
username = 'FullstackAcademy'
url = f"https://api.github.com/users/{username}"
user_data = requests.get(url).json()
pprint('Name of Github user: ' + user_data['name'])
pprint('Bio: ' + user_data['bio'])
pprint('E-mail: ' + user_data['email'])
pprint('Blog: ' + user_data['blog'])
pprint('Github Repos: ' + user_data['repos_url'])
pprint('Location: ' + user_data['location'])
pprint('Type of account: ' + user_data['type'])
