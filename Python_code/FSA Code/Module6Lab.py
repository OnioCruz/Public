#!/usr/bin/env python3

import chowencryption

testplaintext = 'some data late at night'
file = open('encrypted.txt', 'r')
ciphertext = file.read()
# print(type(ciphertext))
chowencryption.chowencrypt(testplaintext, 6667)
decryptedresult = chowencryption.chowdecrypt(ciphertext, 6667)

# simple validation test
if (testplaintext == decryptedresult) == True:
    print('Data integrity valid')
