from pieces import Piece
from config import BD_X, BD_Y, BD_SZ, SQ_SZ


class Pawn(Piece):
    value = 1

    def __init__(self, p_no=None, colour='White', is_captured=False, start_pos=True):
        super().__init__(p_no, colour, is_captured)
        self.start_pos = start_pos  # Special case for pawn - double push

    def valid_moves(self, is_flipped=False):
        x = self.pos[0]
        y = self.pos[1]

        valids = []
        start_pos = self.start_pos

        def gen_valids1():
            if y + SQ_SZ < BD_SZ:
                # Diagonal moves
                if x - SQ_SZ >= BD_X:
                    valids.append((x - SQ_SZ, y + SQ_SZ))
                valids.append((x + SQ_SZ, y + SQ_SZ))
                # Straight 1 sq
                valids.append((x, y + SQ_SZ))

            if start_pos:
                # Straight 2 sq
                valids.append((x, y + 2 * SQ_SZ))

            return valids

        def gen_valids2():
            if y - SQ_SZ >= BD_Y:
                # Diagonal moves
                if x - SQ_SZ >= BD_X:
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

    def refine_valid_moves(self, board, old_valid_moves):
        new_valid_moves = []
        
        for move in old_valid_moves:
            # print(board.get_sq_notation(move))
            temp = board.fetch_piece(move)
            if temp:
                if temp.colour != board.get_next_turn():
                    new_valid_moves.append(move)
            else:
                if self.colour == 'Black':
                    if not board.is_flipped:
                        if move == (self.pos[0] + SQ_SZ, self.pos[1]) or \
                        move == (self.pos[0] + 2 * SQ_SZ, self.pos[1]):
                            new_valid_moves.append(move)
                        else:
                            if move == (self.pos[0] - SQ_SZ, self.pos[1]) or \
                            move == (self.pos[0] - 2 * SQ_SZ, self.pos[1]):
                                new_valid_moves.append(move)
                else:
                    if not board.is_flipped:
                        if move == (self.pos[0] - SQ_SZ, self.pos[1]) or \
                        move == (self.pos[0] - 2 * SQ_SZ, self.pos[1]):
                            new_valid_moves.append(move)
                    else:
                        if move == (self.pos[0] + SQ_SZ, self.pos[1]) or \
                        move == (self.pos[0] + 2 * SQ_SZ, self.pos[1]):
                            new_valid_moves.append(move)

        return new_valid_moves

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
                    piece2.is_captured = True
                    self.move(sq2_pos)

                    if board.is_controlled_sq(own_king_pos, board.get_next_turn()):
                        piece2.is_captured = False
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
        # self.is_captured = True
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
        

