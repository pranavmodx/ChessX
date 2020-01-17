from .piece import Piece


class Queen(Piece):
    value = 9

    def __repr__(self):
        return f'Queen({self.colour})'

    def __str__(self):
        return f'Queen({self.colour})'

    def valid_moves():
        pass
