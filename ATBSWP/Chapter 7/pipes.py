#!/bin/python3 

import re

# Find first occurence

hero_regex = re.compile(r'Batman|Tina Fey')

match_object_1 = hero_regex.search('Batman and Tina Fey')
match_object_2 = hero_regex.search('Tina Fey and Batman')

print(match_object_1.group())
print(match_object_2.group())


bat_regex = re.compile(r'Bat(man|mobile|copter|bat)')
match_object = bat_regex.search('Batmobile lost a wheel')
print(match_object.group())
print(match_object.group(1))

