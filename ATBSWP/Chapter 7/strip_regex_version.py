#!/bin/python3 

import re


def strip_string(context, strip_character):
    if strip_character == "":
        regex_strip_whitespace = re.compile(r"^\s+|\s+$")
        stripped_context = regex_strip_whitespace.sub("", context)
        print(stripped_context)
    else:
        regex_strip_character = re.compile(r"[" + strip_character + "]")
        stripped_context = regex_strip_character.sub("", context)
        print(stripped_context)


print("Enter a string:")
string = str(input())

print("Enter a character to strip:")
character = str(input())

strip_string(string, character)
