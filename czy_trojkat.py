# def czy_trojkat(a, b, c):
#     if a + b <= c:
#         return False
#     if b + c <= a:
#         return False
#     if c + a <= b:
#         return False
#     return True

# def czy_trojkat(a, b, c):
#     if a + b <= c or b + c <= a or c + a <= b:
#         return False
#     return True

# print(czy_trojkat(1, 1, 1))
# print(czy_trojkat(1, 1, 3))


def czy_trojkat(a, b, c):
    return a + b > c and b + c > a and c + a > b

def czy_prostokatny(a, b, c):
    if not czy_trojkat(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > c and a > b:
        return a ** 2 == c ** 2 + b ** 2


a = float(input("Wprowadź długość pierwszego boku: "))
b = float(input("Wprowadź długość drugiergo boku: "))
c = float(input("Wprowadź długość trzeciego boku: "))

if czy_trojkat(a, b, c):
    print("Z boków o takiej długości można zbudować trójkąt.")
else:
    print("Z boków o takiej długości nie można zbudować trójkąta.")
if czy_prostokatny(a, b, c):
    print("Trójkąt jest prostokątny.")
else:
    print("Trójkąt nie jest prostokątny.")