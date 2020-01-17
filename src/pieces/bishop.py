from .piece import Piece


class Bishop(Piece):
    value = 3

    def __init__(self, b_no, colour='White', captured=False):
        super().__init__(colour, captured)
        self.b_no = b_no

    def __repr__(self):
        return f'Bishop{self.b_no}({self.colour})'

    def __str__(self):
        return f'Bishop{self.b_no}({self.colour})'

    def valid_moves():
        pass