#!/bin/python3 

import re

phone_number_regex_nogroup = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")  # no groups
match_object = phone_number_regex_nogroup.search(
    "Cell: 415-555-9999, Work: 212-555-0000"
)
print(match_object.group())
print(phone_number_regex_nogroup.findall("Cell: 415-555-9999, Work: 212-555-0000"))

phone_number_regex_group = re.compile(r"(\d\d\d)-(\d\d\d)-(\d\d\d\d)")  # has groups
print(phone_number_regex_group.findall("Cell: 415-555-9999, Work: 212-555-0000"))
