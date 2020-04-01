from pieces import Piece
from config import BD_X, BD_Y


class King(Piece):
    value = None

    def __init__(self, p_no=None, colour='White'):
        super().__init__(p_no, colour)
        self.start_pos = True # For checking castling ability

    def valid_moves(self):
        x = self.pos[0]
        y = self.pos[1]

        SQ_SZ = self.size()
        BD_SZ = SQ_SZ * 8

        valids = []

        inc_x = x + SQ_SZ
        dec_x = x - SQ_SZ
        inc_y = y + SQ_SZ
        dec_y = y - SQ_SZ

        # Right
        if inc_x < BD_SZ:
            valids.append((inc_x, y))

        # Left
        if dec_x >= BD_X:
            valids.append((dec_x, y))

        # Down
        if inc_y < BD_SZ:
            valids.append((x, inc_y))

        # Up
        if dec_y >= BD_Y:
            valids.append((x, dec_y))

        # Bottomright
        if inc_x < BD_SZ and inc_y < BD_SZ:
            valids.append((inc_x, inc_y))

        # Bottomleft
        if dec_x >= BD_X and inc_y < BD_SZ:
            valids.append((dec_x, inc_y))

        # Topright
        if inc_x < BD_SZ and dec_y >= BD_Y:
            valids.append((inc_x, dec_y))
            
        # Topleft
        if dec_x >= BD_X and dec_y >= BD_Y:
            valids.append((dec_x, dec_y))      

        # Two squares left and right
        if self.start_pos:
            valids.append((x + 2 * SQ_SZ, y))
            valids.append((x - 2 * SQ_SZ, y))

        return valids

    def handle_move(self, board, sq1_pos, sq2_pos, under_check=False):
        def castle_king():
            if self.colour == 'White':
                            rook1 = board.pieces['w_pieces'][0]
                            rook2 = board.pieces['w_pieces'][-1]
            else:
                rook1 = board.pieces['b_pieces'][0]
                rook2 = board.pieces['b_pieces'][-1]

            # Short castling
            if sq1_pos[0] < sq2_pos[0] and rook2.start_pos:
                self.move(sq2_pos)
                board.king_pos[self.colour] = sq2_pos
                self.start_pos = False
                rook2.move((rook2.pos[0] - 2 * board.SQ_SZ, rook2.pos[1]))
                rook2.start_pos = False
                rook1.start_pos = False

            # Long castling
            elif sq1_pos[0] > sq2_pos[0] and rook1.start_pos:
                self.move(sq2_pos)
                board.king_pos[self.colour] = sq2_pos
                self.start_pos = False
                rook1.move((rook1.pos[0] + 3 * board.SQ_SZ, rook1.pos[1]))
                rook1.start_pos = False
                rook2.start_pos = False

            self.colour = self.next_turn()

        piece2 = board.fetch_piece_by_turn(sq2_pos, self.next_turn())

        dist_x, dist_y = board.calc_sq_dist(sq1_pos, sq2_pos)

        if not piece2:
            if sq2_pos in self.valid_moves() and not board.is_controlled_sq(sq2_pos, self.colour):
                if not under_check:
                    castling_allowed = True
                # Checking for castling
                if abs(dist_x) == 2 * board.SQ_SZ:
                    # Checking if piece present in b/w
                    if dist_x < 0:
                        k = board.fetch_piece((self.pos[0] - board.SQ_SZ, self.pos[1]))
                        if k:
                            castling_allowed = False
                    else:
                        k = board.fetch_piece((self.pos[0] + board.SQ_SZ, self.pos[1]))
                        if k:
                            castling_allowed = False

                    if castling_allowed:
                        castle_king()

                else:
                    self.move(sq2_pos)
                    board.king_pos[self.colour] = sq2_pos
                    self.start_pos = False
                    self.colour = self.next_turn()
        
        else:
            if not board.is_controlled_sq(sq2_pos, self.colour):
                if self.colour != piece2.colour:
                    piece2.captured = True
                    self.move(sq2_pos)
                    board.king_pos[self.colour] = sq2_pos

        # Discovered attack by self
        if board.is_controlled_sq(board.king_pos[self.colour], self.colour):
            under_check = True