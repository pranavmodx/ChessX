from .piece import Piece
from config import BD_X, BD_Y


class Rook(Piece):
    value = 5

    def __init__(self, p_type='Rook', p_no=None, colour='White'):
        super().__init__(p_type, p_no, colour)
        self.start_pos = True # For checking castling ability

    def valid_moves(self):
        x = self.pos[0]
        y = self.pos[1]

        SQ_SZ = self.size()
        BD_SZ = SQ_SZ * 8
        valids = []

        for i in range(1, 8):
            inc_x = x + i * SQ_SZ
            dec_x = x - i * SQ_SZ
            inc_y = y + i * SQ_SZ
            dec_y = y - i * SQ_SZ

            # Right
            if inc_x < BD_SZ:
                valids.append((inc_x, y))

            # Left
            if dec_x >= BD_X:
                valids.append((dec_x, y))

            # Down
            if inc_y < BD_SZ:
                valids.append((x, inc_y))

            # Up
            if dec_y >= BD_Y:
                valids.append((x, dec_y))

        return valids
