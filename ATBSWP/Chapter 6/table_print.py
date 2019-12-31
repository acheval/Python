#!/bin/python3

table_data = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def print_table(table):
    col_width = [0] * len(table) #initialize col_width with the length of table
    for items in range(0, len(table)): #for each item in range 0 to the length of table do:
        for strings in range(0, len(table[items])): # for each string in range 0 to the length of the current table's item, do:
            if len(table[items][strings]) > col_width[items]: #if the length of the table's item's string is greater than the item's of the col_width, do:
                col_width[items] = len(table[items][strings]) #set the col_width's item as the length of the table's item's string

    for row in range(0, len(table[0])): #for each item between 0 and length of the first item in the table
        for col in range(0, len(table)): #for each item between 0 and the length of the table
            print(table[col][row].rjust(col_width[col]), end= " ") #print table's columns and rows, right justify with the value of col in col_width, append a space after each column.
        print(' ') # add a blank string after each row
        
print_table(table_data)
