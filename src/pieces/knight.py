from .piece import Piece
from board import BD_SZ, SQ_SZ, bd_x, bd_y

class Knight(Piece):
    value = 3

    def __init__(self, p_no=None, colour='White', p_type='Knight', captured=False):
        super().__init__(p_type, p_no, colour, captured)

    def valid_moves(self):
        x = self.pos[0]
        y = self.pos[1]
        valids = []

        inc_x1 = x + SQ_SZ
        dec_x1 = x - SQ_SZ
        inc_y1 = y + SQ_SZ
        dec_y1 = y - SQ_SZ

        inc_x2 = x + 2 * SQ_SZ
        dec_x2 = x - 2 * SQ_SZ
        inc_y2 = y + 2 * SQ_SZ
        dec_y2 = y - 2 * SQ_SZ

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
