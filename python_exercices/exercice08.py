#!/bin/python3 


# 8. Write a Python program to count the number of strings where the string
# length is 2 or more and the first and last character are same from a given
# list of strings.  Sample List : y['abc', 'xyz', 'aba', '1221'] Expected Result
# : 2

list = ['abc', 'xyz', 'aba', '1221']

n = 0

for i in list:
    if len(i) > 2 :
        x = i[:1]
        y = i[-1:]
        if x == y:
            n = n + 1
print(n)
