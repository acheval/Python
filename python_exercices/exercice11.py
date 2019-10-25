#!/bin/python

# 11.Write a Python program to get a string from a given string where all
# occurrences of its first char have been changed to '$', except the first char
# itself.  Sample String : 'restart' Expected Result : 'resta$t'

string = 'restart'

i = string[0]

string2 = i + string[1:].replace(i, '$')

print(string2)
