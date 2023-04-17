list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
biggest = list[0]

for i in range(1, len(list)):
    if list[i] > biggest:
        biggest = list[i]

print(biggest)

list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
biggest = list[0]

for i in list:
    if i > biggest:
        biggest = list[i]

print(biggest)

list1 = [17, 3, 11, 5, 1, 9, 7, 15, 13]
biggest1 = list1[0]

for i in list1[1:]:
    if i > biggest1:
        biggest1 = i

print(biggest1)