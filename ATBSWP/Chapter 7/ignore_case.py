#!/bin/python3 

import re

robocop = re.compile(r"robocop", re.I)
print(robocop.search("Robocop is part man, part machine, all cop").group())
print(robocop.search("ROBOCOP protects the innocent").group())
print(
    robocop.search(
        "Al, why does yout programming book talks about robocop so\
    much ?"
    ).group()
)
