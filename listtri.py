#!/usr/bin/python

list = [3,6,1,8,5]
print(list)
counter = 0
endList = len(list)-1

while counter < endList:

    print("counter = " + str(counter))

    if list[counter] > list[counter+1]:

        c = list[counter]
        list[counter] = list[counter+1]
        list[counter+1] = c
        print("c = " + str(c))

    counter = counter+1

print(sorted(list))
