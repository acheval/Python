#!/bin/python3 

#/bin/python3

cat_names=[]
while True:
    print('Enter the name of the cat ' + str(len(cat_names) + 1) + ' (Or enter nothing to stop.):')

    name = input()
    if name == '':
        break
    cat_names = cat_names + [name]

print('The cat names are: ')
for name in cat_names: print (' ' + name)
