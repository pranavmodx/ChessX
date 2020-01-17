from .piece import Piece


class Rook(Piece):
    value = 5

    def __init__(self, r_no, colour='White', captured=False):
        super().__init__(colour, captured)
        self.r_no = r_no

    def __repr__(self):
        return f'Rook{self.r_no}({self.colour})'

    def __str__(self):
        return f'Rook{self.r_no}({self.colour})'

    def valid_moves():
        pass