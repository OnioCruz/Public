#!/usr/bin/env python3

# Module 3 Lesson 2 "Sequence" Example 1
'''
mylist = ['astring', 10, 21.0, True]
print('the length of my list is: ' + str(len(mylist)))
# iterate over a list
for i in mylist:
    print(i)

print('-------spacer------')

# calling list by index
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[3])
print('-------spacer------')
# verify the heterogenous datatype
print('The third elemenet of the list is type: ' + str(type(mylist[3])))
'''
'''
myrange = range(0, 100, 5)
print(type(myrange))
for i in myrange:
    print(i - 10)
print('-------spacer-----------')
# no variable needed
for i in range(0, 10, 1):
    print(i)
'''
# Module 3 Lesson 2 "Mapping and Hashes" Example 2
'''
mydictionary = {
    "ipaddress": "8.8.8.8",
    "owner": "Google",
    "comment": "Public facing DNS server",
    "inuse": True,
    "number_load_balanced_servers": 100
}

print('printing mydictionary')
print(mydictionary)
print('-------------------')
print('get value by key: ')
print(mydictionary['ipaddress'])
print('-------------------')

# how about the reverse? use the .items method with a for loop
print('get KEY by value(s): ')
for key, value in mydictionary.items():
    if value == 'Google':
        print(key)

# example dictionary modifier methods
print('-------------------')
print('update a key value: ')
mydictionary.update({"inuse": False})
print(mydictionary)
'''

# Module 3 Lesson 2 "LIFO style queue"
'''
mylist = ['astring', 10, 21.0, True]
print('the length of my list is: ' + str(len(mylist)))
# iterate over a list
for i in mylist:
    print(i)

print('-------spacer------')

# calling list by index
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[3])
print('-------spacer------')
# verify the heterogenous datatype
print('The third elemenet of the list is type: ' + str(type(mylist[3])))

# add or remove items from a list
mylist.append('beer thirty')
mylist.append(30)
print('my NEW length of mylist is: ' + str(len(mylist)))

print('-------spacer------')
print('removing astring based on value, not index: ')
mylist.remove('astring')
print(mylist)
print('popping off the list based on LAST element in position')
mylist.pop(len(mylist)-1)  # include minus 1 because computers count from 0
print(mylist)
'''
# Intializing a queue
'''
# load libraries needed

# open file handler
import re
file = open('sample-data.txt', 'r')

# if using a counter create an empty var
ssncount = 0
emailcount = 0

# add the queue for now just to show we know how to use one
myqueue = []
for i in file:
    myqueue.append(i)
# print(myqueue)

# close file handler
file.close()

# grab from the queue FIFO
for i in range(0, len(myqueue)-1):
    queue_element = myqueue.pop(0)
    # print(queue_element)
    isssn = re.match('\d{3}-\d{2}-\d{4}', queue_element)
    isemail = re.match(
        '[a-zA-Z0-9]{1,20}\@[a-zA-Z]{1,20}\.[a-zA-Z]{3,5}', queue_element)
    if (bool(isssn)) == True:  # use bool to get true/false condition of match
        ssncount = ssncount + 1
    if (bool(isemail)) == True:
        emailcount = emailcount + 1
'''
# this is the regular way of iterating through file w/o FIFO queue
for i in file:
    isssn = re.match('\d{3}-\d{2}-\d{4}', i)
    isemail = re.match('[a-zA-Z0-9]{1,20}\@[a-zA-Z]{1,20}\.[a-zA-Z]{3,5}', i)
    if (bool(isssn)) == True:  # use bool to get true/false condition of match
        ssncount = ssncount + 1
    if (bool(isemail)) == True:
        emailcount = emailcount + 1
'''
# print results std out
print('SSNs detected: ' + str(ssncount))
print('Emails detected: ' + str(emailcount))

# print queue should be 0 now
print('check for the empty queue: ')
print(myqueue)

# close file handler
# file.close()
'''
