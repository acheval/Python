import sys

def collatz(number):
    if number == 1:
        return number
    elif number <= 0:
        print('Collatz sequence works best with non zero or positive integers')
    else:
        while number != 1:
            if number % 2 == 0:
                number = number // 2
                print(number)
            else:
                number = 3 * number + 1
                print(number)

print('Enter a number to find it\'s Collatz sequence')

try:
    user_number = int(input())
except ValueError:
    print('You must enter an integer')
    sys.exit()

print(collatz(user_number))
