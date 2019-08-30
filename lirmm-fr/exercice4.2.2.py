#!/bin/python

import sys

# Reprenez le script et faites que le seuil et la longueur lg soient
# passés en paramètres

lg = int(sys.argv[1])

# Déclarer une variable seuil dans laquelle vous mémorisez la valeur
# 75

seuil = int(sys.argv[2])

# Écriver une structure conditionnelle pour vérifier que lg est
# supérieure au seuil et afficher un message "ORF valide" dans ce
# cas, et un message "ORF invalide" dans le cas contraire

if lg > seuil:
    print("ORF valide")
else:
    print("ORF invalide")