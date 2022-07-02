
import string


name = input('Enter your name: ')

if len(name) < 3:
    print(name + ' the name you entered is too short')
elif len(name) >= 3 and len(name) <= 25:
    print(name + ' the name you entered is valid') 
else:
    print(name + ' the name you entered is too long')
