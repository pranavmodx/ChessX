from .piece import Piece


class Queen(Piece):
    value = 9

    def __init__(self, p_no=None, colour='White', p_type='Queen', captured=False):
        super().__init__(p_type, p_no, colour, captured)

    def valid_moves():
        pass
