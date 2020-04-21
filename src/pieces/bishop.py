from pieces import Piece
from config import BD_X, BD_Y, BD_SZ, SQ_SZ


class Bishop(Piece):
    value = 3

    def __init__(self, p_no=None, colour='White'):
        super().__init__(p_no, colour)

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
                # Down
                if inc_y < BD_SZ:
                    valids.append((inc_x, inc_y))
                # Up
                if dec_y >= BD_Y:
                    valids.append((inc_x, dec_y))

            # Left
            if dec_x >= BD_X:
                # Down
                if inc_y < BD_SZ:
                    valids.append((dec_x, inc_y))
                # Up
                if dec_y >= BD_Y:
                    valids.append((dec_x, dec_y))

        return valids

    @staticmethod
    def move_through(board, req_pos, dist_x, dist_y):
        temp = None
        for i in range(1, int(abs(dist_x) / board.SQ_SZ)):
            # Left
            if dist_x < 0:
                # Up
                if dist_y < 0:
                    temp = board.fetch_piece(
                        (req_pos[0] - i * board.SQ_SZ, req_pos[1] - i * board.SQ_SZ))
                # Down
                elif dist_y > 0:
                    temp = board.fetch_piece(
                        (req_pos[0] - i * board.SQ_SZ, req_pos[1] + i * board.SQ_SZ))

            # Right
            elif dist_x > 0:
                # Up
                if dist_y < 0:
                    temp = board.fetch_piece(
                        (req_pos[0] + i * board.SQ_SZ, req_pos[1] - i * board.SQ_SZ))
                # Down
                elif dist_y > 0:
                    temp = board.fetch_piece(
                        (req_pos[0] + i * board.SQ_SZ, req_pos[1] + i * board.SQ_SZ))

            if temp:
                return True

        return False

    def move_checks_king(self, board, sq2_pos):
        if board.king_pos[board.get_next_turn()] in self.valid_moves() and \
            not self.move_through(
            board,
            sq2_pos,
            board.king_pos[board.get_next_turn()][0] - sq2_pos[0],
            board.king_pos[board.get_next_turn()][1] - sq2_pos[1]
        ) or \
            board.is_controlled_sq(
            board.king_pos[board.get_next_turn()],
            board.get_next_turn()
        ):
            return True

    def handle_move(self, board, sq1_pos, sq2_pos):
        piece2 = board.fetch_piece(sq2_pos)

        dist_x, dist_y = board.calc_sq_dist(sq1_pos, sq2_pos)

        # If piece is present in b/w the 2 sqs
        if self.move_through(board, sq1_pos, dist_x, dist_y):
            return 0
        else:
            # If occupied square
            if piece2 and piece2.colour != self.colour:
                piece2.captured = True
                self.move(sq2_pos)

                # Undo move if own king comes under attack by the move
                if board.under_check and \
                        board.is_controlled_sq(
                            board.king_pos[self.colour], self.colour
                        ):
                    piece2.captured = False
                    self.move(sq1_pos)
                    return 0

            # If empty square
            else:
                self.move(sq2_pos)

                # Undo move...
                if board.is_controlled_sq(board.king_pos[self.colour], self.colour):
                    self.move(sq1_pos)
                    return 0

            # Check if the move caused a check to king
            if self.move_checks_king(board, sq2_pos):
                # Some issue here -> highlights both kings alternately after this
                board.under_check = True
            else:
                board.under_check = False

            return 1
