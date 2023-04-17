# user break point and decission point added

while True:

    # User pick
    print("Hello dear user, please pick what would you like to convert:", sep="")
    print("1.) Celsius to Fahrenheit -> type in 1", sep="")
    print("2.) Celsius to Kelvin -> type in 2", sep="")
    print("3.) Fahrenheit to Celsius -> type in 3", sep="")
    print("4.) Fahrenheit to Kelvin -> type in 4", sep="")
    print("5.) Kelvin to Celsius -> type in 5", sep="")
    print("6.) Kelvin to Fahrenheit -> type in 6", sep="")
    pick = int(input())

    # Branch and the result
    if pick == 1:
        celsius = float(input("Input temperature in Centigrade: "))
        print()
        celsius_to_fahrenheit = ((celsius * (9/5)) + 32)
        print(celsius, "'C is:", round(celsius_to_fahrenheit, 1), "'F")
        print("MrSz Corporation ©, Wroclaw 2023.", "All rights reserved. \n")
    elif pick == 2:
        celsius = float(input("Input temperature in Centigrade: "))
        print()
        celsius_to_kelvin = (celsius + 273.15)
        print(celsius, "'C is:", round(celsius_to_kelvin, 1), "'K")
        print("MrSz Corporation ©, Wroclaw 2023.", "All rights reserved. \n")
    elif pick == 3:
        fahrenheit = float(input("Input temperature in Fahrenheit scale: "))
        print()
        fahrenheit_to_celsius = ((fahrenheit - 32) * (5/9))
        print(fahrenheit, "'F is:", round(fahrenheit_to_celsius, 1), "'C")
        print("MrSz Corporation ©, Wroclaw 2023.", "All rights reserved. \n")
    elif pick == 4:
        fahrenheit = float(input("Input temperature in Fahrenheit scale: "))
        print()
        fahrenheit_to_kelvin = ((fahrenheit + 459.67) * (5/9))
        print(fahrenheit, "'F is:", round(fahrenheit_to_kelvin, 2), "'K")
        print("MrSz Corporation ©, Wroclaw 2023.", "All rights reserved. \n")
    elif pick == 5:
        kelvin = float(input("Enter temperature in Kelvin scale: "))
        print()
        kelvin_to_celsius = (kelvin - 273.15)
        print(kelvin, "'K is:", round(kelvin_to_celsius, 1), "'C")
        print("MrSz Corporation ©, Wroclaw 2023.", "All rights reserved. \n")
    elif pick == 6:
        kelvin = float(input("Enter temperature in Kelvin scale: "))
        print()
        kelvin_to_fahrenheit = (((kelvin - 273.15) * 1.8) + 32)
        print(kelvin, "'K is:", round(kelvin_to_fahrenheit, 2), "'F")
        print("MrSz Corporation ©, Wroclaw 2023.", "All rights reserved. \n")
    print("Would you like make another conversion?")
    print('Type in Y for "yes", or N for "no": ')
    decission = str(input("So what say you? "))
    if decission.upper() == "N":
        print()
        print("Good bye then.")        
        break


# # Variables input
# celsius = float(input("Input temperature in Centigrade: " ))
# fahrenheit = float(input("Input temperature in Fahrenheit scale: "))
# kelvin = float(input("Enter temperature in Kelvin scale: "))

# # Conversion calculations
# celsius_to_fahrenheit = ((celsius * (9/5)) + 32)
# fahrenheit_to_celsius = ((fahrenheit - 32) * (5/9))
# celsius_to_kelvin = (celsius + 273.15)
# kelvin_to_celsius = (kelvin - 273.15)
# kelvin_to_fahrenheit = (((kelvin - 273.15) * 1.8) + 32)
# fahrenheit_to_kelvin = ((fahrenheit + 459.67) * (5/9))

# Output data
# print("MrSz Corporation ©, Wroclaw 2023.", "All rights reserved. \n")
# print(celsius, "'C is:", round(celsius_to_fahrenheit, 1), "'F")
# print(fahrenheit, "'F is:", round(fahrenheit_to_celsius, 1), "'C")
# print(celsius, "'C is:", round(celsius_to_kelvin, 1), "'K")
# print(kelvin, "'K is:", round(kelvin_to_celsius, 1), "'C")
# print(kelvin, "'K is:", round(kelvin_to_fahrenheit, 2), "'F")
# print(fahrenheit, "'F is:", round(fahrenheit_to_kelvin, 2), "'K")
# heh koment dla komentu