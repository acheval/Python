#!/bin/python

# Reprenez le script et faites que le seuil et la longueur lg soient
# saisis (plutôt qu'écrits dans le script)

# Déclarer une variable lg dans laquelle vous mémoriser la longueur
# d'une ORF d'un ARN

print("Enter the value for lg: ")
lg = int(input())

# Déclarer une variable seuil dans laquelle vous mémorisez la valeur
# 75

print("Enter the value for the threshold: ")
seuil = int(input())

# Écriver une structure conditionnelle pour vérifier que lg est
# supérieure au seuil et afficher un message "ORF valide" dans ce
# cas, et un message "ORF invalide" dans le cas contraire

if lg > seuil:
    print("ORF valide")
else:
    print("ORF invalide")