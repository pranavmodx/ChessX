from .piece import Piece
from board import SQ_SZ

class Knight(Piece):
    value = 3

    def __init__(self, p_no=None, colour='White', p_type='Knight', captured=False):
        super().__init__(p_type, p_no, colour, captured)

    def valid_moves(self):
        x = self.pos[0]
        y = self.pos[1]
        valids = [
            (x + SQ_SZ, y + 2 * SQ_SZ),
            (x - SQ_SZ, y + 2 * SQ_SZ),
            (x + SQ_SZ, y - 2 * SQ_SZ),
            (x - SQ_SZ, y - 2 * SQ_SZ),
            (x + 2 * SQ_SZ, y + SQ_SZ),
            (x - 2 * SQ_SZ, y + SQ_SZ),
            (x + 2 * SQ_SZ, y - SQ_SZ),
            (x - 2 * SQ_SZ, y - SQ_SZ),
        ]

        return valids
