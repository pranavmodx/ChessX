from .piece import Piece


class Bishop(Piece):
    value = 3

    def __init__(self, p_no=None, colour='White', p_type='Bishop'):
        super().__init__(p_type, p_no, colour)

    def valid_moves(self):
        BD_X = self.pos[0]
        BD_Y = self.pos[1]
        SQ_SZ = self.size() # Square size = Piece size
        BD_SZ = SQ_SZ * 8
        valids = []

        for i in range(1, 8):
            inc_x = x + i * SQ_SZ
            dec_x = x - i * SQ_SZ
            inc_y = y + i * SQ_SZ
            dec_y = y - i * SQ_SZ

            if inc_x < BD_SZ and inc_y < BD_SZ:
                valids.append((inc_x, inc_y))

            if dec_x >= bd_x and inc_y < BD_SZ:
                valids.append((dec_x, inc_y))

            if inc_x < BD_SZ and dec_y >= BD_Y:
                valids.append((inc_x, dec_y))

            if inc_x >= bd_x and dec_y >= BD_Y:
                valids.append((dec_x, dec_y))

        return valids