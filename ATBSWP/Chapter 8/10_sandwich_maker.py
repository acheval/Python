import pyinputplus as pyip

total = 0
sandwich = []

print('Please, choose your bread: ')
bread = {'White': 0.5, 'Wheat': 0.75, 'Sourdough': 1}
bread_choice = pyip.inputMenu(list(bread), numbered = True)
total = total + bread[bread_choice]
sandwich.append(bread_choice)

print('Please, choose your protein: ')
protein = {'Chicken': 0.4, 'Turkey': 0.45, 'Tofu': 0.55, 'Ham': 0.60}
protein_choice = pyip.inputMenu(list(protein), numbered = True)
total = total + protein[protein_choice]
sandwich.append(protein_choice)

print('Do you want cheese ?')
cheese = pyip.inputYesNo(prompt = 'Yes/No ')

if cheese == 'yes':
    print('Which type of cheese do you want ?')
    cheese_type = {'Cheddar': 0.9,'Swiss': 1.2,'Mozzarella': 0.75}
    cheese_choice = pyip.inputMenu(list(cheese_type), numbered = True, default = None)
    total = total + cheese_type[cheese_choice]
    sandwich.append(cheese_choice)
else:
    cheese_type = 'No cheese'
    sandwich.append(cheese_type)

print('Do you want any sauce with your sandwich ?')
sauce = pyip.inputYesNo(prompt = 'Yes/No ')

if sauce == 'yes':
    print('Which sauce do you want ?')
    sauce_type = {'Mayo': 0.2,'Ketchup': 0.2,'Mustard': 0.2}
    sauce_choice = pyip.inputMenu(list(sauce_type), numbered = True, default = None)
    total = total + sauce_type[sauce_choice]
    sandwich.append(sauce_choice)
else:
    sauce_type = 'No sauce'
    sandwich.append(sauce_type)

print('How many sandwiches do you need ?')
number_of_sandwiches = pyip.inputInt(min = 1)
total = total * number_of_sandwiches

print(sandwich)
print("Montant total: " + str(round(total, 2)) + " Euros")
