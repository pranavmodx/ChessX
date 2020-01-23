from .piece import Piece
from board import SQ_SZ


class Queen(Piece):
    value = 9

    def __init__(self, p_no=None, colour='White', p_type='Queen', captured=False):
        super().__init__(p_type, p_no, colour, captured)

    def valid_moves(self):
        x = self.pos[0]
        y = self.pos[1]
        valids = []

        for i in range(8):
            # Rook
            valids.append((x + i * SQ_SZ, y))
            valids.append((x - i * SQ_SZ, y))
            valids.append((x, y + i * SQ_SZ))
            valids.append((x, y - i * SQ_SZ))

            # Bishop
            valids.append((x + i * SQ_SZ, y + i * SQ_SZ))
            valids.append((x - i * SQ_SZ, y + i * SQ_SZ))
            valids.append((x + i * SQ_SZ, y - i * SQ_SZ))
            valids.append((x - i * SQ_SZ, y - i * SQ_SZ))

        return valids

