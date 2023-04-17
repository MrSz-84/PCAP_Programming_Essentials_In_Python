list = [10, 1, 8, 3, 5]

list[0], list[4] = list[4], list[0]
list[1], list[3] = list[3], list[1]

print(list)

print()

list = [10, 1, 8, 3, 5]
d = len(list)

for i in range(d // 2):
    list[i], list[d - i - 1] = list[d - i -1], list[i]

print(list)
