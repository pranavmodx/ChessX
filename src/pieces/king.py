from .piece import Piece
from board import BD_SZ, SQ_SZ

class King(Piece):
    value = None

    def __init__(self, p_no=None, colour='White', p_type='King', captured=False):
        super().__init__(p_type, p_no, colour, captured)
        self.start_pos = True # For checking castling ability

    def valid_moves(self):
        x = self.pos[0]
        y = self.pos[1]
        valids = [
            ((x + SQ_SZ) % BD_SZ, y),
            ((x - SQ_SZ) % BD_SZ, y),
            (x, (y + SQ_SZ) % BD_SZ),
            (x, (y - SQ_SZ) % BD_SZ),
            ((x + SQ_SZ) % BD_SZ, (y + SQ_SZ) % BD_SZ),
            ((x - SQ_SZ) % BD_SZ, (y + SQ_SZ) % BD_SZ),
            ((x + SQ_SZ) % BD_SZ, (y - SQ_SZ) % BD_SZ),
            ((x - SQ_SZ) % BD_SZ, (y - SQ_SZ) % BD_SZ),
        ]

        if self.start_pos:
            valids.append((x + 2 * SQ_SZ, y))
            valids.append((x - 2 * SQ_SZ, y))

        return valids