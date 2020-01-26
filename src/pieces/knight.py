from .piece import Piece
from board import BD_SZ, SQ_SZ

class Knight(Piece):
    value = 3

    def __init__(self, p_no=None, colour='White', p_type='Knight', captured=False):
        super().__init__(p_type, p_no, colour, captured)

    def valid_moves(self):
        x = self.pos[0]
        y = self.pos[1]
        valids = [
            ((x + SQ_SZ) % BD_SZ, (y + 2 * SQ_SZ) % BD_SZ),
            ((x - SQ_SZ) % BD_SZ, (y + 2 * SQ_SZ) % BD_SZ),
            ((x + SQ_SZ) % BD_SZ, (y - 2 * SQ_SZ) % BD_SZ),
            ((x - SQ_SZ) % BD_SZ, (y - 2 * SQ_SZ) % BD_SZ),
            ((x + 2 * SQ_SZ) % BD_SZ, (y + SQ_SZ) % BD_SZ),
            ((x - 2 * SQ_SZ) % BD_SZ, (y + SQ_SZ) % BD_SZ),
            ((x + 2 * SQ_SZ) % BD_SZ, (y - SQ_SZ) % BD_SZ),
            ((x - 2 * SQ_SZ) % BD_SZ, (y - SQ_SZ) % BD_SZ),
        ]

        return valids
