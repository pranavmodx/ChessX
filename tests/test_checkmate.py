import unittest
from config import BD_X, BD_Y
from board import Board

class TestCheckmate(unittest.TestCase):
    def setUp(self):
        self.board = Board((BD_X, BD_Y))
        self.board.init_all_pieces()
        self.board.set_pos_all()

        self.w_pawns = self.board.pieces['w_pawns']
        self.w_pieces = self.board.pieces['w_pieces']
        self.b_pawns = self.board.pieces['b_pawns']
        self.b_pieces = self.board.pieces['b_pieces']

        self.w_rook1 = self.w_pieces[0]
        self.w_knight1 = self.w_pieces[1]
        self.w_bishop1 = self.w_pieces[2]
        self.w_queen = self.w_pieces[3]
        self.w_king = self.w_pieces[4]
        self.w_bishop2 = self.w_pieces[5]
        self.w_knight2 = self.w_pieces[6]
        self.w_rook2 = self.w_pieces[7]

        self.b_rook1 = self.b_pieces[0]
        self.b_knight1 = self.b_pieces[1]
        self.b_bishop1 = self.b_pieces[2]
        self.b_queen = self.b_pieces[3]
        self.b_king = self.b_pieces[4]
        self.b_bishop2 = self.b_pieces[5]
        self.b_knight2 = self.b_pieces[6]
        self.b_rook2 = self.b_pieces[7]

    def test_checkmate(self):
        get_sq_coord = self.board.get_sq_coord

        # Fool's Mate Position
        self.w_pawns[4].move(get_sq_coord('e4'))
        self.b_pawns[4].move(get_sq_coord('e5'))
        self.w_bishop2.move(get_sq_coord('c4'))
        self.b_bishop2.move(get_sq_coord('c5'))
        self.w_queen.move(get_sq_coord('f3'))
        self.b_pawns[3].move(get_sq_coord('d6'))

        # self.w_knight2.move(get_sq_coord('h3'))
        # self.b_knight2.move(get_sq_coord('h6'))

        self.b_pawns[5].is_captured = True
        self.board.pos_of_piece_causing_check = get_sq_coord('f7')
        self.w_queen.move(get_sq_coord('f7'))
        self.board.under_check = True

        self.assertEqual(self.board.is_checkmate(), True)


if __name__ == '__main__':
    unittest.main()