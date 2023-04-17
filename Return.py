# def odliczanie(zyczenia = True):
#     print("Trzy...")
#     print("Dwa...")
#     print("Jeden...")
#     if not zyczenia:
#         return
    
#     print("Szczęśliwego Nowego Roku!")

# odliczanie(False)

# def nudna_funkcja():
#     return 123

# x = nudna_funkcja()

# print("nudna_funkcja zwróciła swój wynik:", x)

# def nudna_funkcja():
#     print("'Tryb Nudny' WŁĄCZONY.")
#     return 123

# print("Ta lekcja jest interesująca!")
# nudna_funkcja()
# print("Ta lekcja jest nudna...")

# def suma_listy(lst):
#     suma = 0

#     for elem in lst:
#         suma += elem
    
#     return suma

# print(suma_listy([5, 5, 4, 0, 1, 2134, 6]))

def lista_funkcji(n):
    lista = []

    for i in range(0, n):
        lista.insert(0, i)

    return lista

print(lista_funkcji(5))