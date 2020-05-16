from pieces import Piece
from config import BD_X, BD_Y, BD_SZ, SQ_SZ


class King(Piece):
    value = None

    def __init__(self, colour='White'):
        super().__init__(colour=colour)
        self.start_pos = True  # For checking castling ability

    def valid_moves(self):
        x = self.pos[0]
        y = self.pos[1]

        valids = []

        inc_x = x + SQ_SZ
        dec_x = x - SQ_SZ
        inc_y = y + SQ_SZ
        dec_y = y - SQ_SZ

        # Right
        if inc_x < BD_SZ:
            valids.append((inc_x, y))
            # Down
            if inc_y < BD_SZ:
                valids.append((inc_x, inc_y))
            # Up
            if dec_y >= BD_Y:
                valids.append((inc_x, dec_y))

        # Left
        if dec_x >= BD_X:
            valids.append((dec_x, y))
            # Down
            if inc_y < BD_SZ:
                valids.append((dec_x, inc_y))
            # Up
            if dec_y >= BD_Y:
                valids.append((dec_x, dec_y))

        # Down
        if inc_y < BD_SZ:
            valids.append((x, inc_y))

        # Up
        if dec_y >= BD_Y:
            valids.append((x, dec_y))

        if self.start_pos:
            # Two squares left and right
            valids.append((x + 2 * SQ_SZ, y))
            valids.append((x - 2 * SQ_SZ, y))

        return valids

    def castle(self, board, sq1_pos, sq2_pos):
        if board.turn == 'White':
            rook1 = board.pieces['w_pieces'][0]
            rook2 = board.pieces['w_pieces'][-1]
        else:
            rook1 = board.pieces['b_pieces'][0]
            rook2 = board.pieces['b_pieces'][-1]

        # Short castling
        if sq1_pos[0] < sq2_pos[0] and rook2.start_pos:
            self.move(sq2_pos)
            board.king_pos[board.turn] = sq2_pos
            self.start_pos = False
            rook2.move((rook2.pos[0] - 2 * board.SQ_SZ, rook2.pos[1]))
            rook2.start_pos = False
            rook1.start_pos = False

        # Long castling
        elif sq1_pos[0] > sq2_pos[0] and rook1.start_pos:
            self.move(sq2_pos)
            board.king_pos[board.turn] = sq2_pos
            self.start_pos = False
            rook1.move((rook1.pos[0] + 3 * board.SQ_SZ, rook1.pos[1]))
            rook1.start_pos = False
            rook2.start_pos = False

    def move_checks_king(self, board):
        opp_king_pos = board.king_pos[board.get_next_turn()]
        if board.is_controlled_sq(opp_king_pos, board.turn):
            return True
        return False

    def handle_move(self, board, sq1_pos, sq2_pos):
        # Only applies to king
        # Temporarily remove king from path and check whether sq2_pos
        # is controlled by any piece 
        # (else 'is_path_obstructed' in 'is_controlled_sq' returns true 
        # because king comes in the way)
        self.captured = True
        if board.is_controlled_sq(sq2_pos, board.get_next_turn()):
            self.captured = False
            return 0
        self.captured = False

        piece2 = board.fetch_piece(sq2_pos)

        dist_x, dist_y = board.calc_sq_dist(sq1_pos, sq2_pos)

        if piece2:
            if board.turn != piece2.colour:
                piece2.captured = True
                self.move(sq2_pos)
                board.king_pos[board.turn] = sq2_pos
            else:    
                return 0

        else:
            if not board.under_check:
                castling_allowed = True
            # Checking for castling
            if abs(dist_x) == 2 * board.SQ_SZ:
                temp = None
                # Checking if piece present in b/w
                if dist_x < 0:
                    temp = board.fetch_piece(
                        (self.pos[0] - board.SQ_SZ, self.pos[1]))
                    if temp is None:
                        temp = board.fetch_piece(
                          self.pos[0] - 2 * board.SQ_SZ, self.pos[1])  
      
                else:
                    temp = board.fetch_piece(
                        (self.pos[0] + board.SQ_SZ, self.pos[1]))
                    if temp is None:
                        board.fetch_piece(
                        (self.pos[0] + 2 * board.SQ_SZ, self.pos[1]))

                if temp is not None:
                    castling_allowed = False

                if castling_allowed:
                    self.castle(board, sq1_pos, sq2_pos)
                else:
                    return 0

            else:
                self.move(sq2_pos)
                board.king_pos[board.turn] = sq2_pos
                self.start_pos = False

        # Discovered attack by king
        if self.move_checks_king(board):
            board.under_check = True
        else:
            board.under_check = False

        return 1
