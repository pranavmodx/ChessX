from pieces import Piece
from config import BD_X, BD_Y


class Bishop(Piece):
    value = 3

    def __init__(self, p_type='Bishop', p_no=None, colour='White'):
        super().__init__(p_type, p_no, colour)

    def valid_moves(self):
        x = self.pos[0]
        y = self.pos[1]

        SQ_SZ = self.size()
        BD_SZ = SQ_SZ * 8

        valids = []

        for i in range(1, 8):
            inc_x = x + i * SQ_SZ
            dec_x = x - i * SQ_SZ
            inc_y = y + i * SQ_SZ
            dec_y = y - i * SQ_SZ

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

        return valids

    @staticmethod
    def move_through(board, req_pos, dist_x, dist_y):
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