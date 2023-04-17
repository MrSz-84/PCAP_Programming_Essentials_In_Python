slowo_bez_samoglosek = ""

# Poproś użytkownika o wprowadzenie słowa
# i przypisz je do zmiennej slowo_uzytkownika

slowo_uzytkownika = str(input("Wpisz dowolne słowo: "))

for litera in slowo_uzytkownika.upper():
    # Uzupełnij pętlę for poniżej.
    if litera == "A":
        continue
    if litera == "E":
        continue
    if litera == "I":
        continue
    if litera == "O":
        continue
    if litera == "U":
        continue
    if litera == "Y":
        continue
    else:
        slowo_bez_samoglosek += litera
print(slowo_bez_samoglosek)
