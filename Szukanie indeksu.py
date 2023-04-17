list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(list)):
    found = list[i] == to_find
    if found:
        break

if found:
    print("Element found at index:", i)
else:
    print("brak")

print()

wylosowano = [5, 11, 9, 42, 3, 49]
obstawiono = [3, 7, 11, 42, 34, 49]
trafiono = 0

for i in obstawiono:
    if i in wylosowano:
        trafiono += 1

print(trafiono)

