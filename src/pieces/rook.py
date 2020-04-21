from .piece import Piece
from config import BD_X, BD_Y, BD_SZ, SQ_SZ


class Rook(Piece):
    value = 5

    def __init__(self, p_no=None, colour='White'):
        super().__init__(p_no, colour)
        self.start_pos = True  # For checking castling ability

    def valid_moves(self):
        x = self.pos[0]
        y = self.pos[1]

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
        temp = None
        if dist_x == 0:
            for i in range(1, int(abs(dist_y) / board.SQ_SZ)):
                # Up
                if dist_y < 0:
                    temp = board.fetch_piece(
                        (sq1_pos[0], sq1_pos[1] - i * board.SQ_SZ))
                # Down
                elif dist_y > 0:
                    temp = board.fetch_piece(
                        (sq1_pos[0], sq1_pos[1] + i * board.SQ_SZ))

                if temp:
                    return True

        elif dist_y == 0:
            for i in range(1, int(abs(dist_x) / board.SQ_SZ)):
                # Right
                if dist_x > 0:
                    temp = board.fetch_piece(
                        (sq1_pos[0] + i * board.SQ_SZ, sq1_pos[1]))
                # Left
                elif dist_x < 0:
                    temp = board.fetch_piece(
                        (sq1_pos[0] - i * board.SQ_SZ, sq1_pos[1]))

                if temp:
                    return True

        return False

    def move_checks_king(self, board, sq2_pos):
        if board.king_pos[board.get_next_turn()] in self.valid_moves() or \
            board.is_controlled_sq(
            board.king_pos[board.get_next_turn()],
            board.turn,
        ):
            return True

    def handle_move(self, board, sq1_pos, sq2_pos):
        piece2 = board.fetch_piece(sq2_pos)

        dist_x, dist_y = board.calc_sq_dist(sq1_pos, sq2_pos)

        if self.move_through(board, sq1_pos, dist_x, dist_y):
            return 0

        else:
            if piece2 and self.colour != piece2.colour:
                piece2.captured = True
                self.move(sq2_pos)

                if board.is_controlled_sq(board.king_pos[board.turn], board.get_next_turn()):
                    piece2.captured = False
                    self.move(sq1_pos)
                    return 0

            else:
                self.move(sq2_pos)

                if board.is_controlled_sq(board.king_pos[board.turn], board.get_next_turn()):
                    self.move(sq1_pos)
                    return 0

            # Check if the move caused a check to king
            if self.move_checks_king(board, sq2_pos):
                board.under_check = True
            else:
                board.under_check = False

            return 1
