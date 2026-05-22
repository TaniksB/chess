# Takes input string, returns a dictionary with piece, target_x, target_y, and optionally piece_x or piece_y and promotion, or simply 1 or 2 for castling (1 = short)
# piece_x and piece_< are optional and default to None

def interpret_move(move_string):
    # Strip whitespace from beginning and end
    move_string = move_string.strip()
    # Get castling out of the way first
    if move_string == "0-0":
        return 1
    if move_string == "0-0-0":
        return 2
    # Set up move dict
    move = {
        "piece": None,
        "x": None,
        "y": None,
        "piece_x": None,
        "piece_y": None,
        "promotion": None
    }
    pieces = ["R", "N", "B", "Q", "K"]
    # Remove x and # as those are checked on every move already
    stripped_string = move_string.replace("x", "")
    stripped_string = stripped_string.replace("#", "")
    # Determine promotion
    if "=" in stripped_string:
        if stripped_string[-1] in pieces[:-1]:
            move["promotion"] = stripped_string[-1]
            stripped_string = stripped_string[:-2]
    # Determine piece
    if stripped_string[0] in pieces:
        move["piece"] = stripped_string[0]
    else:
        move["piece"] = "P"
    # Determine y
    if stripped_string[-1].isdecimal():
        if int(stripped_string[-1]) > 0 and int(stripped_string[-1]) < 9:
            move["y"] = int(stripped_string[-1])
    else:
        return 0
    # Determine x
    conversion = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8
    }
    if stripped_string[-2] in conversion:
        move["x"] = conversion[stripped_string[-2]]
    else:
        return 0
    # Determine if piece_x or piece_y are specified
    if stripped_string[0] in pieces:
        stripped_string = stripped_string[1:]
    if len(stripped_string) == 3:
        if stripped_string[0].isdecimal():
            if int(stripped_string[0]) > 0 and int(stripped_string[0]) < 9:
                move["piece_y"] = int(stripped_string[0])
        else:
            if stripped_string[0] in conversion:
                move["piece_x"] = conversion[stripped_string[0]]
    return move



