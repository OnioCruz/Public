#!/bin/usr/env python3
from urllib import request
from pathlib import Path
import requests
import os.path
import time
import progressbar
import json
import subprocess
import sys
import re
import os
from pprint import pprint
from urllib.request import urlopen
# ---------------------------------------- Student name as Input
result = os.popen(
    "curl https://api.agify.io/?name=$'" + input("What is your first name? ") + "'.json'").read()
with open("my_agify_info.json", "w") as file:
    file.write(json.dumps(result))
# ---------------------------------------------cURL and jq sort
result1 = os.popen(
    "curl https://releases.hashicorp.com/terraform/index.json").read()
with open("results1.json", "w") as file1:
    file1.write(json.dumps(result1))
# ----------------------------------------------File Name echo
with open('curljq.sh', 'w') as file2:
    file2.write("#!/bin/bash\nLATEST_TF_URL=`curl -L https://releases.hashicorp.com/terraform/index.json | jq -r '.versions[].builds[].url' | egrep -v 'rc|beta' | egrep 'linux.*amd64' |tail -1`\n")

output = os.system("sh curljq.sh")
if output == True:
    with open("FILENAME.txt", "w") as file3:
        file3.write(output[0:6])
# -----------------------------------------------Does file exist
file_exists = os.path.exists('FILENAME.txt')
print(file_exists)
if file_exists == True:
    bar = progressbar.ProgressBar()
    for i in bar(range(100)):
        output = os.system("sh curljq.sh")
        with open("FILENAME.txt", "w") as file4:
            file4.write(output)
# ----------------------------------------------------REST API call and request
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
