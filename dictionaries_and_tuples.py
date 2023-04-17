# class_1 = {}

# while True:
#     name = input("Type in student's name: ")
#     if name == '':
#         break

#     result = int(input("Type in the result of the student (0-10): "))
#     if result not in range(0, 11):
#         break

#     if name in class_1:
#         class_1[name] += (result,)
#     else:
#         class_1[name] = (result,)

# for name in sorted(class_1.keys()):
#     sum = 0
#     counter = 0
#     for result in class_1[name]:
#         sum += result
#         counter += 1
#     print(name, ":", sum / counter)


# tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
# duplicates = tup.count(2)

# print(duplicates)    # wyjście: 4


# d1 = {'Adam Smith':'A', 'Judy Paxton':'B+'}
# d2 = {'Mary Louis':'A', 'Patrick White':'C'}
# d3 = {}

# for item in (d1, d2):
#     d3.update(item)
# print(d3)

# lst = ["car", "Ford", "flower", "Tulip"]

# tup = tuple(lst)
# print(tup)

# colors = (("green", "#008000"), ("blue", "#0000FF"))

# col_dict = dict(colors)

# print(col_dict)


