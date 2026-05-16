# Things to check:
# 1. Can the target square be reached with the Piece's movement?
# 2. Is the target square empty or does it contain a Piece of the opposite color?
# 3. For pieces except Knights, are the in-between squares empty?

class Piece:
    # moves can be specified for debug purposes but shouldn't under normal circumstances
    def __init__(self, white, x, y, moves=0):
        self.white = white
        # True = white, False = black

        self.x = x
        self.y = y
        self.moves = moves

    # These functions determine if a square can be reached with a specific movement mode
    # To-be-written function already checks if the target square actually exists, so none of these functions do
    def check_line(self, square):
        # Rook, Queen
        if self.x == square[0] and self.y == square[1]:
            return False
        if self.x == square[0] or self.y == square[1]:
            return True
        return False

    def check_diag(self, square):
        # Bishop, Queen
        x_offset = abs(self.x - square[0])
        y_offset = abs(self.y - square[1])
        if x_offset == 0:
            return False
        return True if x_offset == y_offset else False
    
    def check_onesquare(self, square):
        # King
        x_offset = abs(self.x - square[0])
        y_offset = abs(self.y - square[1])
        if x_offset == 0 and y_offset == 0:
            return False
        if x_offset == 0 or x_offset == 1:
            if y_offset == 0 or y_offset == 1:
                return True
        return False
    
    def check_nighthop(self, square):
        # kNight
        x_offset = abs(self.x - square[0])
        y_offset = abs(self.y - square[1])
        if x_offset == 0 and y_offset == 0:
            return False
        if x_offset == 2 and y_offset == 1:
            return True
        if x_offset == 1 and y_offset == 2:
            return True
        return False
    
    def check_pawn(self, square, gamestate):
        # pawn...
        # en passant is not supported yet... god help me
        x_offset = abs(self.x - square[0])
        target = gamestate[square[0]][square[1]]

        if self.white is True:
            if square[0] == self.x and square[1] == self.y + 2:
                if self.moves == 0:
                    if target is None:
                        return True
            if square[0] == self.x and square[1] == self.y + 1:
                if target is None:
                        return True
        if x_offset == 1 and square[1] == self.y + 1:
            if target is not None:
                        return True
            
        if self.white is False:
             if square[0] == self.x and square[1] == self.y - 2:
                if self.moves == 0:
                    if target is None:
                        return True
             if square[0] == self.x and square[1] == self.y - 1:
                if target is None:
                        return True
        if x_offset == 1 and square[1] == self.y - 1:
            if target is not None:
                        return True
            
        return False
    
    def collision_check(self, square, gamestate):
        # To be used *after* check_line and/or check_diag!
        # Kings, Pawns and Knights only ever need to look at 1 target square so they aren't getting a general-purpose function

        x = 0
        y = 0
        if self.x > square[0]:
            x = -1
        elif self.x < square[0]:
            x = 1
        if self.y > square[1]:
            y = -1
        elif self.y < square[1]:
            y = 1
        squares = []
        squares.append((self.x + x, self.y + y))
        travel_square = squares[-1]
        while travel_square != square:
            travel_square = (squares[-1][0] + x, squares[-1][1] + y)
            squares.append(travel_square)
        for sq in squares:
            if sq == squares[-1]:
                if gamestate[sq[0]][sq[1]] is not None:
                    if gamestate[sq[0]][sq[1]].white == self.white:
                        return False
            else:
                if gamestate[sq[0]][sq[1]] is not None:
                    return False
        return True
    
class Rook(Piece):
    def __init__(self, white, x, y):
        super().__init__(white, x, y)
    
    # Castling is handled elsewhere

    def check_move(self, square, gamestate):
        if self.check_line(square) is False:
            return False 
        if self.collision_check(square, gamestate) is False:
            return False
        return True
    
class Bishop(Piece):
    def __init__(self, white, x, y):
        super().__init__(white, x, y)

    def check_move(self, square, gamestate):
        if self.check_diag(square) is False:
            return False
        if self.collision_check(square, gamestate) is False:
            return False
        return True
    
class Queen(Piece):
    def __init__(self, white, x, y):
        super().__init__(white, x, y)

    def check_move(self, square, gamestate):
        if self.check_diag(square) is False and self.check_line(square) is False:
            return False
        if self.collision_check(square, gamestate) is False:
            return False
        return True
    
class Knight(Piece):
    def __init__(self, white, x, y):
        super().__init__(white, x, y)

    def check_move(self, square, gamestate):
        if gamestate[square[0]][square[1]] is not None:
            if gamestate[square[0]][square[1]].white == self.white:
                return False
        return False if self.check_nighthop is False else True