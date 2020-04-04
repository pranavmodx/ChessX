from .piece import Piece
from config import BD_X, BD_Y


class Rook(Piece):
    value = 5

    def __init__(self, p_no=None, colour='White'):
        super().__init__(p_no, colour)
        self.start_pos = True # For checking castling ability

    def valid_moves(self):
        x = self.pos[0]
        y = self.pos[1]

        SQ_SZ = self.size()
        BD_SZ = SQ_SZ * 8
        valids = []

        for i in range(1, 8):
            inc_x = x + i * SQ_SZ
            dec_x = x - i * SQ_SZ
            inc_y = y + i * SQ_SZ
            dec_y = y - i * SQ_SZ

            # Right
            if inc_x < BD_SZ:
                valids.append((inc_x, y))

            # Left
            if dec_x >= BD_X:
                valids.append((dec_x, y))

            # Down
            if inc_y < BD_SZ:
                valids.append((x, inc_y))

            # Up
            if dec_y >= BD_Y:
                valids.append((x, dec_y))

        return valids

    @staticmethod
    def move_through(board, sq1_pos, dist_x, dist_y):
        # Top
        if dist_x == 0 and dist_y < 0:
            for i in range(1, int(abs(dist_y) / board.SQ_SZ)):
                temp = board.fetch_piece((sq1_pos[0], sq1_pos[1] - i * board.SQ_SZ))
                if temp:
                    return True

        # Bottom
        elif dist_x == 0 and dist_y > 0:
            for i in range(1, int(abs(dist_y) / board.SQ_SZ)):
                temp = board.fetch_piece((sq1_pos[0], sq1_pos[1] + i * board.SQ_SZ))
                if temp:
                    return True

        # Right
        elif dist_x > 0 and dist_y == 0:
            for i in range(1, int(abs(dist_x) / board.SQ_SZ)):
                temp = board.fetch_piece((sq1_pos[0] + i * board.SQ_SZ, sq1_pos[1]))
                if temp:
                    return True

        # Left
        elif dist_x < 0 and dist_y == 0:
            for i in range(1, int(abs(dist_x) / board.SQ_SZ)):
                temp = board.fetch_piece((sq1_pos[0] - i * board.SQ_SZ, sq1_pos[1]))
                if temp:
                    return True

        return False

    def handle_move(self, board, sq1_pos, sq2_pos, under_check=False):
        piece2 = board.fetch_piece(sq2_pos)

        dist_x, dist_y = board.calc_sq_dist(sq1_pos, sq2_pos)

        if not piece2:
            if sq2_pos in self.valid_moves():
                if not self.move_through(board, sq1_pos, dist_x, dist_y):
                    self.move(sq2_pos)

                    if board.is_controlled_sq(board.king_pos[self.colour], self.colour):
                        self.move(sq1_pos)
                        return

                    return 1

        else:
            if sq2_pos in self.valid_moves():
                if self.colour != piece2.colour and \
                    not self.move_through(board, sq1_pos, dist_x, dist_y):
                    piece2.captured = True
                    self.move(sq2_pos)

                    if under_check:
                        if board.is_controlled_sq(board.king_pos[self.colour], self.colour):
                            piece2.captured = False
                            self.move(sq1_pos)
                            return

                    return 1

        # Check if the move caused a check to king
        if board.king_pos[self.colour] in self.valid_moves() and \
            not self.move_through(
                board,
                sq2_pos,
                board.king_pos[self.colour][0] - sq2_pos[0],
                board.king_pos[self.colour][1] - sq2_pos[1]
            ) or \
            board.is_controlled_sq(board.king_pos[self.colour], self.colour):
            return -1

        return 0
        