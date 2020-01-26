from board import SQ_SZ
from pieces.piece_store import piece_store
from utilities import next_turn, fetch_piece


def handle_pawn_move(sq1_pos, sq2_pos, valid_moves, turn):
    key1, idx1, piece1 = fetch_piece(sq1_pos)
    key2, idx2, piece2 = fetch_piece(sq2_pos)

    dist_x = sq2_pos[0] - sq1_pos[0]
    dist_y = sq2_pos[1] - sq1_pos[1]

    if not key2:
        if dist_x == 0 and sq2_pos in valid_moves:
            piece1.move(sq2_pos)
            if piece1.start_pos == True:
                piece1.start_pos = False
            turn = next_turn(turn)

    else:
        if sq2_pos in valid_moves:
            # If there's a piece directly in front of pawn
            # 1 or 2 squares (2 if at start pos)
            if piece1.p_type == 'Pawn':
                if (abs(dist_y) != SQ_SZ and abs(dist_y) != 2 * SQ_SZ) or abs(dist_x) == SQ_SZ:
                    if piece1.colour != piece2.colour:
                        # piece2.captured = True
                        # piece2.set_pos = None
                        del piece_store[key2][idx2]

                        piece1.move(sq2_pos)
                        if piece1.start_pos == True:
                            piece1.start_pos = False

                        turn = next_turn(turn)
    
    return turn

def handle_king_move(sq1_pos, sq2_pos, valid_moves, turn):
    key1, idx1, piece1 = fetch_piece(sq1_pos)
    key2, idx2, piece2 = fetch_piece(sq2_pos)

    dist_x = sq2_pos[0] - sq1_pos[0]
    dist_y = sq2_pos[1] - sq1_pos[1]

    if not key2:
        if sq2_pos in valid_moves:
            allow_castling = True
            # Checking for castling
            if abs(dist_x) == 2 * SQ_SZ:
                # Checking if piece present in b/w
                if dist_x < 0:
                    k, _, _ = fetch_piece((piece1.pos[0] - SQ_SZ, piece1.pos[1]))
                    if k:
                        allow_castling = False
                else:
                    k, _, _ = fetch_piece((piece1.pos[0] + SQ_SZ, piece1.pos[1]))
                    if k:
                        allow_castling = False

                if allow_castling:
                    rook1 = piece_store[key1][0]
                    rook2 = piece_store[key1][-1]

                    # Short castling
                    if sq1_pos[0] < sq2_pos[0] and rook2.start_pos:
                        piece1.move(sq2_pos)
                        piece1.start_pos = False
                        rook2.move((rook2.pos[0] - 2 * SQ_SZ, rook2.pos[1]))
                        rook2.start_pos = False

                    # Long castling
                    elif sq1_pos[0] > sq2_pos[0] and rook1.start_pos:
                        piece1.move(sq2_pos)
                        piece1.start_pos = False
                        rook1.move((rook1.pos[0] + 3 * SQ_SZ, rook1.pos[1]))
                        rook1.start_pos = False

                    turn = next_turn(turn)

            else:
                piece1.move(sq2_pos)
                piece1.start_pos = False
                turn = next_turn(turn)
    
    else:
        if piece1.colour != piece2.colour:
            # piece2.captured = True
            # piece2.set_pos = None
            del piece_store[key2][idx2]
            piece1.move(sq2_pos)

            turn = next_turn(turn)

    return turn


def bishop_move_through(sq1_pos, sq2_pos, dist_x, dist_y):
    # Topleft
    if dist_x < 0 and dist_y < 0:
        for i in range(1, int(abs(dist_x) / SQ_SZ)):
            k, _, _ = fetch_piece((sq1_pos[0] - i * SQ_SZ, sq1_pos[1] - i * SQ_SZ))
            if k:
                return True

    # Topright
    elif dist_x > 0 and dist_y < 0:
        for i in range(1, int(abs(dist_x) / SQ_SZ)):
            k, _, _ = fetch_piece((sq1_pos[0] + i * SQ_SZ, sq1_pos[1] - i * SQ_SZ))
            if k:
                return True

    # Bottomleft
    elif dist_x < 0 and dist_y > 0:
        for i in range(1, int(abs(dist_x) / SQ_SZ)):
            k, _, _ = fetch_piece((sq1_pos[0] - i * SQ_SZ, sq1_pos[1] + i * SQ_SZ))
            if k:
                return True

    # Bottomright
    elif dist_x > 0 and dist_y > 0:
        for i in range(1, int(abs(dist_x) / SQ_SZ)):
            k, _, _ = fetch_piece((sq1_pos[0] + i * SQ_SZ, sq1_pos[1] + i * SQ_SZ))
            if k:
                return True

    return False

def handle_bishop_move(sq1_pos, sq2_pos, valid_moves, turn):
    key1, idx1, piece1 = fetch_piece(sq1_pos)
    key2, idx2, piece2 = fetch_piece(sq2_pos)

    dist_x = sq2_pos[0] - sq1_pos[0]
    dist_y = sq2_pos[1] - sq1_pos[1]

    if not key2:
        if sq2_pos in valid_moves:
            if not bishop_move_through(sq1_pos, sq2_pos, dist_x, dist_y):
                piece1.move(sq2_pos)
                turn = next_turn(turn)

    else:
        if sq2_pos in valid_moves:
            if piece1.colour != piece2.colour and \
                not bishop_move_through(sq1_pos, sq2_pos, dist_x, dist_y):
                # piece2.captured = True
                # piece2.set_pos = None
                del piece_store[key2][idx2]
                piece1.move(sq2_pos)
                turn = next_turn(turn)

    return turn

def handle_knight_move(sq1_pos, sq2_pos, valid_moves, turn):
    key1, idx1, piece1 = fetch_piece(sq1_pos)
    key2, idx2, piece2 = fetch_piece(sq2_pos)

    if not key2:
        if sq2_pos in valid_moves:
            piece1.move(sq2_pos)
            turn = next_turn(turn)

    else:
        if sq2_pos in valid_moves:
            if piece1.colour != piece2.colour:
                # piece2.captured = True
                # piece2.set_pos = None
                del piece_store[key2][idx2]
                piece1.move(sq2_pos)

                turn = next_turn(turn)

    return turn


def rook_move_through(sq1_pos, sq2_pos, dist_x, dist_y):
    # Top
    if dist_x == 0 and dist_y < 0:
        for i in range(1, int(abs(dist_y) / SQ_SZ)):
            k, _, _ = fetch_piece((sq1_pos[0], sq1_pos[1] - i * SQ_SZ))
            if k:
                return True

    # Bottom
    elif dist_x == 0 and dist_y > 0:
        for i in range(1, int(abs(dist_y) / SQ_SZ)):
            k, _, _ = fetch_piece((sq1_pos[0], sq1_pos[1] + i * SQ_SZ))
            if k:
                return True

    # Right
    elif dist_x > 0 and dist_y == 0:
        for i in range(1, int(abs(dist_x) / SQ_SZ)):
            k, _, _ = fetch_piece((sq1_pos[0] + i * SQ_SZ, sq1_pos[1]))
            if k:
                return True

    # Left
    elif dist_x < 0 and dist_y == 0:
        for i in range(1, int(abs(dist_x) / SQ_SZ)):
            k, _, _ = fetch_piece((sq1_pos[0] - i * SQ_SZ, sq1_pos[1]))
            if k:
                return True

    return False

def handle_rook_move(sq1_pos, sq2_pos, valid_moves, turn):
    key1, idx1, piece1 = fetch_piece(sq1_pos)
    key2, idx2, piece2 = fetch_piece(sq2_pos)

    dist_x = sq2_pos[0] - sq1_pos[0]
    dist_y = sq2_pos[1] - sq1_pos[1]

    if not key2:
        if sq2_pos in valid_moves:
            if not rook_move_through(sq1_pos, sq2_pos, dist_x, dist_y):
                piece1.move(sq2_pos)
                turn = next_turn(turn)

    else:
        if sq2_pos in valid_moves:
            if piece1.colour != piece2.colour and \
                not rook_move_through(sq1_pos, sq2_pos, dist_x, dist_y):
                # piece2.captured = True
                # piece2.set_pos = None
                del piece_store[key2][idx2]
                piece1.move(sq2_pos)

                turn = next_turn(turn)

    return turn

def handle_queen_move(sq1_pos, sq2_pos, valid_moves, turn):
    key1, idx1, piece1 = fetch_piece(sq1_pos)
    key2, idx2, piece2 = fetch_piece(sq2_pos)

    dist_x = sq2_pos[0] - sq1_pos[0]
    dist_y = sq2_pos[1] - sq1_pos[1]

    if not key2:
        if sq2_pos in valid_moves:
            if dist_x and dist_y:
                if not bishop_move_through(sq1_pos, sq2_pos, dist_x, dist_y):
                    piece1.move(sq2_pos)
                    turn = next_turn(turn)
            else:
                if not rook_move_through(sq1_pos, sq2_pos, dist_x, dist_y):
                    piece1.move(sq2_pos)
                    turn = next_turn(turn)

    else:
        if sq2_pos in valid_moves:
            if piece1.colour != piece2.colour and \
                not rook_move_through(sq1_pos, sq2_pos, dist_x, dist_y):
                # piece2.captured = True
                # piece2.set_pos = None
                del piece_store[key2][idx2]
                piece1.move(sq2_pos)

                turn = next_turn(turn)

    return turn