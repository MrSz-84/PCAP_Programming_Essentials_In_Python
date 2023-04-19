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
    checkup_lst.clear()
    for row in range(9):
        temporary_list = []
        for column in range(9):
            temporary_list.append(sudoku[column][row])
        checkup_lst.append(temporary_list)
    return checkup(checkup_lst)


def squares_rearrange(sudoku):
    checkup_lst.clear()
    for row_counter in range(3):
        for col_counter in range(3):
            temporary_list = []
            for roww in range(3):
                for col in range(3):
                    temporary_list.append(
                        sudoku[col + 3 * row_counter][roww + 3 * col_counter])
            checkup_lst.append(temporary_list)
    return checkup(checkup_lst)


# Prepare data input from user. Clean out end of line signs and return data to a list.
print('Check if given numbers are Sudoku or not.\n'
      'Data has to be 9 rows, 9 digits per row\n'
      'NO SPACES ARE ALLOWED!')
bucket = stdin.readlines(9*9)

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
cols_ok = column_rearrange(sudoku)
squares_ok = squares_rearrange(sudoku)

if rows_ok and cols_ok and squares_ok:
    print('Given data are valid. Congrats you have a Sudoku!')
else:
    print('I\'m so sorry. Your data don\'t make a Sudoku :(')
