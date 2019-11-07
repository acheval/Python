#!/bin/python3 


# 15. Write a Python function that takes a list of words and returns the length
# of the longest one.

list = ["test", "garbage", "landlord", "timesheet",
        "akhjlsdhbcjzgydhsdfnbsdfnavhegasdbsN<DBMfhsdf"]

word_length = []

for word in list:
    word_length.append(len(word))

word_length.sort(reverse=True)
print(word_length[0])

