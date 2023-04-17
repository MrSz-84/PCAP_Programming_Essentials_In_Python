blokow = int(input("Wprowadź liczbę bloków: "))

wysokosc = 0
suma_wyk_blokow = 0
kolejna_warstwa = 0

while suma_wyk_blokow <= blokow:
    if blokow - kolejna_warstwa < 0:
        break
    wysokosc += 1
    suma_wyk_blokow = suma_wyk_blokow + wysokosc
    kolejna_warstwa = suma_wyk_blokow + wysokosc + 1

print("Wysokość piramidy wynosi:", wysokosc)

