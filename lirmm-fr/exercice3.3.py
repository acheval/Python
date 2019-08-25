#!/bin/python3

list = []
n = 0

while True :
    print("Enter a number, type fin de saisie to terminate the program : ")
    n = input()
    try:
         int(n)
         list.append(n)
         print(list)
    except ValueError:
        if n == "fin de saisie":
            print(list)
            break
        else:
            print("Type a number, or fin de saisie")
