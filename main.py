import rich
import sys
from pieces import Pawn, Rook, Knight, Bishop, King, Queen
from render import render
from setup import setup
from interpret_move import interpret_move

def main():
    move_white = True
    checkmate = 0 # This variable is never refreshed, need to add checkmate / draw detection in the future
    gamestate = setup()
    print("Instructions:\n -<reset> to restart the game\n -<quit> to close the program\n -Algebraic notation for any kind of move")
    while checkmate == 0:
        render(gamestate, move_white)
        color = "White" if move_white is True else "Black"

        # Finds the King which is needed later
        for file in gamestate:
                for square in gamestate[file]:
                    if isinstance(gamestate[file][square], King):
                        if gamestate[file][square].white == move_white:
                            king = gamestate[file][square]

        move = input(f"{color} to move: ")
        if move == "reset":
            move_white = True
            gamestate = setup()
            continue
        elif move == "quit":
            sys.exit()
        int_move = interpret_move(move)
        if int_move == 1:
            new_gamestate = castle_short(gamestate, king)
        elif int_move == 2:
            new_gamestate = castle_long(gamestate, king)
        else:
            new_gamestate = gamestate
            actor = None
            actor_type = get_actor_type(int_move["piece"])
            for file in gamestate:
                for square in gamestate[file]:
                    if isinstance(gamestate[file][square], actor_type):
                        if gamestate[file][square].white == move_white:
                            if gamestate[file][square].check_move((int_move["y"], int_move["x"]), gamestate):
                                    actor = gamestate[file][square]
            if actor is None:
                new_gamestate = None
            else:
                new_gamestate[actor.x][actor.y], new_gamestate[int_move["x"]][int_move["y"]] = None, actor
        if new_gamestate is None or king.check_check(new_gamestate):
            print(f"Move {move} is invalid!")
            continue
        else:
            gamestate = new_gamestate
            move_white = not move_white

        

            
        

        

def castle_short(gamestate, king):
    if king.castle_short(gamestate):
        if king.white:
            gamestate[1][7], gamestate[1][5] = king, None
            gamestate[1][6], gamestate[1][8] = gamestate[1][8], None
        else:
            gamestate[8][7], gamestate[8][5] = king, None
            gamestate[8][6], gamestate[8][8] = gamestate[1][8], None
        return gamestate
    return None

def castle_long(gamestate, king):
    if king.castle_long(gamestate):
        if king.white:
            gamestate[1][3], gamestate[1][5] = king, None
            gamestate[1][4], gamestate[1][1] = gamestate[1][1], None
        else:
            gamestate[8][3], gamestate[8][5] = king, None
            gamestate[8][4], gamestate[8][1] = gamestate[1][1], None
        return gamestate
    return None

def get_actor_type(id):
    conversion = {
        "P": Pawn,
        "R": Rook,
        "N": Knight,
        "B": Bishop,
        "Q": Queen,
        "K": King
    }
    if id in conversion:
        return conversion[id]
    return 1

main()