#!/bin/python3 

import re

name_regex = re.compile(r"First Name: (.*) Last Name: (.*)")
matching_object = name_regex.search("First Name: Al Last Name: Sweigart")
print(matching_object.group(1))
print(matching_object.group(2))

non_greedy_regex = re.compile(r"<.*?>")
matching_object = non_greedy_regex.search("<To serve man> for dinner.>")
print(matching_object.group())

greedy_regex = re.compile(r"<.*>")
matching_object = greedy_regex.search("<To serve man> for dinner.>")
print(matching_object.group())
