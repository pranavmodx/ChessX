from .piece import Piece


class Bishop(Piece):
    value = 3

    def __init__(self, p_no=None, colour='White', p_type='Bishop', captured=False):
        super().__init__(p_type, p_no, colour, captured)

    def valid_moves():
        pass