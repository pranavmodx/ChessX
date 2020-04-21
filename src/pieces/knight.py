from pieces import Piece
from config import BD_X, BD_Y, BD_SZ, SQ_SZ


class Knight(Piece):
    value = 3

    def __init__(self, p_no=None, colour='White'):
        super().__init__(p_no, colour)

    def valid_moves(self):
        x = self.pos[0]
        y = self.pos[1]

        valids = []

        # 1 square
        inc_x1 = x + SQ_SZ
        dec_x1 = x - SQ_SZ
        inc_y1 = y + SQ_SZ
        dec_y1 = y - SQ_SZ

        # 2 squares
        inc_x2 = x + 2 * SQ_SZ
        dec_x2 = x - 2 * SQ_SZ
        inc_y2 = y + 2 * SQ_SZ
        dec_y2 = y - 2 * SQ_SZ

        # Right 1 sq
        if inc_x1 < BD_SZ:
            # Down 2 sq
            if inc_y2 < BD_SZ:
                valids.append((inc_x1, inc_y2))
            # Up 2 sq
            if dec_y2 >= BD_Y:
                valids.append((inc_x1, dec_y2))

        # Left 1 sq
        if dec_x1 >= BD_X:
            # Down 2 sq
            if inc_y2 < BD_SZ:
                valids.append((dec_x1, inc_y2))
            # Up 2 sq
            if dec_y2 >= BD_Y:
                valids.append((dec_x1, dec_y2))

        # Right 2 sq
        if inc_x2 < BD_SZ:
            # Down 1 sq
            if inc_y1 < BD_SZ:
                valids.append((inc_x2, inc_y1))
            # Up 1 sq
            if dec_y1 >= BD_Y:
                valids.append((inc_x2, dec_y1))

        # Left 2 sq
        if dec_x2 >= BD_X:
            # Down 1 sq
            if inc_y1 < BD_SZ:
                valids.append((dec_x2, inc_y1))
            # Up 1 sq
            if dec_y1 >= BD_Y:
                valids.append((dec_x2, dec_y1))

        return valids

    def move_checks_king(self, board):
        if board.king_pos[board.get_next_turn()] in self.valid_moves() or \
                board.is_controlled_sq(board.king_pos[board.get_next_turn()], board.turn):
            return True

    def handle_move(self, board, sq1_pos, sq2_pos):
        piece2 = board.fetch_piece(sq2_pos)

        if piece2:
            if board.turn != piece2.colour:
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
        if self.move_checks_king(board):
            board.under_check = True
        else:
            board.under_check = False

        return 1
