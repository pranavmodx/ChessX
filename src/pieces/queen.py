from pieces import Bishop, Rook
from config import BD_X, BD_Y


class Queen(Bishop, Rook):
    value = Bishop.value + Rook.value + 1

    def __init__(self, p_type='Queen', p_no=1, colour='White'):
        super().__init__(p_type, p_no, colour)

    def valid_moves(self):
        valids = []
        valids = Bishop.valid_moves(self)
        valids.extend(Rook.valid_moves(self))

        return valids

