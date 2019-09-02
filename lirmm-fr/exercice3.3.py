#!/bin/python3

list = []

while True:
    print("Enter a number, type fin de saisie to terminate the program : ")
    n = input()
    if n == "-1":
        print("-1 is not an accepted value")
        print(list)
        break
    elif n == "fin de saisie":
        print(list)
        break
    else:
        int(n)
        list.append(n)
        print(list)

#    try:
#        int(n)
#        list.append(n)
#        print(list)
#    except ValueError:
#        if ( n == 'fin de saisie' ):
#            print(list)
#            break
#        else:
#            print("Type a number, or fin de saisie")
