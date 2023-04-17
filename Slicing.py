# Kopiowanie całej listy.
lista_1 = [1]
lista_2 = lista_1[:]
lista_1[0] = 2
print(lista_2)

# Kopiowanie części listy.
list = [10, 8, 6, 4, 2]
new_list = list[1:3]
print(new_list)

# Kopiowanie części listy.
lista = [10, 8, 6, 4, 2]
new_list1 = lista[1:len(lista)]
print(new_list1)


listalista = [10, 8, 6, 4, 2]
nowa_lista = listalista[1:-1]
print(nowa_lista)

listalista = [10, 8, 6, 4, 2]
nowa_lista = listalista[1:0]
print(nowa_lista)

lista = [10, 8, 6, 4, 2]
nowa_lista = lista[:3]
print(nowa_lista)

lista = [10, 8, 6, 4, 2]
nowa_lista = lista[3:]
print(nowa_lista)

lista = [10, 8, 6, 4, 2]
del lista[1:3]
print(lista)

lista = [10, 8, 6, 4, 2]
del lista[:]
print(lista)
