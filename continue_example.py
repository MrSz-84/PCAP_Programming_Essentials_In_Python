najwieksza_liczba = -9999999
licznik = 0

liczba = int(input("Wprowadz liczbe lub wpisz -1 aby zakonczyc: "))
while liczba != -1:
    if liczba == -1:
        continue
    licznik += 1

    if liczba > najwieksza_liczba:
        najwieksza_liczba = liczba
    liczba = int(input("Wprowadz liczbe lub wpisz -1, aby zakonczyc: "))

if licznik:
    print("Najwieksza liczba wynosi", najwieksza_liczba)
else:
    print("Nie wprowadzono zadnej wartosci.")