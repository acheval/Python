#!/bin/python3

# Reprenez l'exercice de la Boucle for et faites deux nouvelles
# versions du script pour que le nombre soit passé en paramètre.

import sys

n = int(sys.argv[1])

for i in range(n):
    print(i)
