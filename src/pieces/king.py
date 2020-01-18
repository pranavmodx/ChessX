from .piece import Piece


class King(Piece):
    value = None

    def __init__(self, p_no=None, colour='White', p_type='King', captured=False):
        super().__init__(p_type, p_no, colour, captured)

    def valid_moves():
        pass