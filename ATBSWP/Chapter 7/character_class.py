#!/bin/python3 

import re

xmas_regex = re.compile(r"\d+\s\w+")

print(
    xmas_regex.findall(
        "12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, \
        7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridges"
    )
)
