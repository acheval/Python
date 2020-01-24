#!/bin/python3 

def password_strength_check(password):
    import re

    password_regex = re.compile(
        r"""(
                    (?=\S*[A-Z]+)                                       #lookahead matches at least one upper case character
                    (?=\S*[a-z]+)                                       #lookahead matches at least one lower case character
                    (?=\S*\d+)                                          #lookahead matches at least one digit
                    (?=\S*[!@#\"\'\\$%^&*()\-_\{\}\[\]?/.,<>|+=~`]+)    #lookahead matches any one of those characters
                    \S{8,}                                              #matches at least 8 non whitespace characters
                    )""",
        re.VERBOSE,
    )
    password_assessed = password_regex.search(password)
    if password_assessed is not None:
        print("Password is strong")
    else:
        print(password_assessed + " is a weak password")


print("Please enter a password: ")
input_password = str(input())

password_strength_check(input_password)
