def czy_trojkat(a, b, c):
    return a + b > c and b + c > a and c + a > b

def heron(a, b, c):
    p = (a + b + c) / 2
    return((p * (p - a) * (p - b) * (p - c)) ** 0.5)

def pole_powierzchni(a, b, c):
    if not czy_trojkat:
        return None
    else:
        return heron(a, b, c)
    

# a = float(input("Wprowadź długość pierwszego boku: "))
# b = float(input("Wprowadź długość drugiergo boku: "))
# c = float(input("Wprowadź długość trzeciego boku: "))

print(pole_powierzchni(1, 1, 2 ** 0.5))