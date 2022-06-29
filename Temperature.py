#A program that asks for your name and Temperature in Celsuis and converts it to fahrenheit
name = input('Enter your name: ')
Temp_celsius = float(input('Enter Temperature in Celsius: '))
Temp_fahren = (Temp_celsius*1.8)+32
# print(name)
print(name + ' your Temperature is ', Temp_fahren,'\u00B0F')  

# print('\u00B0')