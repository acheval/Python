import re

bat_regex = re.compile(r'Bat(wo)+man')

match_object_1 = bat_regex.search('The Adventure of Batman')
try:
    print(match_object_1.group())
except:
    print('No matches found')

match_object_2 = bat_regex.search('The Adventure of Batwoman')
print(match_object_2.group())

match_object_3 = bat_regex.search('The Adventure of Batwowoman')
print(match_object_3.group())


