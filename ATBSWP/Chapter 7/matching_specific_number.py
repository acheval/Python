import re

ha_regex = re.compile(r'(Ha){3}')

match_object_1 = ha_regex.search('HaHaHa') 
print(match_object_1.group())

match_object_2 = ha_regex.search('Ha') 
print(match_object_2 == None)
