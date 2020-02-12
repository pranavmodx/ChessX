from .piece import Piece


class Rook(Piece):
    value = 5

    def __init__(self, p_no=None, colour='White', p_type='Rook'):
        super().__init__(p_type, p_no, colour)
        self.start_pos = True # For checking castling ability

    def valid_moves(self):
        x = self.pos[0]
        y = self.pos[1]
        sq_size = self.size()
        bd_size = sq_size * 8
        valids = []

        for i in range(1, 8):
            inc_x = x + i * sq_size
            dec_x = x - i * sq_size
            inc_y = y + i * sq_size
            dec_y = y - i * sq_size

            # Rook
            if inc_x < bd_size:
                valids.append((inc_x, y))

            if dec_x >= bd_x:
                valids.append((dec_x, y))

            if inc_y < bd_size:
                valids.append((x, inc_y))

            if dec_y >= bd_y:
                valids.append((x, dec_y))

        return valids
