#!/bin/python3 


# 17. Write a Python program to sort (ascending and descending) a dictionary by
# value.

dictionary = {'key2':'value2','key1':'value1','key4':'value4','key3':'value3'}

def sort_dictionary(i = "reverse"):
    if (i == "reverse"):
        print(sorted(dictionary.values(), reverse=True))
    elif (i == "normal"):
        print(sorted(dictionary.values(), reverse=False))
    else:
        print("Incorrect parameter")

sort_dictionary()
