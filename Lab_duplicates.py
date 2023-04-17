# my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
my_list = []
to_delete = []
found = ""
to_find = ""
number = ""
print("Please enter random quantity of numbers. If you want to stop type in '0'")

while True:
    if number != 0:
        number = int(input())
        if number == 0:
            continue
        my_list.append(int(number))
    else:
        break


for i in range(len(my_list)):
    to_find = my_list[i]
    for j in range(len(my_list)-(len(my_list)-(i+1)), len(my_list)):

        found = my_list[j]
        if to_find == found:
            if j in to_delete:
                continue
            to_delete.append(j)

        
to_delete.sort(reverse = True)
for i in to_delete:
    del my_list[i]

print("List containing only unicque values:")
print(my_list)































# moja_lista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# nowa_lista = []
# for liczba in moja_lista:  # Browse all numbers from the source list.
# 	if liczba not in nowa_lista:  # If the number doesn't appear within the new list...
# 		nowa_lista.append(liczba)  # ...append it here.
# moja_lista = nowa_lista[:]  # Make a copy of nowa_lista.
# print("Lista tylko z unikalnymi elementami:")
# print(moja_lista)
