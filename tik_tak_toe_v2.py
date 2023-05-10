from random import randrange


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print('+-------' * 3 + '+')
    for row in range(3):
        print('|       ' * 3 + '|')
        for col in range(3):
            print('|   ' + str(board[row][col]) + '   ', end='')
        print('|')
        print('|       ' * 3 + '|')
        print('+-------' * 3 + '+')


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    ok = False
    while not ok:
        player_input = input('Enter your move: ')
        ok = not player_input < '1' and player_input <= '9' and len(player_input) == 1 \
            and player_input.isdigit()
        if not ok:
            print('Your choice isn\'t valid. Pick a number in range 1-9.')
            continue
        free_fields = make_list_of_free_fields(board)
        player_pick = free_fields[int(player_input) - 1]
        ok = player_pick != 'taken'
        if not ok:
            print('This field is taken, pick another one.')
            continue
    board[player_pick[0]][player_pick[1]] = 'ϴ'
    display_board(board)


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ('x', 'ϴ'):
                free_fields.append((row, col))
            else:
                free_fields.append('taken')
    return free_fields


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    for rc in range(3):
        win = board[rc][0] == sign and board[rc][1] == sign and board[rc][2] == sign
        if win:
            return sign
        win = board[0][rc] == sign and board[1][rc] == sign and board[2][rc] == sign
        if win:
            return sign
        win = board[0][0] == sign and board[1][1] == sign and board[2][2] == sign
        if win:
            return sign
        win = board[0][2] == sign and board[1][1] == sign and board[2][0] == sign
        if win:
            return sign
    return None


def draw_move(board):
    # The function draws the computer's move and updates the board.
    ok = False
    while not ok:
        cpu_move = randrange(1, 10)
        free_fields = make_list_of_free_fields(board)
        player_pick = free_fields[int(cpu_move) - 1]
        ok = player_pick != 'taken'
        if not ok:
            continue
    board[player_pick[0]][player_pick[1]] = 'x'
    display_board(board)


board = [[(i + 1 + (j * 3)) for i in range(3)] for j in range(3)]
board[1][1] = 'x'
display_board(board)
victor = None
while True:
    if make_list_of_free_fields(board).count('taken') >= 9:
        break
    enter_move(board)
    victor = victory_for(board, 'ϴ')
    if victor is not None:
        break
    if make_list_of_free_fields(board).count('taken') >= 9:
        break
    draw_move(board)
    victor = victory_for(board, 'x')
    if victor is not None:
        break

if victor == 'ϴ':
    print('You won human')
elif victor == 'x':
    print('Lord of the bytes has won!')
else:
    print('It\'s a draw')
