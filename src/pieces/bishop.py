from pieces import Piece
from config import BD_X, BD_Y


class Bishop(Piece):
    value = 3

    def __init__(self, p_type='Bishop', p_no=None, colour='White'):
        super().__init__(p_type, p_no, colour)

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

        return valids