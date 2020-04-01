from pieces import Piece
from config import BD_X, BD_Y


class Knight(Piece):
    value = 3

    def __init__(self, p_no=None, colour='White'):
        super().__init__(p_no, colour)

    def valid_moves(self):
        x = self.pos[0]
        y = self.pos[1]

        SQ_SZ = self.size()
        BD_SZ = SQ_SZ * 8

        valids = []

        inc_x1 = x + SQ_SZ
        dec_x1 = x - SQ_SZ
        inc_y1 = y + SQ_SZ
        dec_y1 = y - SQ_SZ

        inc_x2 = x + 2 * SQ_SZ
        dec_x2 = x - 2 * SQ_SZ
        inc_y2 = y + 2 * SQ_SZ
        dec_y2 = y - 2 * SQ_SZ

        if inc_x1 < BD_SZ and inc_y2 < BD_SZ:  
            valids.append((inc_x1, inc_y2))

        if dec_x1 >= BD_X and inc_y2 < BD_SZ:  
            valids.append((dec_x1, inc_y2))

        if inc_x1 < BD_SZ and dec_y2 >= BD_Y:  
            valids.append((inc_x1, dec_y2))

        if dec_x1 >= BD_X and dec_y2 >= BD_Y:  
            valids.append((dec_x1, dec_y2))

        if inc_x2 < BD_SZ and inc_y1 < BD_SZ:  
            valids.append((inc_x2, inc_y1))

        if dec_x2 >= BD_X and inc_y1 < BD_SZ:  
            valids.append((dec_x2, inc_y1))

        if inc_x2 < BD_SZ and dec_y1 >= BD_Y:  
            valids.append((inc_x2, dec_y1))

        if dec_x2 >= BD_X and dec_y1 >= BD_Y:  
            valids.append((dec_x2, dec_y1))
            
        return valids

    def handle_move(self, board, sq1_pos, sq2_pos, under_check=False):
        piece2 = board.fetch_piece_by_turn(sq2_pos, self.next_turn())

        if not piece2:
            if sq2_pos in self.valid_moves():
                self.move(sq2_pos)

                if board.is_controlled_sq(board.king_pos[self.colour], self.colour):
                    self.move(sq1_pos)
                    return

                return 1

        else:
            if sq2_pos in self.valid_moves():
                if self.colour != piece2.colour:
                    piece2.captured = True
                    self.move(sq2_pos)

                    if under_check:
                        if board.is_controlled_sq(board.king_pos[self.colour], self.colour):
                            piece2.captured = False
                            self.move(sq1_pos)
                            return

                    return 1

        # Check if the self move caused a check to king
        if board.king_pos[self.colour] in self.valid_moves() or \
            board.is_controlled_sq(board.king_pos[self.colour], self.colour):
            under_check = True
