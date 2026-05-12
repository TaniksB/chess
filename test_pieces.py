import unittest
from pieces import Piece

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