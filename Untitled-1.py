# try:
#     value = int(input('Enter a natural number: '))
#     print('The reciprocal of', value, 'is', 1/value)
# except:
#     print('I do not know what to do.')


# board = []
# field = 1

# print("+-------" * 3, "+", sep="")
# for row in range(3):
#     row = []
#     print("|       " * 3, "|", sep ="")
#     for column in range(3):
#         print("|" + " " * 3 + str(field)+ " " * 3, end="")
#         row.append(field)
#         field += 1 
#     print("|")
#     print("|       " * 3,"|",sep="") 
#     print("+-------" * 3, "+", sep="")
#     board.append(row)

# print(board)


# column = []
# field = 1

# for i in range(3):
#     row = []
#     for j in range(3):
#         row.append(field)
#         field += 1 
#     column.append(row)

# board = column[:]
# print(board)




def display_board(board):
    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("|       " * 3, "|", sep ="")
        for column in range(3):
            print("|" + " " * 3 + str(board[row][column])+ " " * 3, end="") # Returnes board numeration for given value imported from board list comprehension.
        print("|")
        print("|       " * 3,"|",sep="") 
        print("+-------" * 3, "+", sep="")

# def enter_move(board):
#     ok = False
#     while not ok:
#         user_move = input("Make your move human: ")
#         ok = len(user_move) == 1 and user_move >= '1' and user_move <= '9'
#         if not ok:
#             print("This move is not allowed, try again human.")
#             continue
#         user_move = int(user_move) - 1
#         row = user_move // 3
#         column = user_move % 3
#         player = board[row][column]
#         ok = player not in ['O', 'X']
#         if not ok:
#             print("This site is taken! Make another move!")
#             continue
#     board[row][column] = 'O'



# board = [[ (row + column * 3 + 1) for row in range(3)] for column in range(3)]

# board = []
# field = 1
# for i in range(3):
#     row = []
#     for j in range(3):
#         row.append(field)
#         field += 1 
#     board.append(row)

# board[1][1] = 'X'
# print(board)
# display_board(board)
# enter_move(board)
# display_board(board)

# print(user_move)
# print(row)
# print(column)

from random import randrange
for i in range(10):
    print(randrange(8)+1)

