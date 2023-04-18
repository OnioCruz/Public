#!/usr/bin/env python3
'''
# area of a rectangle formula
def findrectanglearea(base, height):
    if base <= 0 or height <= 0:
        print("Please provide only positive values")

    # try/catch block to perform input validation
    try:
        base = float(base)
        height = float(height)
        area = base * height
    except:
        print("Please provide a valid input")


# Test the function to find the area of a rectangle
findrectanglearea(3, 10)
#findrectanglearea(-17, 4)
#findrectanglearea('foo', 'bar')
'''
'''
file = open('output.txt', 'r')
for line in file:
    print(line.split(','))
file.close()
'''

# Function to collect user data




from unittest import result
def collectuser():
    f_name = input("Please enter your first name: ")
    l_name = input("Please enter your last name: ")
    age = int(input("Please enter your age: "))
    ssn = int(input("Please enter your Social Security Number without dashses: "))
    cc_num = int(input("Please enter your credit card number: "))

    if isinstance(f_name, str) != True:
        print("Please enter a valid string first name")
        exit()
    if isinstance(l_name, str) != True:
        print("Please enter a valid string last name")
        exit()
    if isinstance(age, int) != True:
        print("Please enter a valid integer age")
        exit()
    if isinstance(ssn, int) != True:
        print("Please enter a valid SSN in the form of all integers")
        exit()
    if isinstance(cc_num, int) != True:
        print("Please enter a valid credit card number in thr form of all integers")
        exit()

    print("All input validated")
    print(f_name, l_name, age, ssn, cc_num)


# Call the function and use the data to print out a pwnd message to the user
user_info = collectuser()
print("Hello {} {}, you have been breached!! Thank you for supplying your age: {}, SSN: {}, and Credit Card information: {}.".format(
    user_info[0], user_info[1], user_info[2], user_info[3], user_info[4]))
