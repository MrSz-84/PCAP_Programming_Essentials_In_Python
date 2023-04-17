list = []
swapped = True
num = int(input("Ile elementów chcesz posortować: "))

for i in range(num):
    val = float(input("Wprowadź element listy: "))
    list.append(val)

while swapped:
    swapped = False
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            swapped = True
            list[i], list[i + 1] = list[i + 1], list[i]

print("\nPosortowane:")
print(list)


lista = [8,10,6,2,4]
lista.sort()
print(lista)
lista = [8,10,6,2,4]
lista.reverse()
print(lista)
lista = [8,10,6,2,4]
lista.sort(reverse = True)
print(lista)