from pieces import Piece
from config import BD_X, BD_Y


class King(Piece):
    value = None

    def __init__(self, p_no=None, colour='White', p_type='King'):
        super().__init__(p_type, p_no, colour)
        self.start_pos = True # For checking castling ability

    def valid_moves(self):
        x = self.pos[0]
        y = self.pos[1]

        SQ_SZ = self.size()
        BD_SZ = SQ_SZ * 8

        valids = []

        inc_x = x + SQ_SZ
        dec_x = x - SQ_SZ
        inc_y = y + SQ_SZ
        dec_y = y - SQ_SZ

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

        # Bottomright
        if inc_x < BD_SZ and inc_y < BD_SZ:
            valids.append((inc_x, inc_y))

        # Bottomleft
        if dec_x >= BD_X and inc_y < BD_SZ:
            valids.append((dec_x, inc_y))

        # Topright
        if inc_x < BD_SZ and dec_y >= BD_Y:
            valids.append((inc_x, dec_y))
            
        # Topleft
        if dec_x >= BD_X and dec_y >= BD_Y:
            valids.append((dec_x, dec_y))      

        # Two squares left and right
        if self.start_pos:
            valids.append((x + 2 * SQ_SZ, y))
            valids.append((x - 2 * SQ_SZ, y))

        return valids