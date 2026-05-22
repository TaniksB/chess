from pieces import Pawn, Rook, Knight, Bishop, Queen, King
from rich import print

def render(gamestate, move_white):
    if move_white:
        render_white(gamestate)
    else:
        render_black(gamestate)



def render_white(gamestate):
    board = "8 "
    pointer_x = 1
    pointer_y = 8
    square_white = True
    while pointer_y > 0:
        # Set Piece type
        if gamestate[pointer_y][pointer_x] is None:
            symbol = " "
        if isinstance(gamestate[pointer_y][pointer_x], Pawn):
            symbol = "P"
        if isinstance(gamestate[pointer_y][pointer_x], Rook):
            symbol = "R"
        if isinstance(gamestate[pointer_y][pointer_x], Knight):
            symbol = "N"
        if isinstance(gamestate[pointer_y][pointer_x], Bishop):
            symbol = "B"
        if isinstance(gamestate[pointer_y][pointer_x], Queen):
            symbol = "Q"
        if isinstance(gamestate[pointer_y][pointer_x], King):
            symbol = "K"
        # Set Piece color
        if gamestate[pointer_y][pointer_x] != None and gamestate[pointer_y][pointer_x].white:
            symbol = f"[bold white]{symbol}[/bold white]"
        else:
            symbol = f"[bold black]{symbol}[/bold black]"
        # Set Square color and build full string
        if square_white:
            square = f"[white][[/white]{symbol}[white]][/white]"
        else:
            square = f"[black][[/black]{symbol}[black]][/black]"
        board += square
        if pointer_x == 8:
            # add row number here later
            pointer_x = 1
            pointer_y -= 1
            if pointer_y != 0:
                board += f"\n{pointer_y} "
        else:
            pointer_x += 1
            square_white = not square_white
    board += "\n   a  b  c  d  e  f  g  h"
    print(board)




def render_black(gamestate):
    board = "1 "
    pointer_x = 1
    pointer_y = 1
    square_white = True
    while pointer_y < 9:
        # Set Piece type
        if gamestate[pointer_y][pointer_x] is None:
            symbol = " "
        if isinstance(gamestate[pointer_y][pointer_x], Pawn):
            symbol = "P"
        if isinstance(gamestate[pointer_y][pointer_x], Rook):
            symbol = "R"
        if isinstance(gamestate[pointer_y][pointer_x], Knight):
            symbol = "N"
        if isinstance(gamestate[pointer_y][pointer_x], Bishop):
            symbol = "B"
        if isinstance(gamestate[pointer_y][pointer_x], Queen):
            symbol = "Q"
        if isinstance(gamestate[pointer_y][pointer_x], King):
            symbol = "K"
        # Set Piece color
        if gamestate[pointer_y][pointer_x] != None and gamestate[pointer_y][pointer_x].white:
            symbol = f"[bold white]{symbol}[/bold white]"
        else:
            symbol = f"[bold black]{symbol}[/bold black]"
        # Set Square color and build full string
        if square_white:
            square = f"[white][[/white]{symbol}[white]][/white]"
        else:
            square = f"[black][[/black]{symbol}[black]][/black]"
        board += square
        if pointer_x == 8:
            # add row number here later
            pointer_x = 1
            pointer_y += 1
            if pointer_y != 9:
                board += f"\n{pointer_y} "
        else:
            pointer_x += 1
            square_white = not square_white
    board += "\n   a  b  c  d  e  f  g  h"
    print(board)

