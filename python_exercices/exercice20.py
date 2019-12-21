#!/bin/python3


# 20. Write a Python program to concatenate following dictionaries to create a
# new one.  Sample Dictionary : dic1={1:10, 2:20} dic2={3:30, 4:40}
# dic3={5:50,6:60} Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


def merge_dictionary(first_dic, *dic):
    merged_dictionary = first_dic.copy()
    for x in dic:
        merged_dictionary.update(x)
    return merged_dictionary


dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic4 = {7: 50, 8: 60}
dic5 = {9: 50, 10: 60}

print(merge_dictionary(dic1, dic2, dic3, dic5, dic4))
