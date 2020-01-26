from .piece import Piece
from board import BD_SZ, SQ_SZ, bd_x, bd_y


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
            inc_x = x + i * SQ_SZ
            dec_x = x - i * SQ_SZ
            inc_y = y + i * SQ_SZ
            dec_y = y - i * SQ_SZ

            # Rook
            if inc_x < BD_SZ:
                valids.append((inc_x, y))

            if dec_x >= bd_x:
                valids.append((dec_x, y))

            if inc_y > BD_SZ:
                valids.append((x, inc_y))

            if dec_y >= bd_y:
                valids.append((x, dec_y))

        return valids
