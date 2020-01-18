from .piece import Piece


class Pawn(Piece): 
    value = 1 

    def __init__(self, p_no=None, colour='White', p_type='Pawn', captured=False):
        super().__init__(p_type, p_no, colour, captured)
        self.start_pos = True # Special case for pawns

    def valid_moves(self):
        pass
