#!/bin/python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip

text = pyperclip.paste() # get data from the clipboard

#Separate line and add stars.

lines = text.split('\n') # split the text
for i in range(len(lines)): #loop through all indexes in the "lines" list
    lines[i] = '* ' + lines[i] # add a star to each string in the "lines" list

text = '\n'.join(lines)

pyperclip.copy(text)
