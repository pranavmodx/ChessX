class Move:
    def __init__(self):
        self.turn = 'White'
        self.valid_moves = []

    def next_turn(self, turn):
        if turn == 'White':
            return 'Black'
        return 'White'

    def fetch_piece_by_turn(self, board, req_pos):
        '''Fetches piece (by turn) present at a given position on the board'''

        if self.turn == 'White':
            for w_pawn in board.pieces['w_pawns']:
                if w_pawn.pos == req_pos:
                    return w_pawn

            for w_piece in board.pieces['w_pieces']:
                if w_piece.pos == req_pos:
                    return w_piece

        else:
            for b_pawn in board.pieces['b_pawns']:
                if b_pawn.pos == req_pos:
                    return b_pawn

            for b_piece in board.pieces['b_pieces']:
                if b_piece.pos == req_pos:
                    return b_piece

        return None

    def fetch_piece(self, board, req_pos):
        '''Fetches piece present at a given position on the board'''

        for w_pawn in board.pieces['w_pawns']:
            if w_pawn.pos == req_pos:
                return w_pawn

        for w_piece in board.pieces['w_pieces']:
            if w_piece.pos == req_pos:
                return w_piece

        for b_pawn in board.pieces['b_pawns']:
            if b_pawn.pos == req_pos:
                return b_pawn

        for b_piece in board.pieces['b_pieces']:
            if b_piece.pos == req_pos:
                return b_piece

        return None

    def delete_piece(self, board, piece):
        '''Deletes a given piece from the list of pieces'''

        if self.turn == 'White':
            if piece.p_type == 'Pawn':
                board.piece_store['w_pawns'].remove(piece)
            else:
                board.piece_store['w_pieces'].remove(piece)

        else:
            if piece.p_type == 'Pawn':
                board.piece_store['b_pawns'].remove(piece)
            else:
                board.piece_store['b_pieces'].remove(piece)

    def handle_pawn(self, board, sq1_pos, sq2_pos):
        pawn = self.fetch_piece_by_turn(board, sq1_pos)
        piece2 = self.fetch_piece(board, sq2_pos)

        dist_x = sq2_pos[0] - sq1_pos[0]
        dist_y = sq2_pos[1] - sq1_pos[1]

        if not piece2:
            if dist_x == 0 and sq2_pos in self.valid_moves:
                pawn.move(sq2_pos)
                if pawn.start_pos == True:
                    pawn.start_pos = False
                self.turn = self.next_turn(self.turn)

        else:
            if sq2_pos in self.valid_moves:
                # If there's a piece directly in front of pawn
                # 1 or 2 squares (2 if at start pos)
                if (abs(dist_y) != board.SQ_SZ and abs(dist_y) != 2 * board.SQ_SZ) or abs(dist_x) == board.SQ_SZ:
                    if pawn.colour != piece2.colour:
                        # piece2.captured = True
                        # piece2.set_pos = None
                        self.delete_piece(piece2, self.next_turn(self.turn))

                        pawn.move(sq2_pos)
                        if pawn.start_pos == True:
                            pawn.start_pos = False

                        self.turn = self.next_turn(self.turn)

    def handle_king(self, sq1_pos, sq2_pos):
        king = self.fetch_piece_by_turn(board, sq1_pos)
        piece2 = self.fetch_piece(board, sq2_pos)

        dist_x = sq2_pos[0] - sq1_pos[0]
        dist_y = sq2_pos[1] - sq1_pos[1]

        if not piece2:
            if sq2_pos in self.valid_moves:
                allow_castling = True
                # Checking for castling
                if abs(dist_x) == 2 * SQ_SZ:
                    # Checking if piece present in b/w
                    if dist_x < 0:
                        k = self.fetch_piece((king.pos[0] - SQ_SZ, king.pos[1]))
                        if k:
                            allow_castling = False
                    else:
                        k = self.fetch_piece((king.pos[0] + SQ_SZ, king.pos[1]))
                        if k:
                            allow_castling = False

                    if allow_castling:
                        if turn == 'White':
                            rook1 = piece_store['w_pieces'][0]
                            rook2 = piece_store['w_pieces'][-1]
                        else:
                            rook1 = piece_store['b_pieces'][0]
                            rook2 = piece_store['b_pieces'][-1]

                        # Short castling
                        if sq1_pos[0] < sq2_pos[0] and rook2.start_pos:
                            king.move(sq2_pos)
                            king.start_pos = False
                            rook2.move((rook2.pos[0] - 2 * SQ_SZ, rook2.pos[1]))
                            rook2.start_pos = False
                            rook1.start_pos = False

                        # Long castling
                        elif sq1_pos[0] > sq2_pos[0] and rook1.start_pos:
                            king.move(sq2_pos)
                            king.start_pos = False
                            rook1.move((rook1.pos[0] + 3 * SQ_SZ, rook1.pos[1]))
                            rook1.start_pos = False
                            rook2.start_pos = False

                        self.turn = self.next_turn(turn)

                else:
                    king.move(sq2_pos)
                    king.start_pos = False
                    self.turn = self.next_turn(self.turn)
        
        else:
            if king.colour != piece2.colour:
                # piece2.captured = True
                # piece2.set_pos = None
                self.delete_piece(piece2, self.next_turn(turn))
                king.move(sq2_pos)

                self.turn = self.next_turn(self.turn)


    def bishop_through(self, sq1_pos, dist_x, dist_y):
        # Topleft
        if dist_x < 0 and dist_y < 0:
            for i in range(1, int(abs(dist_x) / SQ_SZ)):
                k = self.fetch_piece((sq1_pos[0] - i * SQ_SZ, sq1_pos[1] - i * SQ_SZ))
                if k:
                    return True

        # Topright
        elif dist_x > 0 and dist_y < 0:
            for i in range(1, int(abs(dist_x) / SQ_SZ)):
                k = self.fetch_piece((sq1_pos[0] + i * SQ_SZ, sq1_pos[1] - i * SQ_SZ))
                if k:
                    return True

        # Bottomleft
        elif dist_x < 0 and dist_y > 0:
            for i in range(1, int(abs(dist_x) / SQ_SZ)):
                k = self.fetch_piece((sq1_pos[0] - i * SQ_SZ, sq1_pos[1] + i * SQ_SZ))
                if k:
                    return True

        # Bottomright
        elif dist_x > 0 and dist_y > 0:
            for i in range(1, int(abs(dist_x) / SQ_SZ)):
                k = self.fetch_piece((sq1_pos[0] + i * SQ_SZ, sq1_pos[1] + i * SQ_SZ))
                if k:
                    return True

        return False

    def handle_bishop(self, sq1_pos, sq2_pos):
        bishop = self.fetch_piece_by_turn(board, sq1_pos)
        piece2 = self.fetch_piece(board, sq2_pos)

        dist_x = sq2_pos[0] - sq1_pos[0]
        dist_y = sq2_pos[1] - sq1_pos[1]

        self.valid_moves = queen.valid_moves()

        if not piece2:
            if sq2_pos in self.valid_moves:
                if not self.bishop_through(sq1_pos, dist_x, dist_y):
                    bishop.move(sq2_pos)
                    self.turn = self.next_turn(self.turn)

        else:
            if sq2_pos in self.valid_moves:
                if bishop.colour != piece2.colour and \
                    not self.bishop_through(sq1_pos, dist_x, dist_y):
                    # piece2.captured = True
                    # piece2.set_pos = None
                    self.delete_piece(piece2, self.next_turn(turn))
                    bishop.move(sq2_pos)
                    self.turn = self.next_turn(self.turn)

    def handle_knight(self, sq1_pos, sq2_pos):
        knight = self.fetch_piece_by_turn(board, sq1_pos)
        piece2 = self.fetch_piece(board, sq2_pos)

        self.valid_moves = queen.valid_moves()

        if not piece2:
            if sq2_pos in self.valid_moves:
                knight.move(sq2_pos)
                self.turn = self.next_turn(self.turn)

        else:
            if sq2_pos in self.valid_moves:
                if knight.colour != piece2.colour:
                    # piece2.captured = True
                    # piece2.set_pos = None
                    self.delete_piece(piece2, self.next_turn(turn))
                    knight.move(sq2_pos)

                    self.turn = self.next_turn(self.turn)


    def rook_through(self, sq1_pos, dist_x, dist_y):
        # Top
        if dist_x == 0 and dist_y < 0:
            for i in range(1, int(abs(dist_y) / SQ_SZ)):
                k = self.fetch_piece((sq1_pos[0], sq1_pos[1] - i * SQ_SZ))
                if k:
                    return True

        # Bottom
        elif dist_x == 0 and dist_y > 0:
            for i in range(1, int(abs(dist_y) / SQ_SZ)):
                k = self.fetch_piece((sq1_pos[0], sq1_pos[1] + i * SQ_SZ))
                if k:
                    return True

        # Right
        elif dist_x > 0 and dist_y == 0:
            for i in range(1, int(abs(dist_x) / SQ_SZ)):
                k = self.fetch_piece((sq1_pos[0] + i * SQ_SZ, sq1_pos[1]))
                if k:
                    return True

        # Left
        elif dist_x < 0 and dist_y == 0:
            for i in range(1, int(abs(dist_x) / SQ_SZ)):
                k = self.fetch_piece((sq1_pos[0] - i * SQ_SZ, sq1_pos[1]))
                if k:
                    return True

        return False

    def handle_rook(self, sq1_pos, sq2_pos):
        rook = self.fetch_piece_by_turn(board, sq1_pos)
        piece2 = self.fetch_piece(board, sq2_pos)

        dist_x = sq2_pos[0] - sq1_pos[0]
        dist_y = sq2_pos[1] - sq1_pos[1]

        self.valid_moves = queen.valid_moves()

        if not piece2:
            if sq2_pos in self.valid_moves:
                if not self.rook_through(sq1_pos, dist_x, dist_y):
                    rook.move(sq2_pos)
                    self.turn = self.next_turn(self.turn)

        else:
            if sq2_pos in self.valid_moves:
                if rook.colour != piece2.colour and \
                    not self.rook_through(sq1_pos, dist_x, dist_y):
                    # piece2.captured = True
                    # piece2.set_pos = None
                    self.delete_piece(piece2, self.next_turn(self.turn))
                    rook.move(sq2_pos)

                    self.turn = self.next_turn(self.turn)

    def handle_queen(self, sq1_pos, sq2_pos):
        queen = self.fetch_piece_by_turn(board, sq1_pos)
        piece2 = self.fetch_piece(board, sq2_pos)

        dist_x = sq2_pos[0] - sq1_pos[0]
        dist_y = sq2_pos[1] - sq1_pos[1]

        self.valid_moves = queen.valid_moves()

        if not piece2:
            if sq2_pos in self.valid_moves:
                if dist_x and dist_y:
                    if not self.bishop_through(sq1_pos, dist_x, dist_y):
                        queen.move(sq2_pos)
                        self.turn = self.self.next_turn(self.turn)
                elif (dist_x == 0 and dist_y) or (dist_y == 0 and dist_x):
                    if not self.rook_through(sq1_pos, dist_x, dist_y):
                        queen.move(sq2_pos)
                        self.turn = self.next_turn(self.turn)

        else:
            if sq2_pos in self.valid_moves:
                if queen.colour != piece2.colour and \
                    not self.rook_through(sq1_pos, dist_x, dist_y) and \
                        not self.bishop_through(sq1_pos, dist_x, dist_y):
                    # piece2.captured = True
                    # piece2.set_pos = None
                    self.delete_piece(piece2, self.next_turn(self.turn))
                    queen.move(sq2_pos)

                    self.turn = self.self.next_turn(self.turn)

    def handle_piece(self, board, sq1_pos, sq2_pos):
        piece1 = self.fetch_piece_by_turn(board, sq1_pos)
        # piece2 = self.fetch_piece(board, sq2_pos)

        dist_x = sq2_pos[0] - sq1_pos[0]
        dist_y = sq2_pos[1] - sq1_pos[1]

        self.valid_moves = piece1.valid_moves()

        if piece1.p_type == 'Pawn':
            self.turn = self.handle_pawn(board, sq1_pos, sq2_pos)

        elif piece1.p_type == 'Bishop':
            self.turn = self.handle_bishop(sq1_pos, sq2_pos)

        elif piece1.p_type == 'Knight':
            self.turn = self.handle_knight(sq1_pos, sq2_pos)

        elif piece1.p_type == 'Rook':
            self.turn = self.handle_rook(sq1_pos, sq2_pos)

        elif piece1.p_type == 'Queen':
            self.turn = self.handle_queen(sq1_pos, sq2_pos)

        elif piece1.p_type == 'King':
            self.turn = self.handle_king(sq1_pos, sq2_pos)