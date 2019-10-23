#!/bin/python3 


# 6. Write a Python program to count the number of characters in a string.
# Sample String : 'google.com' Expected Result : {'o': 3, 'g': 2, '.': 1, 'e':
# 1, 'l': 1, 'm': 1, 'c': 1}

string = 'google.com'

d = dict()

for letter in string:
    if letter in d:
        d[letter] = d[letter]+1
    else:
        d[letter] = 1

for key in list(d.keys()):
    print(key, ": ", d[key])


