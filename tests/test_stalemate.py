import unittest
from config import BD_X, BD_Y
from board import Board
from pieces import (
    Pawn,
    Bishop,
    Knight,
    Rook,
    Queen,
    King,
)

class TestStalemate(unittest.TestCase):
    def setUp(self):
        self.board = Board((BD_X, BD_Y))
        self.board.init_all_pieces(is_captured=True)
        self.board.set_pos_all()

    def test_stalemate(self):
        get_sq_coord = self.board.get_sq_coord

        w_pawns = self.board.pieces['w_pawns']
        b_pawns = self.board.pieces['b_pawns']
        w_pieces = self.board.pieces['w_pieces']
        b_pieces = self.board.pieces['b_pieces']

        w_king = w_pieces[4]
        w_king.is_captured = False
        w_bishop2 = w_pieces[5]
        w_bishop2.is_captured = False
        w_knight2 = w_pieces[6]
        w_knight2.is_captured = False
        w_rook2 = w_pieces[7]
        w_rook2.is_captured = False

        b_king = b_pieces[4]
        b_king.is_captured = False

        w_pawns[0].move(get_sq_coord('c4'))
        w_pawns[0].is_captured = False
        w_pawns[1].move(get_sq_coord('e2'))
        w_pawns[1].is_captured = False
        w_pawns[2].move(get_sq_coord('f3'))
        w_pawns[2].is_captured = False
        w_pawns[3].move(get_sq_coord('f4'))
        w_pawns[3].is_captured = False
        w_pawns[4].move(get_sq_coord('h2'))
        w_pawns[4].is_captured = False
        w_pawns[5].move(get_sq_coord('h3'))
        w_pawns[5].is_captured = False

        b_pawns[0].move(get_sq_coord('c5'))
        b_pawns[0].is_captured = False
        b_pawns[1].move(get_sq_coord('e3'))
        b_pawns[1].is_captured = False
        b_pawns[2].move(get_sq_coord('f5'))
        b_pawns[2].is_captured = False
        b_pawns[3].move(get_sq_coord('h5'))
        b_pawns[3].is_captured = False

        w_king.move(get_sq_coord('g2'))
        w_rook2.move(get_sq_coord('h1'))
        w_knight2.move(get_sq_coord('g1'))
        w_bishop2.move(get_sq_coord('f1'))

        b_king.move(get_sq_coord('h4'))

        self.assertEqual(self.board.is_stalemate(), True)
    

if __name__ == '__main__':
    unittest.main()