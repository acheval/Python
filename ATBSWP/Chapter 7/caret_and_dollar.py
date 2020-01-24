#!/bin/python3 

import re

begins_with_hello = re.compile(r"^Hello")

print(begins_with_hello.search("Hello World !"))
print(begins_with_hello.search("hello world !"))
print(begins_with_hello.search("He said hello World !"))

ends_with_number = re.compile(r"\d$")
print(ends_with_number.search("Your number is 42"))
print(ends_with_number.search("Your number is 42. "))
print(ends_with_number.search("Your number is forty two"))

whole_string_is_num = re.compile(r"^\d+$")
print(whole_string_is_num.search("1234567890"))
print(whole_string_is_num.search("12345xyz67890"))
print(whole_string_is_num.search("12345 67890"))
