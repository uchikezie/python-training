name = input('Enter your name: ')
Temp_celsius = float(input('Enter Temperature in Celsius: '))
Temp_fahren = (Temp_celsius*1.8)+32
#print(name + ' your Temperature is ', Temp_fahren,'\u00B0 F')  

if Temp_fahren >= float(20) and Temp_fahren <= float(49):
    print(name + ' it is a cold day, ensure you are properly covered')
elif Temp_fahren >= float(50) and Temp_fahren <= float(69):
    print(name + ' it is a cool day')
elif Temp_fahren >= float(70) and Temp_fahren <= float(85):
    print(name + ' it is a warm day to take a ride')
elif Temp_fahren > float(85):
    print(name + ', this is a very hot day, ensure you stay hrdrated')


#elif age >= 20 and age <= 100:
#     print('Hi, you are wrong, try again!')