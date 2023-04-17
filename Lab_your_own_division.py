# %%
# My code
# def mysplit(string):
#     slice_index = 0
#     lst = []
#     ch = 0
#     if len(string) == 0:
#         return lst
#     else:
#         while ch < len(string):
#             for ch in range(len(string)):
#                 if string[ch] == " ":
#                     lst.append(string[slice_index:ch])
#                     slice_index = ch + 1
#                 else:
#                     continue
#             lst.append(string[string.rfind(" ") + 1:])
#             lst_ = []
#             for i in lst:
#                 if i == '':
#                     continue
#                 else:
#                     lst_.append(i)
#             lst = lst_
#             return lst
#
#
# print(mysplit("Być albo nie być, oto jest pytanie"))
# print(mysplit("Być albo nie być,oto jest pytanie"))
# print(mysplit("   "))
# print(mysplit(" abc "))
# print(mysplit(""))

# %%
# Code with Cico Academy help
def mysplit(string):
    if string == '' or string.isspace():        # zwróć [], jeśli ciąg jest pusty lub zawiera tylko spacje
        return []
    lst = []                                    # przygotuj listę do zwrotu
    word = ''                                   # przygotuj słowo, aby zbudować kolejne słowa
    inword = not string[0].isspace()            # sprawdź, czy obecnie znajdujemy się w słowie (tzn. jeśli łańcuch zaczyna się od słowa)
    for ch in string:                           # iteruj przez wszystkie znaki w łańcuchu
        if inword:                              # jeśli jesteśmy obecnie w łańcuchu znaków ...
            if not ch.isspace():                # ... a obecny znak nie jest spacją...
                word = word + ch                # ... zaktualizuj bieżące słowo
            else:
                lst.append(word)                # ... w przeciwnym razie doszliśmy do końca słowa, więc musimy dodać je do listy ...
                inword = False                  # ... i zasygnalizować fakt, że jesteśmy teraz poza słowem
        else:
            if not ch.isspace():                # jeśli jesteśmy poza słowem i dotarliśmy do znaku innego niż biały ...
                inword = True                   # ... oznacza, że zaczęło się nowe słowo, więc musimy o tym pamiętać i ...
                word = ch                       # ... przechować pierwszą literę nowego słowa
            else:
                pass
    if inword:                                  # jeśli opuściliśmy łańcuch i istnieje niepusty łańcuch w słowie, musimy zaktualizować listę
        lst.append(word)
    return lst                                  # zwraca listę do invokera


print(mysplit("Być albo nie być, oto jest pytanie"))
print(mysplit("Być albo nie być,oto jest pytanie"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
