class Move:
    def __init__(self):
        self.turn = 'White'
        self.valid_moves = []
        self.under_check = False

    @staticmethod
    def next_turn(turn):
        if turn == 'White':
            return 'Black'
        return 'White'

    def handle_pawn(self, board, piece1, sq1_pos, sq2_pos):
        pawn = piece1
        piece2 = board.fetch_piece(sq2_pos)

        dist_x, dist_y = board.calc_sq_dist(sq1_pos, sq2_pos)

        if not piece2:
            if dist_x == 0 and sq2_pos in self.valid_moves:
                pawn.move(sq2_pos)

                if board.is_controlled_sq(board.king_pos[self.turn], self.turn):
                    pawn.move(sq1_pos)
                    return

                if pawn.start_pos:
                    pawn.start_pos = False

                self.turn = self.next_turn(self.turn)

                if board.king_pos[self.turn] in pawn.valid_moves(board.is_flipped):
                    self.under_check = True

        else:
            if sq2_pos in self.valid_moves:
                # If there's a piece directly in front of pawn
                # 1 or 2 squares (2 if at start pos)
                if (abs(dist_y) != board.SQ_SZ and \
                    abs(dist_y) != 2 * board.SQ_SZ) \
                    or abs(dist_x) == board.SQ_SZ:
                    if pawn.colour != piece2.colour:
                        piece2.captured = True
                        pawn.move(sq2_pos)

                        if self.under_check:
                            if board.is_controlled_sq(board.king_pos[self.turn], self.turn):
                                piece2.captured = False
                                pawn.move(sq1_pos)
                                return

                        if pawn.start_pos == True:
                            pawn.start_pos = False

                        self.turn = self.next_turn(self.turn)

                        if board.king_pos[self.turn] in pawn.valid_moves(board.is_flipped) or \
                            board.is_controlled_sq(board.king_pos[self.turn], self.turn):
                            self.under_check = True

    def handle_king(self, board, piece1, sq1_pos, sq2_pos):
        king = piece1
        piece2 = board.fetch_piece(sq2_pos)

        dist_x, dist_y = board.calc_sq_dist(sq1_pos, sq2_pos)

        if not piece2:
            if sq2_pos in self.valid_moves and not board.is_controlled_sq(sq2_pos, self.turn):
                if not self.under_check:
                    castling_allowed = True
                # Checking for castling
                if abs(dist_x) == 2 * board.SQ_SZ:
                    # Checking if piece present in b/w
                    if dist_x < 0:
                        k = board.fetch_piece((king.pos[0] - board.SQ_SZ, king.pos[1]))
                        if k:
                            castling_allowed = False
                    else:
                        k = board.fetch_piece((king.pos[0] + board.SQ_SZ, king.pos[1]))
                        if k:
                            castling_allowed = False

                    if castling_allowed:
                        if self.turn == 'White':
                            rook1 = board.pieces['w_pieces'][0]
                            rook2 = board.pieces['w_pieces'][-1]
                        else:
                            rook1 = board.pieces['b_pieces'][0]
                            rook2 = board.pieces['b_pieces'][-1]

                        # Short castling
                        if sq1_pos[0] < sq2_pos[0] and rook2.start_pos:
                            king.move(sq2_pos)
                            board.king_pos[self.turn] = sq2_pos
                            king.start_pos = False
                            rook2.move((rook2.pos[0] - 2 * board.SQ_SZ, rook2.pos[1]))
                            rook2.start_pos = False
                            rook1.start_pos = False

                        # Long castling
                        elif sq1_pos[0] > sq2_pos[0] and rook1.start_pos:
                            king.move(sq2_pos)
                            board.king_pos[self.turn] = sq2_pos
                            king.start_pos = False
                            rook1.move((rook1.pos[0] + 3 * board.SQ_SZ, rook1.pos[1]))
                            rook1.start_pos = False
                            rook2.start_pos = False

                        self.turn = self.next_turn(self.turn)

                else:
                    king.move(sq2_pos)
                    board.king_pos[self.turn] = sq2_pos
                    king.start_pos = False
                    self.turn = self.next_turn(self.turn)
        
        else:
            if not board.is_controlled_sq(sq2_pos, self.turn):
                if king.colour != piece2.colour:
                    piece2.captured = True
                    king.move(sq2_pos)
                    board.king_pos[self.turn] = sq2_pos

        # Discovered attack by king
        if board.is_controlled_sq(board.king_pos[self.turn], self.turn):
            self.under_check = True

    def handle_brq(self, board, piece1, sq1_pos, sq2_pos):
        # Handles moves of bishop, rook and queen

        piece2 = board.fetch_piece(sq2_pos)

        dist_x, dist_y = board.calc_sq_dist(sq1_pos, sq2_pos)

        if not piece2:
            if sq2_pos in self.valid_moves:
                if not piece1.move_through(board, sq1_pos, dist_x, dist_y):
                    piece1.move(sq2_pos)

                    if board.is_controlled_sq(board.king_pos[self.turn], self.turn):
                        piece1.move(sq1_pos)
                        return

                    self.turn = self.next_turn(self.turn)

        else:
            if sq2_pos in self.valid_moves:
                if piece1.colour != piece2.colour and \
                    not piece1.move_through(board, sq1_pos, dist_x, dist_y):
                    piece2.captured = True
                    piece1.move(sq2_pos)

                    if self.under_check:
                        if board.is_controlled_sq(board.king_pos[self.turn], self.turn):
                            piece2.captured = False
                            piece1.move(sq1_pos)
                            return

                    self.turn = self.next_turn(self.turn)

        # Check if the piece1 move caused a check to king
        if board.king_pos[self.turn] in piece1.valid_moves() and \
            not piece1.move_through(
                board, 
                sq2_pos, 
                board.king_pos[self.turn][0] - sq2_pos[0], 
                board.king_pos[self.turn][1] - sq2_pos[1]
            ) or \
            board.is_controlled_sq(board.king_pos[self.turn], self.turn):
            self.under_check = True

    def handle_knight(self, board, piece1, sq1_pos, sq2_pos):
        knight = piece1
        piece2 = board.fetch_piece(sq2_pos)

        if not piece2:
            if sq2_pos in self.valid_moves:
                knight.move(sq2_pos)

                if board.is_controlled_sq(board.king_pos[self.turn], self.turn):
                    knight.move(sq1_pos)
                    return

                self.turn = self.next_turn(self.turn)

                if board.king_pos[self.turn] in knight.valid_moves():
                    self.under_check = True

        else:
            if sq2_pos in self.valid_moves:
                if knight.colour != piece2.colour:
                    piece2.captured = True
                    knight.move(sq2_pos)

                    if board.is_controlled_sq(board.king_pos[self.turn], self.turn):
                        piece2.captured = False
                        knight.move(sq1_pos)
                        return

                    self.turn = self.next_turn(self.turn)

                    # Check if the knight move caused a check to king
                    if board.king_pos[self.turn] in knight.valid_moves() or \
                        board.is_controlled_sq(board.king_pos[self.turn], self.turn):
                        self.under_check = True

    def handle_piece(self, board, piece1, sq1_pos, sq2_pos):
        if piece1.p_type == 'Pawn':
            self.handle_pawn(board, piece1, sq1_pos, sq2_pos)

        elif piece1.p_type == 'Knight':
            self.handle_knight(board, piece1, sq1_pos, sq2_pos)

        elif piece1.p_type == 'King':
            self.handle_king(board, piece1, sq1_pos, sq2_pos)

        else:
            self.handle_brq(board, piece1, sq1_pos, sq2_pos)