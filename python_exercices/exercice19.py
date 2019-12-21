#!/bin/python3


# 19. Write a Python program to add key to a dictionary.  Sample Dictionary :
# {0: 10, 1: 20} Expected Result : {0: 10, 1: 20, 2: 30}


def add_to_dictionary(x):
    dictionary = {0: 10, 1: 20}
    "This adds to a dictionary"
    dictionary.update(x)
    print("Updated dictionary: " + str(dictionary))
    return


add_to_dictionary({2: 30, 4: 50})
