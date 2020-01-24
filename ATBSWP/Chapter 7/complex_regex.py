#!/bin/python3 

import re

phone_regex_compact = re.compile(
    r"((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)"
)

phone_regex_spread = re.compile(
    r"""(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )""",
    re.VERBOSE,
)

print(phone_regex_compact.search("222-333-2313"))
print(phone_regex_spread.search("222-333-2313"))
