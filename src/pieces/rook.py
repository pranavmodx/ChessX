from .piece import Piece


class Rook(Piece):
    value = 5

    def __init__(self, p_no=None, colour='White', p_type='Rook', captured=False):
        super().__init__(p_type, p_no, colour, captured)

    def valid_moves():
        pass