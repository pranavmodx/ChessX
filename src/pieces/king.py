from .piece import Piece


class King(Piece):
    value = 0

    def __repr__(self):
        return f'King({self.colour})'

    def __str__(self):
        return f'King({self.colour})'

    def valid_moves():
        pass