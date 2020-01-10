import re

# Matches 0 or 1 occurence

bat_regex = re.compile(r'Bat(wo)?man')
match_object_1 = bat_regex.search('The Adventure of Batman')
print(match_object_1.group())

match_object_2 = bat_regex.search('The Adventure of Batwoman')
print(match_object_2.group())

try:
    match_object_3 = bat_regex.search('The Adventure of Batwowoman')
    print(match_object_3.group())
except:
    print('No match found')

phone_regex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
match_object_4 = phone_regex.search('My number is 415-555-4242')
print(match_object_4.group())

match_object_5 = phone_regex.search('My number is 555-4242')
print(match_object_5.group())
