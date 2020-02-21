import pyinputplus as pyip

while True:
    prompt = 'Tu veux savoir comment garder un idiot occupé pendant des heures\
    ?\n'
    response = pyip.inputYesNo(prompt, yesVal='oui', noVal='non')
    if response == 'non':
        print('Merci, passe une bonne journée !')
        break

