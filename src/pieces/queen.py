from pieces import Bishop, Rook


class Queen(Bishop, Rook):
    value = Bishop.value + Rook.value + 1

    def __init__(self, p_no=1, colour='White'):
        super().__init__(p_no, colour)

    def valid_moves(self):
        valids = []
        valids = Bishop.valid_moves(self)
        valids.extend(Rook.valid_moves(self))

        return valids

    @staticmethod
    def move_through(board, source, dest):
        return (
            Bishop.move_through(board, source, dest)
            or
            Rook.move_through(board, source, dest)
        )

    def handle_move(self, board, sq1_pos, sq2_pos):
        return Bishop.handle_move(self, board, sq1_pos, sq2_pos)
