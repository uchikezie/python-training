#This program defines the function (Hello) and calls the function to print (Howdy)
def Hello():
    print('Howdy!')
    print('Howdy!!')
    print('Howdy!!!')
Hello()
Hello()

#Adding a name variable to the Hello program and calling the Hello function
def Hello(name):
    print('Your name is ' + name)
Hello('Ugonna')
Hello ('Chikezie')

def plusOne(number):
    return number + 1
Newnumber = plusOne(5)
print(Newnumber)

#A list of animals and how to separate them in list format
print('Ugonna, below is a list of animals:')
print('cat, dog, elephant, etc. ')
print('Cat', 'dog', 'Elephant')
print('cat', 'dog', 'elephant', sep = 'AB')
print('Cat', 'dog', 'Elephant ', end='')
