class Move:
    def __init__(self):
        self.turn = 'White'
        self.valid_moves = []
        self.under_check = False

    def next_turn(self, turn):
        if turn == 'White':
            return 'Black'
        return 'White'

    def is_controlled_sq(self, board, req_pos):
        # Along ranks
            # y is constant
            # loop for x from 0 to board size
                # check if given square is valid move of piece (rook or queen) (of opposite colour) fetched from x
                    # check if it's move through a piece
                        # if it's not, return True for 1st such piece found
        x = req_pos[0]
        y = req_pos[1]

        for i in range(0, int(board.BD_SZ / board.SQ_SZ)):
            # if i * board.SQ_SZ == x:
            #     continue
            piece = board.fetch_piece((i * board.SQ_SZ, y))
            # print(i + 1, piece)

            if piece and piece.colour != self.turn and req_pos in piece.valid_moves():
                print("in valid moves of the other piece")
                if piece.p_type == 'Rook' or piece.p_type == 'Queen':
                    if not self.rook_through(board, req_pos, piece.pos[0] - x, piece.pos[1] - y):
                        return True

        # Along files
            # same as ranks
        for i in range(0, int(board.BD_SZ / board.SQ_SZ)):
            piece = board.fetch_piece((x, i * board.SQ_SZ))
            # print(i + 1, piece)

            if piece and piece.colour != self.turn and req_pos in piece.valid_moves():
                print("in valid moves of the other piece")
                if piece.p_type == 'Rook' or piece.p_type == 'Queen':
                    if not self.rook_through(board, req_pos, piece.pos[0] - x, piece.pos[1] - y):
                        return True

        # Along diagonals
            # both x and y are variables
            # loop for x,y from 0 to board size
                # check if given square is valid move of piece (bishop or queen)
                # same ...
        for i in range(0, int(board.BD_SZ / board.SQ_SZ)):
            piece = board.fetch_piece((i * board.SQ_SZ, i * board.SQ_SZ))
            # print(i + 1, piece)

            if piece and piece.colour != self.turn and req_pos in piece.valid_moves():
                print("in valid moves of the other piece")
                if piece.p_type == 'Bishop' or piece.p_type == 'Queen':
                    if not self.bishop_through(board, req_pos, piece.pos[0] - x, piece.pos[1] - y):
                        return True

        # Along knight routes (L)
        piece = board.fetch_piece(req_pos)
        # print(i + 1, piece)
        if piece and piece.colour != self.turn and req_pos in piece.valid_moves():
            print("in valid moves of the other piece")
            if piece.p_type == 'Knight':
                return True

        return False

    def handle_pawn(self, board, sq1_pos, sq2_pos):
        pawn = board.fetch_piece_by_turn(self.turn, sq1_pos)
        piece2 = board.fetch_piece(sq2_pos)

        dist_x = sq2_pos[0] - sq1_pos[0]
        dist_y = sq2_pos[1] - sq1_pos[1]

        self.valid_moves = pawn.valid_moves(board.is_flipped)

        if not piece2:
            if dist_x == 0 and sq2_pos in self.valid_moves:
                pawn.move(sq2_pos)
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
                        # piece2.captured = True
                        # piece2.set_pos = None
                        board.delete_piece(self.turn, piece2)
                        pawn.move(sq2_pos)
                        if pawn.start_pos == True:
                            pawn.start_pos = False

                        self.turn = self.next_turn(self.turn)

                        if board.king_pos[self.turn] in pawn.valid_moves(board.is_flipped):
                            self.under_check = True
                            print('Yes')

    def handle_king(self, board, sq1_pos, sq2_pos):
        king = board.fetch_piece_by_turn(self.turn, sq1_pos)
        piece2 = board.fetch_piece(sq2_pos)

        dist_x = sq2_pos[0] - sq1_pos[0]
        dist_y = sq2_pos[1] - sq1_pos[1]

        self.valid_moves = king.valid_moves()

        if self.is_controlled_sq(board, sq2_pos):
            print("Controlled sq")

        if not piece2:
            if sq2_pos in self.valid_moves:
                allow_castling = True
                # Checking for castling
                if abs(dist_x) == 2 * board.SQ_SZ:
                    # Checking if piece present in b/w
                    if dist_x < 0:
                        k = board.fetch_piece((king.pos[0] - board.SQ_SZ, king.pos[1]))
                        if k:
                            allow_castling = False
                    else:
                        k = board.fetch_piece((king.pos[0] + board.SQ_SZ, king.pos[1]))
                        if k:
                            allow_castling = False

                    if allow_castling:
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
            if king.colour != piece2.colour:
                # piece2.captured = True
                # piece2.set_pos = None
                board.delete_piece(self.turn, piece2)
                king.move(sq2_pos)
                board.king_pos[self.turn] = sq2_pos

    def bishop_through(self, board, req_pos, dist_x, dist_y):
        # Topleft
        if dist_x < 0 and dist_y < 0:
            for i in range(1, int(abs(dist_x) / board.SQ_SZ)):
                k = board.fetch_piece((req_pos[0] - i * board.SQ_SZ, req_pos[1] - i * board.SQ_SZ))
                if k:
                    return True

        # Topright
        elif dist_x > 0 and dist_y < 0:
            for i in range(1, int(abs(dist_x) / board.SQ_SZ)):
                k = board.fetch_piece((req_pos[0] + i * board.SQ_SZ, req_pos[1] - i * board.SQ_SZ))
                if k:
                    return True

        # Bottomleft
        elif dist_x < 0 and dist_y > 0:
            for i in range(1, int(abs(dist_x) / board.SQ_SZ)):
                k = board.fetch_piece((req_pos[0] - i * board.SQ_SZ, req_pos[1] + i * board.SQ_SZ))
                if k:
                    return True

        # Bottomright
        elif dist_x > 0 and dist_y > 0:
            for i in range(1, int(abs(dist_x) / board.SQ_SZ)):
                k = board.fetch_piece((req_pos[0] + i * board.SQ_SZ, req_pos[1] + i * board.SQ_SZ))
                if k:
                    return True

        return False

    def handle_bishop(self, board, sq1_pos, sq2_pos):
        bishop = board.fetch_piece_by_turn(self.turn, sq1_pos)
        piece2 = board.fetch_piece(sq2_pos)

        dist_x = sq2_pos[0] - sq1_pos[0]
        dist_y = sq2_pos[1] - sq1_pos[1]

        self.valid_moves = bishop.valid_moves()

        if not piece2:
            if sq2_pos in self.valid_moves:
                if not self.bishop_through(board, sq1_pos, dist_x, dist_y):
                    bishop.move(sq2_pos)

                    self.turn = self.next_turn(self.turn)

        else:
            if sq2_pos in self.valid_moves:
                if bishop.colour != piece2.colour and \
                    not self.bishop_through(board, sq1_pos, dist_x, dist_y):
                    # piece2.captured = True
                    # piece2.set_pos = None
                    board.delete_piece(self.turn, piece2)
                    bishop.move(sq2_pos)

                    self.turn = self.next_turn(self.turn)

        if board.king_pos[self.turn] in bishop.valid_moves() and \
            not self.bishop_through(
                board, 
                sq2_pos, 
                board.king_pos[self.turn][0] - sq2_pos[0], 
                board.king_pos[self.turn][1] - sq2_pos[1]
            ):
            self.under_check = True
            print('Yes')

    def handle_knight(self, board, sq1_pos, sq2_pos):
        knight = board.fetch_piece_by_turn(self.turn, sq1_pos)
        piece2 = board.fetch_piece(sq2_pos)

        self.valid_moves = knight.valid_moves()

        if not piece2:
            if sq2_pos in self.valid_moves:
                knight.move(sq2_pos)

                self.turn = self.next_turn(self.turn)

                if board.king_pos[self.turn] in knight.valid_moves():
                    self.under_check = True
                    print('Yes')

        else:
            if sq2_pos in self.valid_moves:
                if knight.colour != piece2.colour:
                    # piece2.captured = True
                    # piece2.set_pos = None
                    board.delete_piece(self.turn, piece2)
                    knight.move(sq2_pos)

                    self.turn = self.next_turn(self.turn)

                    if board.king_pos[self.turn] in knight.valid_moves():
                        self.under_check = True
                        print('Yes')


    def rook_through(self, board, sq1_pos, dist_x, dist_y):
        # Top
        if dist_x == 0 and dist_y < 0:
            for i in range(1, int(abs(dist_y) / board.SQ_SZ)):
                k = board.fetch_piece((sq1_pos[0], sq1_pos[1] - i * board.SQ_SZ))
                if k:
                    return True

        # Bottom
        elif dist_x == 0 and dist_y > 0:
            for i in range(1, int(abs(dist_y) / board.SQ_SZ)):
                k = board.fetch_piece((sq1_pos[0], sq1_pos[1] + i * board.SQ_SZ))
                if k:
                    return True

        # Right
        elif dist_x > 0 and dist_y == 0:
            for i in range(1, int(abs(dist_x) / board.SQ_SZ)):
                k = board.fetch_piece((sq1_pos[0] + i * board.SQ_SZ, sq1_pos[1]))
                if k:
                    return True

        # Left
        elif dist_x < 0 and dist_y == 0:
            for i in range(1, int(abs(dist_x) / board.SQ_SZ)):
                k = board.fetch_piece((sq1_pos[0] - i * board.SQ_SZ, sq1_pos[1]))
                if k:
                    return True

        return False

    def handle_rook(self, board, sq1_pos, sq2_pos):
        rook = board.fetch_piece_by_turn(self.turn, sq1_pos)
        piece2 = board.fetch_piece(sq2_pos)

        dist_x = sq2_pos[0] - sq1_pos[0]
        dist_y = sq2_pos[1] - sq1_pos[1]

        self.valid_moves = rook.valid_moves()

        if not piece2:
            if sq2_pos in self.valid_moves:
                if not self.rook_through(board, sq1_pos, dist_x, dist_y):
                    rook.move(sq2_pos)

                    self.turn = self.next_turn(self.turn)

        else:
            if sq2_pos in self.valid_moves:
                if rook.colour != piece2.colour and \
                    not self.rook_through(board, sq1_pos, dist_x, dist_y):
                    # piece2.captured = True
                    # piece2.set_pos = None
                    board.delete_piece(self.turn, piece2)
                    rook.move(sq2_pos)

                    self.turn = self.next_turn(self.turn)

        if board.king_pos[self.turn] in rook.valid_moves() and \
            not self.rook_through(
                board,
                sq2_pos,
                board.king_pos[self.turn][0] - sq2_pos[0],
                board.king_pos[self.turn][1] - sq2_pos[1]
            ):
            self.under_check = True
            print('Yes')

    def handle_queen(self, board, sq1_pos, sq2_pos):
        queen = board.fetch_piece_by_turn(self.turn, sq1_pos)
        piece2 = board.fetch_piece(sq2_pos)

        dist_x = sq2_pos[0] - sq1_pos[0]
        dist_y = sq2_pos[1] - sq1_pos[1]

        self.valid_moves = queen.valid_moves()

        if not piece2:
            if sq2_pos in self.valid_moves:
                # Bishop move
                if dist_x and dist_y:
                    if not self.bishop_through(board, sq1_pos, dist_x, dist_y):
                        queen.move(sq2_pos)

                        self.turn = self.next_turn(self.turn)

                # Rook move
                elif (dist_x == 0 and dist_y) or (dist_y == 0 and dist_x):
                    if not self.rook_through(board, sq1_pos, dist_x, dist_y):
                        queen.move(sq2_pos)

                        self.turn = self.next_turn(self.turn)

        else:
            if sq2_pos in self.valid_moves:
                if queen.colour != piece2.colour and \
                    not self.rook_through(board, sq1_pos, dist_x, dist_y) and \
                        not self.bishop_through(board, sq1_pos, dist_x, dist_y):
                    # piece2.captured = True
                    # piece2.set_pos = None
                    board.delete_piece(self.turn, piece2)
                    queen.move(sq2_pos)

                    self.turn = self.next_turn(self.turn)

        if board.king_pos[self.turn] in queen.valid_moves() and \
            not self.bishop_through(
                board, 
                sq2_pos, 
                board.king_pos[self.turn][0] - sq2_pos[0], 
                board.king_pos[self.turn][1] - sq2_pos[1]
            ) and \
            not self.rook_through(
                board, 
                sq2_pos, 
                board.king_pos[self.turn][0] - sq2_pos[0], 
                board.king_pos[self.turn][1] - sq2_pos[1]
            ):
            self.under_check = True
            print('Yes')

    def handle_piece(self, board, sq1_pos, sq2_pos):
        piece1 = board.fetch_piece_by_turn(self.turn, sq1_pos)

        if piece1.p_type == 'Pawn':
            self.handle_pawn(board, sq1_pos, sq2_pos)

        elif piece1.p_type == 'Bishop':
            self.handle_bishop(board, sq1_pos, sq2_pos)

        elif piece1.p_type == 'Knight':
            self.handle_knight(board, sq1_pos, sq2_pos)

        elif piece1.p_type == 'Rook':
            self.handle_rook(board, sq1_pos, sq2_pos)

        elif piece1.p_type == 'Queen':
            self.handle_queen(board, sq1_pos, sq2_pos)

        elif piece1.p_type == 'King':
            self.handle_king(board, sq1_pos, sq2_pos)