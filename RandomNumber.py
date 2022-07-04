#This program displays random numbers from 1 to 9 when called

import random
#from webbrowser import get

def getAnswer(answer_number):
    if answer_number == 1:
        return 'It is one '
    elif answer_number == 2:
        return 'The number is 2'
    elif answer_number == 3:
        return 'This is the 3rd number'
    elif answer_number == 4:
        return 'This is the 4th number'
    elif answer_number == 5:
        return 'This is 5'
    elif answer_number == 6:
        return 'This is the 6th'
    elif answer_number == 7:
        return 'This is the 7th'
    elif answer_number == 8:
        return 'This is the 8th'
    elif answer_number == 9:
        return 'this is the 9th'
    

r = random.randint(1,9)
ugonna = getAnswer(r)
print(ugonna)
