#!/bin/python3 


# 10. Write a Python program to get a string made of the first 2 and the last 2
# chars from a given a string. If the string length is less than 2, return
# instead the empty string.  Sample String : 'w3resource' Expected Result :
# 'w3ce' Sample String : 'w3' Expected Result : 'w3w3' Sample String : ' w'
# Expected Result : Empty String

string = 'w3resource', 'w3', 'w', 'Hello World'

for i in string:
    if len(i) < 2:
        print("Empty String")
    else:
        print(i[:2] + i[-2:])


