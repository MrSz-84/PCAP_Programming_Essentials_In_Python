# def message():
#     print("Inpute a value: ")

# message()
# a = int(input())
# message()
# b = int(input())
# message()
# c = int(input())


# def wiadomosc(liczba):
#     print("Wprowadź liczbę:", liczba)

# liczba = 1234
# wiadomosc(1)
# print(liczba)

# def wiadomosc(co, wartosc, master):
#     print("Wprowadź", co, "produktu: ", wartosc, master)

# wiadomosc("kod", 11254, "miszczu")
# wiadomosc("cenę", 1.5, "miszczu")
# wiadomosc("datę ważnośći", "12 marca 1985", "miszczu")

# def my_function(a, b , c):
#     print(a, b, c)

# my_function(1, 2 ,3)

# def introduction(name, surname):
#     print("Hi, I'm", name, surname)

# introduction(surname = "Luke", name = "Skywalker")
# introduction("Krzysztof", "Bondek")
# introduction("Clark", "Kent")
# introduction(surname = "Master", name = "Yoda")
# introduction(name = "Scrum", surname = "Master")

# def address(street, postal_code, city):
#     print("Your addres is:", street, postal_code, city)

# u = input("Street: ")
# m = input("City: ")
# k = input("Postal code: ")

# address( u, m, k)


# przykład 1
def subtra(a, b):
    print(a - b)

subtra(5, 2)    # daje na wyjściu: 3
subtra(2, 5)    # daje na wyjściu: -3


# przykład 2
def subtra(a, b):
    print(a - b)

subtra(a=5, b=2)    # daje na wyjściu: 3
subtra(b=2, a=5)    # daje na wyjściu: 3

# przykład 3
def subtra(a, b):
    print(a - b)

subtra(5, b=2)    # daje na wyjściu: 3
subtra(5, 2)    # daje na wyjściu: 3
