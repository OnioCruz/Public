#!/bin/usr/env python3
from multiprocessing.sharedctypes import Value
from sre_constants import SUCCESS
from textwrap import indent
from urllib import response
from wsgiref import headers
import requests
import json
import subprocess
import sys
import re
import os
from pprint import pprint
from urllib.request import urlopen

result = os.popen(
    "curl https://api.agify.io/?name=$'" + input("What is your first name? ") + "'.json'").read()
with open("my_agify_info.json", "w") as file:
    file.write(json.dumps(result))
    print(result)

studentname = input("What is your first name?")
url = 'https://api.agify.io/?name=$' + studentname + '.json'
response = urlopen(url)
data_json = json.loads(response.read())
print(data_json)
