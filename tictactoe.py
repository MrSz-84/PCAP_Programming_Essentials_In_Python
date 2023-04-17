# Import section

from random import randrange


# Functions section.

def display_board(board):
    print("+-------" * 3, "+", sep = "")
    for row in range(3):
        print("|       " * 3, "|", sep = "")
        for column in range(3):
            print("|" + " " * 3 + str(board[row][column]) + " " * 3, end = "")
        print("|")
        print("|       " * 3, "|", sep = "") 
        print("+-------" * 3, "+", sep = "")


def player1_move(board):

    ok = False
    while not ok:
        user_move = input("Make your move Player 1: ")
        ok = len(user_move) == 1 and user_move >= '1' and user_move <= '9'
        if not ok:
            print("This move is not allowed, try again human.")
            continue
        user_move = int(user_move) - 1
        row = user_move // 3
        column = user_move % 3
        player = board[row][column]
        ok = player not in ['O', 'X']
        if not ok:
            print("This site is taken! Make another move!")
            continue
    board[row][column] = 'O'


def player2_move(board):
    ok = False
    while not ok:
        user_move = input("Make your move Player 2: ")
        ok = len(user_move) == 1 and user_move >= '1' and user_move <= '9'
        if not ok:
            print("This move is not allowed, try again human.")
            continue
        user_move = int(user_move) - 1
        row = user_move // 3
        column = user_move % 3
        player = board[row][column]
        ok = player not in ['O', 'X']
        if not ok:
            print("This site is taken! Make another move!")
            continue
    board[row][column] = 'X'


def make_list_of_free_fields(board):
    global free_field
    free_field = []
    for row in range(3):
        for column in range(3):
            if board[row][column] not in ['O', 'X']:
                free_field.append((row, column))
    return(free_field)


def victory_for(board, sign):
    for r in range(3):
        for c in range(3):
            if sign == board[0][c] == board[1][c] == board[2][c]:
                return True
            elif sign == board[r][0] == board[r][1] == board[r][2]:
                return True
            elif sign == board[0][0] == board[1][1] == board[2][2]:
                return True
            elif sign == board[0][2] == board[1][1] == board[2][0]:
                return True
    return None


def cpu_move(board):
    ok = False
    while not ok:
        cpu_move = randrange(8)
        row = cpu_move // 3
        column = cpu_move % 3
        cpu = board[row][column]
        ok = cpu not in ['O', 'X']
        if not ok:
            continue
    board[row][column] = 'X'


def is_pvp(game_type):
    if game_type == 1:
        return "Player 2"
    else:
        return "CPU"

# Main code section

# board = [[ (row + column * 3 + 1) for row in range(3)] for column in range(3)]
# Same thing only using list comprehension


board = []
field = 1
for i in range(3):
    row = []
    for j in range(3):
        row.append(field)
        field += 1 
    board.append(row)

print("""
Available game types:
1. For Player vs Player
2. For Player vs CPU
""")

right = False
while not right:
    game_type = input("Make your choice: ")
    right = len(game_type) == 1 and game_type >= '1' and game_type <= '2'
    if not right:
        print("The number must be 1 or 2")
        continue

    if int(game_type) == 1:
        make_list_of_free_fields(board)
        player1_turn = True
        game_on = True
        while len(free_field) >= 1:
            display_board(board)
            if player1_turn:
                player1_move(board)
                sign = 'O'
                victor = victory_for(board, sign)
                if victor:
                    sign = 'O'
                    break
            elif not player1_turn:
                player2_move(board)
                sign = 'X'
                victor = victory_for(board, sign)
                if victor:
                    sign = 'X'
                    break
            player1_turn = not player1_turn
            make_list_of_free_fields(board)

    else:
        board[1][1] = 'X'
        make_list_of_free_fields(board)
        player1_turn = True
        game_on = True
        while len(free_field) >= 1:
            display_board(board)
            if player1_turn:
                player1_move(board)
                sign = 'O'
                victor = victory_for(board, sign)
                if victor:
                    sign = 'O'
                    break
            elif not player1_turn:
                cpu_move(board)
                sign = 'X'
                victor = victory_for(board, sign)
                if victor:
                    sign = 'X'
                    break
            player1_turn = not player1_turn
            make_list_of_free_fields(board)

display_board(board)
if victor and sign == 'O':
    print("Player 1 wins!")
elif victor and sign == 'X':
    print(is_pvp(game_type), " wins!")
elif victor == None and sign in ('O', 'X'):
    print("It's a draw!")
