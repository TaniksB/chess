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
        # surr_squares = []
        # pointer_x = self.x - 2
        # for i in range(0, 3):
        #     pointer_y = self.y - 2
        #     pointer_x += 1
        #     for i in range(0, 3):
        #         pointer_y += 1
        #         surr_squares.append((pointer_x, pointer_y))
        # surr_squares.remove((self.x, self.y))
        # return True if square in surr_squares else False
    
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