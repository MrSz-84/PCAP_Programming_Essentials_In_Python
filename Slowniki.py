# slownik = {"kot" : "gato", "pies" : "perro", "koń" : "caballo"}
# numery_telefonow = {'szef' : 5551234567, 'Marian' : 22657854310}
# pusty_slownik = {}

# # print(slownik)
# # print(numery_telefonow)
# # print(pusty_slownik)

# print(slownik['kot'])
# print(numery_telefonow['Marian'])


# slownik = {"kot" : "gato", "pies" : "perro", "koń" : "caballo"}
# slowa = ['kot', 'lew', 'koń']

# for slowo in slowa:
#     if slowo in slownik:
#         print(slowo, "->", slownik[slowo])
#     else:
#         print("W słowniku nie istnieje słowo:", slowo)


# # Przykład 1:
# slownik = {
#            "kot": "gato",
#            "pies": "perro",
#            "koń": "caballo"
#            }

# # Przykład 2:
# numery_telefonow = {'szef': 5551234567,
#                     'Zuza': 22657854310
#                     }

# keys() method
# slownik = {"kot" : "gato", "pies" : "perro", "koń" : "caballo"}

# for klucz in slownik.keys():
#     print(klucz, "->", slownik[klucz])

# sorted() function
# slownik = {"kot" : "gato", "pies" : "perro", "koń" : "caballo"}

# for klucz in sorted(slownik.keys()):
#     print(klucz, "->", slownik[klucz])

# ithem() method

# slownik = {"kot" : "gato",  "pies" : "perro", "koń" : "caballo"}

# for polski, hiszpanski in slownik.items():
#     print(polski, "->", hiszpanski)

# # values() method

# slownik = {"kot" : "gato",  "pies" : "perro", "koń" : "caballo"}

# for hiszpanski in slownik.values():
#     print(hiszpanski)

# asigning new value to existing key

# slownik = {
#           "kot" : "gato",  
#           "pies" : "perro", 
#           "koń" : "caballo"
#           }

# slownik["kot"] = "gatito"
# print(slownik)


# adding new entry

# slownik = {
#           "kot" : "gato",  
#           "pies" : "perro", 
#           "koń" : "caballo"
#           }

# slownik["świnka"] = "paperas"
# print(slownik)

# adding new entry with update() method

# slownik = {
#           "kot" : "gato",  
#           "pies" : "perro", 
#           "koń" : "caballo"
#           }

# slownik.update({"kurczak" : "pollo"})
# print(slownik)

# key deletion

slownik = {
          "kot" : "gato",  
          "pies" : "perro", 
          "koń" : "caballo"
          }

del slownik["pies"]
print(slownik)

# key deletion with popitem() method - deleting last item

slownik = {
          "kot" : "gato",  
          "pies" : "perro", 
          "koń" : "caballo"
          }

slownik.popitem()
print(slownik)
