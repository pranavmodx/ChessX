from .piece import Piece


class King(Piece):
    value = None

    def __init__(self, p_no=None, colour='White', p_type='King'):
        super().__init__(p_type, p_no, colour)
        self.start_pos = True # For checking castling ability

    def valid_moves(self):
        x = self.pos[0]
        y = self.pos[1]
        sq_size = self.size()
        bd_size = sq_size * 8
        valids = []

        inc_x = x + sq_size
        dec_x = x - sq_size
        inc_y = y + sq_size
        dec_y = y - sq_size

        if inc_x < bd_size:
            valids.append((inc_x, y))

        if dec_x >= bd_x:
            valids.append((dec_x, y))

        if inc_y < bd_size:
            valids.append((x, inc_y))

        if dec_y >= bd_y:
            valids.append((x, dec_y))

        if inc_x < bd_size and inc_y < bd_size:
            valids.append((inc_x, inc_y))

        if dec_x >= bd_x and inc_y < bd_size:
            valids.append((dec_x, inc_y))

        if inc_x < bd_size and dec_y >= bd_y:
            valids.append((inc_x, dec_y))
            
        if dec_x >= bd_x and dec_y >= bd_y:
            valids.append((dec_x, dec_y))      

        if self.start_pos:
            valids.append((x + 2 * sq_size, y))
            valids.append((x - 2 * sq_size, y))

        return valids