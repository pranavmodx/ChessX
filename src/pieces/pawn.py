from pieces import Piece
from config import BD_X, BD_Y, BD_SZ, SQ_SZ


class Pawn(Piece):
    value = 1

    def __init__(self, p_no=None, colour='White'):
        super().__init__(p_no, colour)
        self.start_pos = True  # Special case for pawn - double push

    def valid_moves(self, is_flipped=False):
        x = self.pos[0]
        y = self.pos[1]

        valids = []
        start_pos = self.start_pos

        def gen_valids1():
            # Diagonal moves
            valids.append((x - SQ_SZ, y + SQ_SZ))
            valids.append((x + SQ_SZ, y + SQ_SZ))
            # Straight 1 sq
            valids.append((x, y + SQ_SZ))

            if start_pos:
                # Straight 2 sq
                valids.append((x, y + 2 * SQ_SZ))

            return valids

        def gen_valids2():
            # Diagonal moves
            valids.append((x - SQ_SZ, y - SQ_SZ))
            valids.append((x + SQ_SZ, y - SQ_SZ))
            # Straight 1 sq
            valids.append((x, y - SQ_SZ))

            if start_pos:
                # Straight 2 sq
                valids.append((x, y - 2 * SQ_SZ))

            return valids

        if not is_flipped:
            if self.colour == 'Black':
                moves = gen_valids1
            else:
                moves = gen_valids2

        else:
            if self.colour == 'White':
                moves = gen_valids1
            else:
                moves = gen_valids2

        return moves()

    def handle_move(self, board, sq1_pos, sq2_pos):
        piece2 = board.fetch_piece(sq2_pos)

        dist_x, dist_y = board.calc_sq_dist(sq1_pos, sq2_pos)

        if piece2:
            # If there's a piece directly in front of self
            # 1 or 2 squares (2 if at start pos)
            if (abs(dist_y) != board.SQ_SZ and
                    abs(dist_y) != 2 * board.SQ_SZ) \
                    or abs(dist_x) == board.SQ_SZ:
                if self.colour != piece2.colour:
                    piece2.captured = True
                    self.move(sq2_pos)

                    if board.is_controlled_sq(board.king_pos[board.turn], board.get_next_turn()):
                        piece2.captured = False
                        self.move(sq1_pos)
                        return 0

                    if self.start_pos == True:
                        self.start_pos = False

                    return 1
            return 0

        else:
            if dist_x == 0:
                self.move(sq2_pos)

                if board.is_controlled_sq(board.king_pos[board.turn], board.get_next_turn()):
                    self.move(sq1_pos)
                    return 0

                if self.start_pos:
                    self.start_pos = False

                return 1
            return 0

        if board.king_pos[board.turn] in self.valid_moves(board.is_flipped) or \
                board.is_controlled_sq(board.king_pos[board.turn], board.get_next_turn()):
            board.under_check = True
        else:
            board.under_check = False

    def handle_promotion(self):
        pass
