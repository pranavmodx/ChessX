from .piece import Piece


class Pawn(Piece): 
    value = 1 

    def __init__(self, p_no, colour='White', captured=False):
        super().__init__(colour, captured)
        self.p_no = p_no
        self.start_pos = True

    def __repr__(self):
        return f'Pawn{self.p_no + 1}({self.colour})'

    def __str__(self):
        return f'Pawn{self.p_no + 1}({self.colour})'

    def valid_moves(self):
        pass
