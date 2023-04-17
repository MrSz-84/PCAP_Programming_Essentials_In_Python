EMPTY = "-"
ROOK = "ROOK"
BISHOP = "BISHOP"
PAWN = "PAWN"
KNIGHT = "KNIGHT"
KING = "KING"
QUEEN = "QUEEN"
chessboard = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    chessboard.append(row)

chessboard[0][0] = ROOK
chessboard[0][7] = ROOK

chessboard[0][1] = KNIGHT
chessboard[0][6] = KNIGHT

chessboard[0][2] = BISHOP
chessboard[0][5] = BISHOP

chessboard[0][3] = QUEEN

chessboard[7][4] = KING

chessboard[1][0] = PAWN
chessboard[1][1] = PAWN
chessboard[1][2] = PAWN
chessboard[1][3] = PAWN
chessboard[1][4] = PAWN
chessboard[1][5] = PAWN
chessboard[1][6] = PAWN
chessboard[1][7] = PAWN



chessboard[7][0] = ROOK
chessboard[7][7] = ROOK

chessboard[7][1] = KNIGHT
chessboard[7][6] = KNIGHT

chessboard[7][2] = BISHOP
chessboard[7][5] = BISHOP

chessboard[7][3] = QUEEN

chessboard[0][4] = KING

chessboard[6][0] = PAWN
chessboard[6][1] = PAWN
chessboard[6][2] = PAWN
chessboard[6][3] = PAWN
chessboard[6][4] = PAWN
chessboard[6][5] = PAWN
chessboard[6][6] = PAWN
chessboard[6][7] = PAWN

print(chessboard)