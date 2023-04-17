# bedziemy przechowywac obecnie najwieksza liczbe tutaj
najwiekszaLiczba = -999999999

# wprowadz pierwsza wartosc
liczba = int(input("Wprowadz liczbe lub wpisz -1 aby zatrzymac: "))

# jesli liczba nie jest rowna -1, bedziemy kontynuowac
while liczba != -1:
    # czy liczba jest wieksza niz najwiekszaLiczba?
    if liczba > najwiekszaLiczba:
        # tak, uaktualnij najwiekszaLiczba
        najwiekszaLiczba = liczba
    # wprowadz nastepna liczba
    liczba = int(input("Wprowadz liczbe lub wpisz -1 aby zatrzymac: "))

# wyswietl najwiekszaLiczba
print("Najwieksza liczba wynosi:", najwiekszaLiczba)
