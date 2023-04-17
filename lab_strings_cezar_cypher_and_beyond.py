# # %%
# # Cezar's cypher with code value grater than one
# offset = int(input('Enter a whole number: '))
# txt = input("Enter a message: ")
# cypher = ''
# for char in txt:
#     if not char.isalpha():
#         continue
#     char = char.upper()
#     code = ord(char) + offset
#     while code > 90:
#         if code > ord('Z'):
#             code = ord('A') + (code - 90)
#     cypher += chr(code)
#
# print(cypher)


offset = int(input('Enter a whole number: '))
txt = input("Enter a message: ")
cypher = ''
for char in txt:
    if not char.isalpha():
        cypher += char
    elif char == char.upper():
        code = ord(char) + offset
        while code > 90:
            if code > ord('Z'):
                code = ord('@') + (code - 90)
        cypher += chr(code)
    elif char != char.upper():
        code = ord(char) + offset
        while code > 122:
            if code > ord('z'):
                code = ord('`') + (code - 122)
        cypher += chr(code)

print(cypher)


# # wprowadz tekst do zaszyfrowania
# tekst = input("Wpisz wiadomosc: ")
#
# # wprowadz poprawna wartosc przesuniecia (powtarzaj do skutku)
# przesuniecie = 0
#
# while przesuniecie == 0:
#     try:
#         przesuniecie = int(input("Podaj przesuniecie szyfru (1..25): "))
#         if przesuniecie not in range(1,26):
#         	raise ValueError
#     except ValueError:
#         przesuniecie = 0
#     if przesuniecie == 0:
#         print("Niepoprawna wartosc przesuniecia!")
#
# szyfr = ''
#
# for char in tekst:
#     # czy to litera?
#     if char.isalpha():
#         # przesun jego kod
#         kod = ord(char) + przesuniecie
#         # znajdz kod pierwszej litery (drukowane lub male litery)
#         if char.isupper():
#             pierwsza = ord('A')
#         else:
#             pierwsza = ord('a')
#         # wprowadz poprawki
#         kod -= pierwsza
#         kod %= 26
#         # dodaj do wiadomosci zaszyfrowany znak
#         szyfr += chr(pierwsza + kod)
#     else:
#         # dodaj do wiadomosci pierwotny znak
#         szyfr += char
#
# print(szyfr)
