#!/usr/bin/env/python3

# Module 4 Lesson 1 "Interactive" Example 1
'''
import sys
import re
untrustedinput = input('Please enter your name: ')
# check if a name is improbably long for buffer overruns
if len(untrustedinput) > 50:
    print('input too long')
    sys.exit(1)  # exit status code as std error
# input sanitization "de-fanging"
inputscrubstage1 = re.sub("[\\<>\''\/\(\)]", '', untrustedinput)
print(inputscrubstage1)
'''
# Module 4 Lesson 1 "File System" Example 2
'''
import sys
import re
import os

# check for appropriate runtime parameters
if len(sys.argv) == 1:
    print('Usage: main.py </path/to/file>')
    sys.exit(0)

# use file argument for flat file
filenamearg = sys.argv[1]

# open file handler
untrustedinput = open(filenamearg, 'r')

# check if a name is improbably long for buffer overruns
for i in untrustedinput:
    if len(i) > 50:
        print('input too long')
        sys.exit(1)  # exit status code as std error
    # input sanitization "de-fanging"
    inputscrubstage1 = re.sub("[\\<>\''\/\(\);]", '', i)
    # print(inputscrubstage1)
    os.popen('curl -vs -m 1' + ' ' + inputscrubstage1 + ' 2>&1')
'''
# Module 4 Lesson 1 "Web Requests" Example 3
'''
from flask import Flask, request, jsonify
import os
app = Flask(__name__)


@app.route('/foo', methods=['POST'])
def foo():
    data = request.json
    # print(data['somekey'])
    command = str(data['cmd'])
    domain = str(data['domain'])
    result = str(os.popen(command + ' ' + domain).read())
    # return jsonify(data)
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8443)
'''

# Module 4 Lesson 1 "Common Encodings"
'''
#!/usr/bin/env python3
# my dictionary list for validating the correct key
import base64
mywordlist = [‘foo’, ‘bar’, ‘kali’]

# my really insecure key
mycleartextkey = ‘kali’

# encode the key in ascii bytes first prep to base64
mycleartextkey = mycleartextkey.encode(‘ascii’)
# encode my clear-text key to base64
mybase64key = base64.b64encode(mycleartextkey)
# check the output
print(‘This is my encoded value, to check at API auth service: ‘)
print(mybase64key)

# encode dictionary values and check boolean True
for I in mywordlist:
  keybyte = i.encode‘'asci’')
  keybase64value=base64.b64encode(keybyte)
  print“"Tryin“I. ' ' ' ' + str(i))
  if (keybase64value == mybase64key) == True:
    print('Successful authentication key: ' + str(i))
'''

# Module 4 Lesson 3 "Main Lab"
'''
# Example 1
with open('output.txt') as f:
    lines = f.readlines()
    print(lines)
'''
'''
# Example 2
with open('output.txt') as f:
    lines = f.readlines()
    print(lines[0])
    f = close
'''
# Example 3
'''
from fileinput import close
with open('output.txt') as f:
    lines = f.readlines()
    print(lines)
    f = close
'''
'''
output = open('output.txt', "a")
output.write("Please work")
print(output)
'''
# Example 5


def longest_word(filename):
    with open(filename, 'r') as infile:
        words = infile.read().split()
        print(words)

 max_len = len(max(words, key=len))
    # Use list comprehension to find longest word
    return [word for word in words if len(word) == max_len]