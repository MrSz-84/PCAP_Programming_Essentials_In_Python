# %%
# checks if given numbers set is sudoku or not
def checkup(numbers, lst):
    return numbers == sorted(list(lst))


# board creation
sudoku = []
for x in range(9):
    ok = False
    while not ok:
        row = input('Enter data row number #' + str(x + 1) + ': ')
        ok = row.isdigit() and len(row) == 9
        if not ok:
            print('Lenght or data format invalid. Please check the data.')     
            continue
    sudoku.append(row)

# refferance set of digits
numbers = [chr(ord('0') + x) for x in range(1, 10)]

# rows check
for row in sudoku:
    ok = checkup(numbers, row)
    if not ok:
        break

# columns check
if ok:
    for col in range(9):
        columns = []
        for row in range(9):
            columns.append(sudoku[row][col])
        ok = checkup(numbers, columns)
        if not ok:
            break

# squares check
if ok:
    for num in range(0, 9, 3):
        for coll in range(0, 9, 3):
            squares = []
            square = ''
            for roww in range(3):
                thing = sudoku[roww + num][0 + coll:3 + coll]
                square += thing
            squares.append(square)
            ok = checkup(numbers, squares[0])
            if not ok:
                break

if ok:
    print('Those numbers create Sudoku.')
else:
    print('Those numbers don\'t create Sudoku.')
