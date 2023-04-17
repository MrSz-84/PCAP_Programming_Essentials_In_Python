# %%
# Reads if given numbers are sudoku or not
from sys import stdin

# quick check if git control and staging works from ubuntu
# another check from vsc from ubuntu machine

# print('Check if given numbers are Sudoku or not.\n'
#       'Data has to be 9 rows, 9 digits per row\n'
#       'NO SPACES ARE ALLOWED!')
# bucket = stdin.readlines(9*9)
bucket = ['295743861\n', '431865927\n', '876192543\n', '387459216\n', '612387495\n', '549216738\n', '763524189\n', '928671354\n', '154938672\n']
before_sudoku = []
sstring = ''
for index in bucket:
    for digit in index:
        if not digit.isdigit():
            continue
        sstring += digit
    before_sudoku.append(sstring)
    sstring = ''
for i in before_sudoku:
    print(i, len(i))

