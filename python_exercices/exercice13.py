#!/bin/python3 

# 13. Write a Python program to add 'ing' at the end of a given string (length
# should be at least 3). If the given string is already ends with 'ing' then add
# 'ly' instead. If the string length of the given string is less than 3, leave
# it unchanged.  Sample String : 'abc' Expected Result : 'abcing' Sample String
# : 'string' Expected Result : 'stringly'

list  = ['abc', 'string', 'interesting', 'strong', 'et']

ending = 'ing'

for i in list:
    if len(i) < 3:
        print(i)
    else:
        if i[-3:] == ending:
           print(i + 'ly')
        else:
            print(i + 'ing')


