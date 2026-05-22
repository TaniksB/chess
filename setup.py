
from pieces import Rook, Knight, Bishop, King, Queen, Pawn
from render import render

def setup():
    # Builds the starting position's gamestate
    gamestate = {}

    for i1 in range(1, 9):
        gamestate[i1] = {}
        for i2 in range(1, 9):
            gamestate[i1][i2] = None

    gamestate[1][1] = Rook(True, 1, 1)
    gamestate[1][2] = Knight(True, 1, 2)
    gamestate[1][3] = Bishop(True, 1, 3)
    gamestate[1][4] = Queen(True, 1, 4)
    gamestate[1][5] = King(True, 1, 5)
    gamestate[1][6] = Bishop(True, 1, 6)
    gamestate[1][7] = Knight(True, 1, 7)
    gamestate[1][8] = Rook(True, 1, 8)

    for i in range(1, 9):
        gamestate[2][i] = Pawn(True, 2, i)

    for i in range(1, 9):
        gamestate[7][i] = Pawn(False, 7, i)

    gamestate[8][1] = Rook(False, 8, 1)
    gamestate[8][2] = Knight(False, 8, 2)
    gamestate[8][3] = Bishop(False, 8, 3)
    gamestate[8][4] = Queen(False, 8, 4)
    gamestate[8][5] = King(False, 8, 5)
    gamestate[8][6] = Bishop(False, 8, 6)
    gamestate[8][7] = Knight(False, 8, 7)
    gamestate[8][8] = Rook(False, 8, 8)

    return gamestate


gst = setup()
render(gst, True)

