squares = [x ** 2 for x in range(10)]
print(squares)

binary = [2 ** i for i in range(8)]
print(binary)

odds = [x for x in squares if x % 2 != 0]
print(odds)

szachownica = []
PUSTY = ""

# for i in range(8):
#         rzad = [PUSTY for i in range(8)]
#         szachownica.append(rzad)
# print(szachownica)

szachownica = [[PUSTY for i in range(8)] for j in range(8)]
print(szachownica)