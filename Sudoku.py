# %%
# Reads if given numbers are sudoku or not
from sys import stdin


def checkup(checkup_lst):  # check if each sudoku row is valid
    for row in checkup_lst:
        is_sudoku_rows = row
        for i in digits_pattern:
            if i not in is_sudoku_rows:
                return False
    return True


def column_rearrange(sudoku):  # nested list for each column of sudoku as feed for checkup
    for row in range(9):
        temporary_list = []
        for column in range(9):
            temporary_list.append(sudoku[column][row])
        checkup_lst.append(temporary_list)
    return checkup(checkup_lst)


# Prepare data input from user. Clean out end of line signs and return data to a list.
# print('Check if given numbers are Sudoku or not.\n'
#       'Data has to be 9 rows, 9 digits per row\n'
#       'NO SPACES ARE ALLOWED!')
# bucket = stdin.readlines(9*9)
bucket = ['295743861\n', '431865927\n', '876192543\n', '387459216\n', '612387495\n',
          '549216738\n', '763524189\n', '928671354\n', '154938672\n']
before_sudoku = []
sstring = ''
for index in bucket:
    for digit in index:
        if not digit.isdigit():
            continue
        sstring += digit
    before_sudoku.append(sstring)
    sstring = ''

# Creating sudoku grid for checkup if requirements are met.

sudoku = [[int(row) for row in column] for column in before_sudoku]
del before_sudoku, sstring
digits_pattern = [i + 1 for i in range(len(sudoku))]

# Boolean checkups

checkup_lst = sudoku[:]
rows_ok = checkup(checkup_lst)
print(rows_ok)
checkup_lst.clear()
cols_ok = column_rearrange(sudoku)
print(cols_ok)

# Try to think how to make check of 3x3 list made from 3x3 slices of sudoku list.
