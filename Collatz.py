c0 = int(input("Wprowadź dowolną nieujemną liczbę całkowitą: "))

licznik = 0
while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 // 2
        licznik += 1
        print(c0)
    else:
        c0 = 3 * c0 + 1
        licznik +=1
        print(c0)
print("Liczba kroków =", licznik)