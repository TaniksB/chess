import unittest
from pieces import Piece, Rook, Bishop, Queen, Knight, King, Pawn

class TestPieces(unittest.TestCase):
    def test_rook(self):
        Rook = Piece(True, 5, 5)
        self.assertTrue(Rook.check_line((2, 5)))
        self.assertFalse(Rook.check_line((3, 8)))

    def test_bishop(self):
        Bishop = Piece(True, 5, 5)
        self.assertTrue(Bishop.check_diag((2, 2)))
        self.assertFalse(Bishop.check_diag((7, 5)))

    def test_knight(self):
        Knight = Piece(True, 5, 5)
        self.assertTrue(Knight.check_nighthop((6, 3)))
        self.assertFalse(Knight.check_nighthop((1, 1)))

    def test_king(self):
        King = Piece(True, 5, 5)
        self.assertTrue(King.check_onesquare((4, 6)))
        self.assertFalse(King.check_onesquare((5, 7)))
    
    def test_pawn(self):
        PawnW = Piece(True, 5, 2, 0)
        PawnB = Piece(False, 6, 3, 3)
        gamestate = {4: {3: None}, 5: {2: PawnW, 3: None, 4: None}, 6: {1: None, 2: None, 3: PawnB, 4: None}}
        self.assertTrue(PawnW.check_pawn((5, 3), gamestate))
        self.assertTrue(PawnW.check_pawn((5, 4), gamestate))
        self.assertTrue(PawnW.check_pawn((6, 3), gamestate))
        self.assertFalse(PawnW.check_pawn((4, 3), gamestate))
        
        self.assertTrue(PawnB.check_pawn((6, 2), gamestate))
        self.assertFalse(PawnB.check_pawn((6, 4), gamestate))
        self.assertFalse(PawnB.check_pawn((6, 1), gamestate))
        self.assertTrue(PawnB.check_pawn((5, 2), gamestate))



    
    def test_collision(self):
        QueenW = Piece(True, 1, 3)
        KnightB = Piece(False, 2, 4)
        PawnW = Piece(True, 2, 8)
        PawnB = Piece(False, 4, 2)
        KnightW = Piece(True, 4, 3)
        RookW = Piece(True, 4, 4)
        BishopB = Piece(False, 4, 6)
        KingW = Piece(True, 5, 7)
        BishopW = Piece(True, 7, 4)
        RookB = Piece(False, 8, 2)
        collision_gamestate = {1: {1: None, 2: None, 3: QueenW, 4: None, 5: None, 6: None, 7: None, 8: None},
                            2: {1: None, 2: None, 3: None, 4: KnightB, 5: None, 6: None, 7: None, 8: PawnW},
                            3: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None},
                            4: {1: None, 2: PawnB, 3: KnightW, 4: RookW, 5: None, 6: BishopB, 7: None, 8: None}, 
                            5: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: KingW, 8: None}, 
                            6: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None}, 
                            7: {1: None, 2: None, 3: None, 4: BishopW, 5: None, 6: None, 7: None, 8: None}, 
                            8: {1: None, 2: RookB, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None}}
        
        self.assertTrue(RookW.collision_check((4, 6), collision_gamestate))
        self.assertFalse(RookW.collision_check((7, 4), collision_gamestate))
        self.assertTrue(RookW.collision_check((2, 4), collision_gamestate))
        self.assertFalse(RookW.collision_check((4, 2), collision_gamestate))

        self.assertTrue(BishopB.collision_check((2, 8), collision_gamestate))
        self.assertTrue(BishopB.collision_check((5, 7), collision_gamestate))
        self.assertFalse(BishopB.collision_check((1, 3), collision_gamestate))
        self.assertFalse(BishopB.collision_check((8, 2), collision_gamestate))

    def test_Rook(self):
        RookW = Rook(True, 4, 4)
        BishopW = Piece(True, 6, 4)
        BishopB = Piece(False, 4, 7)
        KnightB = Piece(False, 7, 4)
        gamestate = {1: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None},
                    2: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None},
                    3: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None},
                    4: {1: None, 2: None, 3: None, 4: RookW, 5: None, 6: None, 7: BishopB, 8: None}, 
                    5: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None}, 
                    6: {1: None, 2: None, 3: None, 4: BishopW, 5: None, 6: None, 7: None, 8: None}, 
                    7: {1: None, 2: None, 3: None, 4: KnightB, 5: None, 6: None, 7: None, 8: None}, 
                    8: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None}}
        
        self.assertTrue(RookW.check_move((4, 6), gamestate))
        self.assertTrue(RookW.check_move((4, 7), gamestate))
        self.assertFalse(RookW.check_move((4, 8), gamestate))
        self.assertTrue(RookW.check_move((5, 4), gamestate))
        self.assertFalse(RookW.check_move((6, 4), gamestate))
        self.assertFalse(RookW.check_move((7, 4), gamestate))
        self.assertFalse(RookW.check_move((1, 6), gamestate))

    def test_Bishop(self):
        BishopW = Bishop(True, 5, 5)
        RookW = Rook(True, 4, 4)
        RookB = Rook(False, 3, 3)
        KnightB = Piece(False, 7, 3)
        PawnB = Piece(False, 7, 6)
        gamestate = {1: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None},
                    2: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None},
                    3: {1: None, 2: None, 3: RookB, 4: None, 5: None, 6: None, 7: None, 8: None},
                    4: {1: None, 2: None, 3: None, 4: RookW, 5: None, 6: None, 7: None, 8: None}, 
                    5: {1: None, 2: None, 3: None, 4: None, 5: BishopW, 6: None, 7: None, 8: None}, 
                    6: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None}, 
                    7: {1: None, 2: None, 3: KnightB, 4: None, 5: None, 6: PawnB, 7: None, 8: None}, 
                    8: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None}}
        
        self.assertTrue(BishopW.check_move((3, 7), gamestate))
        self.assertTrue(BishopW.check_move((7, 3), gamestate))

        self.assertFalse(BishopW.check_move((4, 4), gamestate))
        self.assertFalse(BishopW.check_move((3, 3), gamestate))
        self.assertFalse(BishopW.check_move((2, 2), gamestate))
        self.assertFalse(BishopW.check_move((7, 6), gamestate))

    def test_Queen(self):
        QueenW = Queen(True, 4, 4)
        gamestate = {1: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None},
                    2: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None},
                    3: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None},
                    4: {1: None, 2: None, 3: None, 4: QueenW, 5: None, 6: None, 7: None, 8: None}, 
                    5: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None}, 
                    6: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None}, 
                    7: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None}, 
                    8: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None}}
        
        self.assertTrue(QueenW.check_move((1, 4), gamestate))
        self.assertTrue(QueenW.check_move((1, 7), gamestate))

        self.assertFalse(QueenW.check_move((1, 5), gamestate))

    def test_Knight(self):
        KnightW = Knight(True, 4, 4)
        RookW = Rook(True, 5, 6)
        KnightB = Knight(False, 6, 5)
        gamestate = {1: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None},
                    2: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None},
                    3: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None},
                    4: {1: None, 2: None, 3: None, 4: KnightW, 5: None, 6: None, 7: None, 8: None}, 
                    5: {1: None, 2: None, 3: None, 4: None, 5: None, 6: RookW, 7: None, 8: None}, 
                    6: {1: None, 2: None, 3: None, 4: None, 5: KnightB, 6: None, 7: None, 8: None}, 
                    7: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None}, 
                    8: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None}}
        
        self.assertTrue(KnightW.check_move((6, 5), gamestate))
        self.assertTrue(KnightW.check_move((3, 6), gamestate))

        self.assertFalse(KnightW.check_move((5, 6), gamestate))
        self.assertFalse(KnightW.check_move((1, 8), gamestate))

    def test_King(self):
        KingW = King(True, 4, 4)
        RookW = Rook(True, 3, 4)
        RookB = Rook(False, 5, 5)
        gamestate = {1: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None},
                    2: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None},
                    3: {1: None, 2: None, 3: None, 4: RookW, 5: None, 6: None, 7: None, 8: None},
                    4: {1: None, 2: None, 3: None, 4: KingW, 5: None, 6: None, 7: None, 8: None}, 
                    5: {1: None, 2: None, 3: None, 4: None, 5: RookB, 6: None, 7: None, 8: None}, 
                    6: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None}, 
                    7: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None}, 
                    8: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None}}
        
        self.assertTrue(KingW.check_move((5, 5), gamestate))
        self.assertTrue(KingW.check_move((5, 4), gamestate))

        self.assertFalse(KingW.check_move((3, 4), gamestate))
        self.assertFalse(KingW.check_move((4, 1), gamestate))
    
    def test_check_check_1(self):
        KingW = King(True, 2, 2)
        KingB = King(False, 5, 3)
        PawnW = Pawn(True, 6, 4)
        PawnB = Pawn(False, 3, 3)
        gamestate = {1: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None},
                    2: {1: None, 2: KingW, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None},
                    3: {1: None, 2: None, 3: PawnB, 4: None, 5: None, 6: None, 7: None, 8: None},
                    4: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None}, 
                    5: {1: None, 2: None, 3: KingB, 4: None, 5: None, 6: None, 7: None, 8: None}, 
                    6: {1: None, 2: None, 3: None, 4: PawnW, 5: None, 6: None, 7: None, 8: None}, 
                    7: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None}, 
                    8: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None}}
        
        self.assertTrue(KingW.check_check(gamestate))
        self.assertFalse(KingB.check_check(gamestate))

    def test_check_check_2(self):
        KingW = King(True, 4, 4)
        KingB = King(False, 7, 3)
        KnightW = Knight(True, 4, 2)
        KnightB = Knight(False, 6, 5)
        gamestate = {1: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None},
                    2: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None},
                    3: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None},
                    4: {1: None, 2: KnightW, 3: None, 4: KingW, 5: None, 6: None, 7: None, 8: None}, 
                    5: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None}, 
                    6: {1: None, 2: None, 3: None, 4: None, 5: KnightB, 6: None, 7: None, 8: None}, 
                    7: {1: None, 2: None, 3: KingB, 4: None, 5: None, 6: None, 7: None, 8: None}, 
                    8: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None}}
        
        self.assertTrue(KingW.check_check(gamestate))
        self.assertFalse(KingB.check_check(gamestate))

    def test_check_check_3(self):
        King1 = King(True, 4, 4)
        King2 = King(False, 5, 5)
        King3 = King(True, 7, 5)
        gamestate = {1: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None},
                    2: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None},
                    3: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None},
                    4: {1: None, 2: None, 3: None, 4: King1, 5: None, 6: None, 7: None, 8: None}, 
                    5: {1: None, 2: None, 3: None, 4: None, 5: King2, 6: None, 7: None, 8: None}, 
                    6: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None}, 
                    7: {1: None, 2: None, 3: None, 4: None, 5: King3, 6: None, 7: None, 8: None}, 
                    8: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None}}
        
        self.assertTrue(King1.check_check(gamestate))
        self.assertFalse(King3.check_check(gamestate))

    def test_check_check_4(self):
        KingW = King(True, 2, 2)
        QueenW = Queen(True, 6, 2)
        KingB = King(False, 6, 6)
        QueenB = Queen(False, 2, 6)
        KnightB = Knight(False, 6, 5)
        gamestate = {1: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None},
                    2: {1: None, 2: KingW, 3: None, 4: None, 5: None, 6: QueenB, 7: None, 8: None},
                    3: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None},
                    4: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None}, 
                    5: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None}, 
                    6: {1: None, 2: QueenW, 3: None, 4: None, 5: KnightB, 6: KingB, 7: None, 8: None}, 
                    7: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None}, 
                    8: {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None}}
        
        self.assertTrue(KingW.check_check(gamestate))
        self.assertFalse(KingB.check_check(gamestate))
        