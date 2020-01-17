from .piece import Piece


class Knight(Piece):
    value = 3

    def __init__(self, k_no, colour='White', captured=False):
        super().__init__(colour, captured)
        self.k_no = k_no

    def __repr__(self):
        return f'Knight{self.k_no}({self.colour})'

    def __str__(self):
        return f'Knight{self.k_no}({self.colour})'

    def valid_moves():
        pass
