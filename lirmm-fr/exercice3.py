#!/bin/python3

L = [987, 65, 43, 21, 43, 98, 145]

#Afficher la liste L

print('List L:', L)

#Compter le nombre d'occurrences de 43 dans L

print('L has', L.count(43), 'occurences of 43')

#Ajouter le nombre 25 en dernière position ; afficher L

L.append(25)
print(L)

#Afficher la longueur de la liste

print('L contains', len(L), 'entries')

#Supprimer un élément 43 de L ; afficher L

L.remove(43)
print(L)

#Refaire 2.

print('L has', L.count(43), 'occurences of 43')

#Renverser l'ordre de L ; afficher L

L.reverse()
print(L)

#Trier L ; afficher L

L.sort()
print(L)

#Supprimer le dernier élément ; afficher L

del L[-1]
print(L)
