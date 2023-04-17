my_list = []

for i in range(5):
    my_list.append(i + 1)

print(my_list)

print()
print()

sum = 0
for i in range(len(my_list)):
    sum += my_list[i]

print(sum)

print()
print()

my_list2 = [10, 1, 8, 3, 5]
sum = 0
for i in my_list2:
    sum += i
print(sum)