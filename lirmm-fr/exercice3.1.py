#!/bin/python3

# Déclarer une variable lg dans laquelle vous mémoriser la longueur d'une ORF d'un ARN

lg = 65

# Déclarer une variable seuil dans laquelle vous mémorisez la valeur 75

seuil = 75

# Écriver une structure conditionnelle pour vérifier que lg est supérieure au seuil et afficher un message "ORF valide" dans ce cas, et un message "ORF invalide" dans le cas contraire

if lg > seuil:
    print("ORF valide")
else:
    print("ORF invalide")
