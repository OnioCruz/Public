#!/usr/bin/env python
import subprocess
with open("finished.txt", "w+") as output:
    subprocess.call(["python", "./linuxextracredit.py"], stdout=output)

question = input("True or False: Did Antonio do the assignment correctly? ")

if question == ("true"):
    print("Yay I did it!")
if question == ("false"):
    print("Failed Miserably!")
