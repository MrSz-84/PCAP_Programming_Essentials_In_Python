najwieksza_liczba = -99999999
licznik = 0

while True:
    liczba = int(input("Wprowadz liczbe lub wpisz -1, aby zakonczyc: "))
    if liczba == -1:
        break
    licznik += 1
    if liczba > najwieksza_liczba:
        najwieksza_liczba = liczba

if licznik != 0:
    print("Najwieksza liczba wynosi", najwieksza_liczba)
else:
    print("Nie wprowadzono żadnej wartości.")