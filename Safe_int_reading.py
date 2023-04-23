def readint(prompt, min, max):
    v = ''
    try:
        v = int(input(prompt))
        assert max >= v >= min
    except ValueError:
        print('Błąd: wprowadzono nieprawidłową liczbę')
    except AssertionError:
        print('Błąd: podana liczba jest spoza dozwolonego zakresu (min..max)')
    return v


v = readint("Podaj liczbe od -10 do 10: ", -10, 10)

print("Liczba to:", v)
