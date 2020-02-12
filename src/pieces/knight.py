from .piece import Piece


class Knight(Piece):
    value = 3

    def __init__(self, p_no=None, colour='White', p_type='Knight'):
        super().__init__(p_type, p_no, colour)

    def valid_moves(self):
        x = self.pos[0]
        y = self.pos[1]
        sq_size = self.size()
        bd_size = sq_size * 8
        valids = []

        inc_x1 = x + sq_size
        dec_x1 = x - sq_size
        inc_y1 = y + sq_size
        dec_y1 = y - sq_size

        inc_x2 = x + 2 * sq_size
        dec_x2 = x - 2 * sq_size
        inc_y2 = y + 2 * sq_size
        dec_y2 = y - 2 * sq_size

        if inc_x1 < BD_SZ and inc_y2 < BD_SZ:  
            valids.append((inc_x1, inc_y2))

        if dec_x1 >= bd_x and inc_y2 < BD_SZ:  
            valids.append((dec_x1, inc_y2))

        if inc_x1 < BD_SZ and dec_y2 >= bd_y:  
            valids.append((inc_x1, dec_y2))

        if dec_x1 >= bd_x and dec_y2 >= bd_y:  
            valids.append((dec_x1, dec_y2))

        if inc_x2 < BD_SZ and inc_y1 < BD_SZ:  
            valids.append((inc_x2, inc_y1))

        if dec_x2 >= bd_x and inc_y1 < BD_SZ:  
            valids.append((dec_x2, inc_y1))

        if inc_x2 < BD_SZ and dec_y1 >= bd_y:  
            valids.append((inc_x2, dec_y1))

        if dec_x2 >= bd_x and dec_y1 >= bd_y:  
            valids.append((dec_x2, dec_y1))
            
        return valids
