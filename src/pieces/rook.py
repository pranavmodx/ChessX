from .piece import Piece
from board import BD_SZ, SQ_SZ


class Rook(Piece):
    value = 5

    def __init__(self, p_no=None, colour='White', p_type='Rook', captured=False):
        super().__init__(p_type, p_no, colour, captured)
        self.start_pos = True # For checking castling ability

    def valid_moves(self):
        x = self.pos[0]
        y = self.pos[1]
        
        valids = []

        for i in range(1, 8):
            valids.append(((x + i * SQ_SZ) % BD_SZ, y))
            valids.append(((x - i * SQ_SZ) % BD_SZ, y))
            valids.append((x, (y + i * SQ_SZ) % BD_SZ))
            valids.append((x, (y - i * SQ_SZ) % BD_SZ))

        return list(set(valids))
