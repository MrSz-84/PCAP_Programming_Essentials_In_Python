numbers = [10, 5, 7, 2, 1]
print("List contains:", numbers)

numbers[0] = 111
print("New list contains:", numbers)

numbers[1] = numbers[4]
print("Newest list contains:", numbers)

numbers[1] = numbers[4]
print(numbers[0])
numbers[1] = numbers[4]
print(numbers)

print("List lenght:", len(numbers))

del numbers[1]
print(len(numbers))
print(numbers)


liczby = [111, 7, 2, 1]
print(liczby[-1])
print(liczby[-2])