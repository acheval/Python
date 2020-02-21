import pyinputplus as pyip

response = pyip.inputNum('Enter num: ', min = 4)
print(response)

response = pyip.inputNum('Enter num: ', greaterThan = 4)
print(response)

response = pyip.inputNum('>', min = 4, lessThan = 6)
print(response)
