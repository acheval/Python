#!/bin/python3 

import re

greedy_ha_regex = re.compile(r"(Ha){3,5}")
matching_object_1 = greedy_ha_regex.search("HaHaHaHaHaHa")
print(matching_object_1.group())

nongreedy_ha_regex = re.compile(r"(Ha){3,5}?")
matching_object_2 = nongreedy_ha_regex.search("HaHaHaHaHaHa")
print(matching_object_2.group())
