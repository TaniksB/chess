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
        y_offset = abs(self.y - square[1])
        target = gamestate[square[0]][square[1]]

        if self.white is True:
            if square[1] == self.y and square[0] == self.x + 2:
                if self.moves == 0:
                    if target is None:
                        if gamestate[square[0]-1][square[1]] is None:
                            return True
            if square[1] == self.y and square[0] == self.x + 1:
                if target is None:
                        return True
        if y_offset == 1 and square[0] == self.x + 1:
            if target is not None and target.white != self.white:
                        return True
            
        if self.white is False:
             if square[1] == self.y and square[0] == self.x - 2:
                if self.moves == 0:
                    if target is None:
                        if gamestate[square[0]-1][square[1]] is None:
                            return True
             if square[1] == self.y and square[0] == self.x - 1:
                if target is None:
                        return True
        if y_offset == 1 and square[0] == self.x - 1:
            if target is not None and target.white != self.white:
                        return True
            
        return False
    
    def collision_check(self, square, gamestate):
        # To be used *after* check_line and/or check_diag!
        # Kings and Knights have no travel-through squares so they aren't getting a general-purpose function (castling is handled seperately)

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
    def __init__(self, white, x, y, moves=0):
        super().__init__(white, x, y, moves)
    
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
        return False if self.check_nighthop(square) is False else True
    
class Pawn(Piece):
    def __init__(self, white, x, y, moves=0):
        super().__init__(white, x, y, moves)

    def check_move(self, square, gamestate):
        return self.check_pawn(square, gamestate)
    
class King(Piece):
    def __init__(self, white, x, y, moves=0):
        super().__init__(white, x, y, moves)

    def check_move(self, square, gamestate):
        if gamestate[square[0]][square[1]] is not None:
            if gamestate[square[0]][square[1]].white == self.white:
                return False
        return False if self.check_onesquare(square) is False else True
    
    def check_check(self, gamestate):
        # After like 10 hours of debugging this function: https://www.reddit.com/r/ProgrammerHumor/comments/15ytbzk/codebyfaithnotbysight/
        # 1. Check if the two Pawn Attack squares contain pawns
        if self.white is True:
            right = (self.x + 1, self.y + 1)
            left = (self.x + 1, self.y - 1)
        else:
            right = (self.x - 1, self.y + 1)
            left = (self.x - 1, self.y - 1)
        squares = [right, left]
        for square in squares:
            if isinstance(gamestate[square[0]][square[1]], Pawn):
                if self.white != gamestate[square[0]][square[1]].white:
                    return True
    
        # 2. Check if the (up to) 8 Knight attack squares contain Knights
        squares = []
        to_remove = []
        squares.append((self.y + 2, self.x +1))
        squares.append((self.y + 1, self.x + 2))
        squares.append((self.y - 1, self.x + 2))
        squares.append((self.y - 2, self.x + 1))
        squares.append((self.y - 2, self.x - 1))
        squares.append((self.y - 1, self.x - 2))
        squares.append((self.y + 1, self.x - 2))
        squares.append((self.y + 2, self.x - 1))
        for square in squares:
            for num in square:
                if num > 8 or num < 1:
                    to_remove.append(square)
        for square in to_remove:
            if square in squares:
                squares.remove(square)
        for square in squares:
            if isinstance(gamestate[square[0]][square[1]], Knight):
                if self.white != gamestate[square[0]][square[1]].white:
                    return True

        # 3. Check if the enemy King can reach the current King's location
        # 4. Find all enemy Queens, Bishops and Rooks and see if they can reach the current King's location
        for file in gamestate:
            for square in gamestate[file]:
                if isinstance(gamestate[file][square], King):
                    if gamestate[file][square].white != self.white:
                        enemy_king = gamestate[file][square]
                if isinstance(gamestate[file][square], Queen) or isinstance(gamestate[file][square], Bishop) or isinstance(gamestate[file][square], Rook):
                    if gamestate[file][square].check_move((self.x, self.y), gamestate):
                        if gamestate[file][square].white != self.white:
                            return True
        if enemy_king.check_move((self.y, self.x), gamestate):
            return True
        return False
    
    def __repr__(self):
        if self.white:
            return f"White King at ({self.x}, {self.y}) with {self.moves} moves played"
        return f"Black King at ({self.x}, {self.y}) with {self.moves} moves played"
    
    def castle_short(self, gamestate):
        # 1 Check if King and Rook have not moved
        if self.white:
            partner = gamestate[1][8]
            squares = ((1, 6), (1, 7))
        else:
            partner = gamestate[8][8]
            squares = ((8, 6), (8, 7))
        if not isinstance(partner, Rook):
            return False
        if self.moves != 0 or partner.moves != 0:
            return False
        # 2 Check if King is in check
        if self.check_check(gamestate):
            return False
        # 3 Create dummy Kings at the King's destination square and travel square and see if they are in check. These never get saved to gamestate!
        for square in squares:
            dummy = King(self.white, square[0], square[1])
            if dummy.check_check(gamestate):
                return False
        # 4 Check if the King can reach his target square (...using check_line and not his own check_move)
        if not self.check_line(squares[1]):
            return False
        # 5 Check if the Rook can reach his target square
        if not partner.check_move(squares[0], gamestate):
            return False
        return True
    
    def castle_long(self, gamestate):
        if self.white:
            partner = gamestate[1][1]
            squares = ((1, 4), (1, 3))
        else:
            partner = gamestate[8][1]
            squares = ((8, 4), (8, 3))
        if not isinstance(partner, Rook):
            return False
        if self.moves != 0 or partner.moves != 0:
            return False
        if self.check_check(gamestate):
            return False
        for square in squares:
            dummy = King(self.white, square[0], square[1])
            if dummy.check_check(gamestate):
                return False
        if not self.check_line(squares[1]):
            return False
        if not partner.check_move(squares[0], gamestate):
            return False
        return True
        