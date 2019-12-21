#!/bin/python3 


# 21. Write a Python program to check if a given key already exists in a
# dictionary.


def find_in_dictionary(key, dictionary):
    key_to_find = list()
    list_of_items = dictionary.items()
    for item in list_of_items:
        if item[0] == key:
            print("Key: " + str(item[0]) + " exists and has a value of: " + str(item[1]))
            break

    print("Key: " + str(key) + " does not exists in "+ str(dic))
    return

dic = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 9: 90, 10: 100, 7: 70, 8: 80}
key = 6

find_in_dictionary(key, dic)
