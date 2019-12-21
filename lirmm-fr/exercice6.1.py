#!/bin/python3

import math
import sys

n = int(sys.argv[1])

while True:
    f = math.factorial(n)
    print(n, "has a factorial of", f)
    break
