#!/bin/usr/env python3
from sre_constants import SUCCESS
from urllib import response
import requests
import json
import sys
import re
import os
from pprint import pprint
from urllib.request import urlopen

input("What is your first name? ")

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
