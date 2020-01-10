import re

phone_num_regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")

match_object = phone_num_regex.search("My number is 415-555-4242")

print("Phone number found: " + match_object.group())

# Grouping with parenthesis

phone_num_regex_groups = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
match_object = phone_num_regex_groups.search("My number is 415-555-4242")

print(match_object.group(0))
print(match_object.group(1))
print(match_object.group(2))
print(match_object.group())
print(match_object.groups())

area_code, main_number = match_object.groups()
print(area_code)
print(main_number)

# Escape characters

phone_num_regex_parenthesis = re.compile(r"(\(\d\d\d\))-(\d\d\d-\d\d\d\d)")
match_object = phone_num_regex_parenthesis.search("My number is (415)-555-4242")
print(match_object.group(1))
print(match_object.group(2))
print(match_object.group())
