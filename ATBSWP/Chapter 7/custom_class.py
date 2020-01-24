#!/bin/python3 

import re

vowel_regex = re.compile(r"[aeiouyAEIOUY]")
print(vowel_regex.findall("Robocop eats baby food. BABY FOOD."))

custom_range_regex = re.compile(r"[a-zA-Z0-9]")
print(custom_range_regex.findall("Robocop eats baby food. BABY FOOD."))

number_range_regex = re.compile(r"[0-5.]")
print(number_range_regex.findall("This is 2020. Not 2026."))

consonant_regex = re.compile(r"[^aeiouyAEIOUY]")
print(consonant_regex.findall("Robocop eats baby food. BABY FOOD."))
