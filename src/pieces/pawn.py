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

    def move_checks_king(self, board, sq2_pos):
        opp_king_pos = board.king_pos[board.get_next_turn()]

        if opp_king_pos in self.valid_moves(board.is_flipped) or \
        board.is_controlled_sq(opp_king_pos, board.turn):
            return True
        return False

    def handle_move(self, board, sq1_pos, sq2_pos):
        self.handle_promotion(sq2_pos)

        piece2 = board.fetch_piece(sq2_pos)
        own_king_pos = board.king_pos[board.turn]
        dist_x, dist_y = board.calc_sq_dist(sq1_pos, sq2_pos)

        if piece2:
            # If there's a piece directly in front of self
            # 1 or 2 squares (2 if at start pos)
            if (abs(dist_y) != board.SQ_SZ and
                    abs(dist_y) != 2 * board.SQ_SZ) \
                    or abs(dist_x) == board.SQ_SZ:
                if board.turn != piece2.colour:
                    piece2.captured = True
                    self.move(sq2_pos)

                    if board.is_controlled_sq(own_king_pos, board.get_next_turn()):
                        piece2.captured = False
                        self.move(sq1_pos)
                        return 0

                    if self.start_pos == True:
                        self.start_pos = False
                else:
                    return 0
            else:
                return 0

        else:
            if dist_x == 0:
                self.move(sq2_pos)

                if board.is_controlled_sq(own_king_pos, board.get_next_turn()):
                    self.move(sq1_pos)
                    return 0

                if self.start_pos:
                    self.start_pos = False
            else:
                return 0

        if self.move_checks_king(board, sq2_pos):
            board.under_check = True
        else:
            board.under_check = False

        return 1

    def handle_promotion(self, pos):
        pass
        # self.captured = True
        # provide choice to promote to
        # make dialog box to pop up and close accordingly

        # if choice Queen
        # make new queen at this pos
        # else other chosen piece
        # and so on...

        # also see if it causes check to king

        # handle case for promotion after capturing and occupying last rank

    def en_passant_move(self, pos):
        pass

        # if opp. pawn is at 4th or 5th rank (black or white resp) 
        # and i make a double pawn push, enable en_passant
        

