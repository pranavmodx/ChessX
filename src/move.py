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

        dist_x = sq2_pos[0] - sq1_pos[0]
        dist_y = sq2_pos[1] - sq1_pos[1]

        if not piece2:
            if dist_x == 0 and sq2_pos in self.valid_moves:
                pawn.move(sq2_pos)
                # if self.under_check:
                if board.is_controlled_sq(board.king_pos[self.turn], self.turn):
                    pawn.move(sq1_pos)
                    return

                if pawn.start_pos:
                    pawn.start_pos = False

                self.turn = self.next_turn(self.turn)

                if board.king_pos[self.turn] in pawn.valid_moves(board.is_flipped):
                    self.under_check = True
                    print('Yes')

        else:
            if sq2_pos in self.valid_moves:
                # If there's a piece directly in front of pawn
                # 1 or 2 squares (2 if at start pos)
                if (abs(dist_y) != board.SQ_SZ and \
                    abs(dist_y) != 2 * board.SQ_SZ) \
                    or abs(dist_x) == board.SQ_SZ:
                    if pawn.colour != piece2.colour:
                        piece2.captured = True
                        # piece2.set_pos = None
                        # board.delete_piece(self.turn, piece2)
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
                            print('Yes')

    def handle_king(self, board, piece1, sq1_pos, sq2_pos):
        king = piece1
        piece2 = board.fetch_piece(sq2_pos)

        dist_x = sq2_pos[0] - sq1_pos[0]
        dist_y = sq2_pos[1] - sq1_pos[1]

        if board.is_controlled_sq(sq2_pos):
            print("Controlled sq")

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
                    # piece2.set_pos = None
                    # board.delete_piece(self.turn, piece2)
                    king.move(sq2_pos)
                    board.king_pos[self.turn] = sq2_pos

        # Discovered attack by king
        if board.is_controlled_sq(board.king_pos[self.turn], self.turn):
            self.under_check = True
            print("Yes")

    def handle_bishop(self, board, piece1, sq1_pos, sq2_pos):
        bishop = piece1
        piece2 = board.fetch_piece(sq2_pos)

        dist_x = sq2_pos[0] - sq1_pos[0]
        dist_y = sq2_pos[1] - sq1_pos[1]

        if not piece2:
            if sq2_pos in self.valid_moves:
                if not bishop.move_through(board, sq1_pos, dist_x, dist_y):
                    bishop.move(sq2_pos)

                    # if self.under_check:
                    if board.is_controlled_sq(board.king_pos[self.turn], self.turn):
                        bishop.move(sq1_pos)
                        return

                    self.turn = self.next_turn(self.turn)

        else:
            if sq2_pos in self.valid_moves:
                if bishop.colour != piece2.colour and \
                    not bishop.move_through(board, sq1_pos, dist_x, dist_y):
                    piece2.captured = True
                    # piece2.set_pos = None
                    # board.delete_piece(self.turn, piece2)
                    bishop.move(sq2_pos)

                    if self.under_check:
                        if board.is_controlled_sq(board.king_pos[self.turn], self.turn):
                            piece2.captured = False
                            bishop.move(sq1_pos)
                            return

                    self.turn = self.next_turn(self.turn)

        # Check if the bishop move caused a check to king
        if board.king_pos[self.turn] in bishop.valid_moves() and \
            not bishop.move_through(
                board, 
                sq2_pos, 
                board.king_pos[self.turn][0] - sq2_pos[0], 
                board.king_pos[self.turn][1] - sq2_pos[1]
            ) or \
            board.is_controlled_sq(board.king_pos[self.turn], self.turn):
            self.under_check = True
            print('Yes')

    def handle_knight(self, board, piece1, sq1_pos, sq2_pos):
        knight = piece1
        piece2 = board.fetch_piece(sq2_pos)

        if not piece2:
            if sq2_pos in self.valid_moves:
                knight.move(sq2_pos)

                # if self.under_check:
                if board.is_controlled_sq(board.king_pos[self.turn], self.turn):
                    knight.move(sq1_pos)
                    return

                self.turn = self.next_turn(self.turn)

                if board.king_pos[self.turn] in knight.valid_moves():
                    self.under_check = True
                    print('Yes')

        else:
            if sq2_pos in self.valid_moves:
                if knight.colour != piece2.colour:
                    piece2.captured = True
                    # piece2.set_pos = None
                    # board.delete_piece(self.turn, piece2)
                    knight.move(sq2_pos)

                    # if self.under_check:
                    if board.is_controlled_sq(board.king_pos[self.turn], self.turn):
                        piece2.captured = False
                        knight.move(sq1_pos)
                        return

                    self.turn = self.next_turn(self.turn)

                    # Check if the knight move caused a check to king
                    if board.king_pos[self.turn] in knight.valid_moves() or \
                        board.is_controlled_sq(board.king_pos[self.turn], self.turn):
                        self.under_check = True
                        print('Yes')

    def handle_rook(self, board, piece1, sq1_pos, sq2_pos):
        rook = piece1
        piece2 = board.fetch_piece(sq2_pos)

        dist_x = sq2_pos[0] - sq1_pos[0]
        dist_y = sq2_pos[1] - sq1_pos[1]

        if not piece2:
            if sq2_pos in self.valid_moves:
                if not rook.move_through(board, sq1_pos, dist_x, dist_y):
                    rook.move(sq2_pos)

                    if self.under_check:
                        if board.is_controlled_sq(board.king_pos[self.turn], self.turn):
                            rook.move(sq1_pos)
                            return

                    self.turn = self.next_turn(self.turn)

        else:
            if sq2_pos in self.valid_moves:
                if rook.colour != piece2.colour and \
                    not rook.move_through(board, sq1_pos, dist_x, dist_y):
                    piece2.captured = True
                    # piece2.set_pos = None
                    # board.delete_piece(self.turn, piece2)
                    rook.move(sq2_pos)

                    # if self.under_check:
                    if board.is_controlled_sq(board.king_pos[self.turn], self.turn):
                        piece2.captured = False
                        rook.move(sq1_pos)
                        return

                    self.turn = self.next_turn(self.turn)

        # Check if the rook move caused a check to king
        if board.king_pos[self.turn] in rook.valid_moves() and \
            not rook.move_through(
                board,
                sq2_pos,
                board.king_pos[self.turn][0] - sq2_pos[0],
                board.king_pos[self.turn][1] - sq2_pos[1]
            ):
            self.under_check = True
            print('Yes')

    def handle_queen(self, board, piece1, sq1_pos, sq2_pos):
        queen = piece1
        piece2 = board.fetch_piece(sq2_pos)

        dist_x = sq2_pos[0] - sq1_pos[0]
        dist_y = sq2_pos[1] - sq1_pos[1]

        if not piece2:
            if sq2_pos in self.valid_moves:
                if not queen.move_through(board, sq1_pos, dist_x, dist_y):
                    queen.move(sq2_pos)

                    # if self.under_check:
                    if board.is_controlled_sq(board.king_pos[self.turn], self.turn):
                        queen.move(sq1_pos)
                        return

                    self.turn = self.next_turn(self.turn)   

        else:
            if sq2_pos in self.valid_moves:
                if queen.colour != piece2.colour and \
                    not queen.move_through(board, sq1_pos, dist_x, dist_y):
                    piece2.captured = True
                    # piece2.set_pos = None
                    # board.delete_piece(self.turn, piece2)
                    queen.move(sq2_pos)

                    if self.under_check:
                        if board.is_controlled_sq(board.king_pos[self.turn], self.turn):
                            piece2.captured = False
                            queen.move(sq1_pos)
                            return

                    self.turn = self.next_turn(self.turn)

        # Check if the queen move caused a check to king
        if board.king_pos[self.turn] in queen.valid_moves() and \
            not queen.move_through(
                board,
                sq2_pos,
                board.king_pos[self.turn][0] - sq2_pos[0],
                board.king_pos[self.turn][1] - sq2_pos[1]
            ) or \
            board.is_controlled_sq(board.king_pos[self.turn], self.turn):
            self.under_check = True
            print('Yes')

    def handle_piece(self, board, piece1, sq1_pos, sq2_pos):
        if piece1.p_type == 'Pawn':
            self.handle_pawn(board, piece1, sq1_pos, sq2_pos)

        elif piece1.p_type == 'Bishop':
            self.handle_bishop(board, piece1, sq1_pos, sq2_pos)

        elif piece1.p_type == 'Knight':
            self.handle_knight(board, piece1, sq1_pos, sq2_pos)

        elif piece1.p_type == 'Rook':
            self.handle_rook(board, piece1, sq1_pos, sq2_pos)

        elif piece1.p_type == 'Queen':
            self.handle_queen(board, piece1, sq1_pos, sq2_pos)

        elif piece1.p_type == 'King':
            self.handle_king(board, piece1, sq1_pos, sq2_pos)