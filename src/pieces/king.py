from .piece import Piece
from board import BD_SZ, SQ_SZ, bd_x, bd_y

class King(Piece):
    value = None

    def __init__(self, p_no=None, colour='White', p_type='King', captured=False):
        super().__init__(p_type, p_no, colour, captured)
        self.start_pos = True # For checking castling ability

    def valid_moves(self):
        x = self.pos[0]
        y = self.pos[1]
        valids = []

        inc_x = x + SQ_SZ
        dec_x = x - SQ_SZ
        inc_y = y + SQ_SZ
        dec_y = y - SQ_SZ

        if inc_x < BD_SZ:
            valids.append((inc_x, y))

        if dec_x >= bd_x:
            valids.append((dec_x, y))

        if inc_y < BD_SZ:
            valids.append((x, inc_y))

        if dec_y >= bd_y:
            valids.append((x, dec_y))

        if inc_x < BD_SZ and inc_y < BD_SZ:
            valids.append((inc_x, inc_y))

        if dec_x >= bd_x and inc_y < BD_SZ:
            valids.append((dec_x, inc_y))

        if inc_x < BD_SZ and dec_y >= bd_y:
            valids.append((inc_x, dec_y))
            
        if dec_x >= bd_x and dec_y >= bd_y:
            valids.append((dec_x, dec_y))      

        if self.start_pos:
            valids.append((x + 2 * SQ_SZ, y))
            valids.append((x - 2 * SQ_SZ, y))

        return valids