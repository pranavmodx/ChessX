from board import bd_obj, BD_SZ, SQ_SZ
from pieces.piece_store import piece_store

import pygame


def display_all(screen):
    '''Display(show) all objects'''

    bd_obj.show(screen)

    for piece_list in piece_store.values():
        for piece in piece_list:
            # if not piece.captured:
            piece.show(screen)

def calc_sq_pos(mouse_pos):
    '''Calculates and returns topleft position of the square clicked'''

    coeff_x = mouse_pos[0] // SQ_SZ
    coeff_y = mouse_pos[1] // SQ_SZ

    return (SQ_SZ * coeff_x, SQ_SZ * coeff_y)


def fetch_piece(req_pos):
    '''Fetches piece present at a given position on the board'''

    found = 0

    for idx, w_pawn in enumerate(piece_store['w_pawns']):
        if w_pawn.pos == req_pos:
            found = 1
            return 'w_pawns', idx, piece_store['w_pawns'][idx]

    if found == 0:
        for idx, w_piece in enumerate(piece_store['w_pieces']):
            if w_piece.pos == req_pos:
                found = 1
                return 'w_pieces', idx, piece_store['w_pieces'][idx]

    if found == 0:
        for idx, b_pawn in enumerate(piece_store['b_pawns']):
            if b_pawn.pos == req_pos:
                found = 1
                return 'b_pawns', idx, piece_store['b_pawns'][idx]

    if found == 0:
        for idx, b_piece in enumerate(piece_store['b_pieces']):
            if b_piece.pos == req_pos:
                found = 1
                return 'b_pieces', idx, piece_store['b_pieces'][idx]

    return None, None, None


def delete_piece(piece):
    '''Deletes a given piece from the list of pieces'''

    if piece.p_type == 'Pawn':
        if piece.colour == 'White':
            piece_store['w_pawns'].remove(piece)
        else:
            piece_store['b_pawns'].remove(piece)

    else:
        if piece.colour == 'White':
            piece_store['w_pieces'].remove(piece)
        else:
            piece_store['b_pieces'].remove(piece)


def flip_board():
    for w_pawn in piece_store['w_pawns']:
        w_pawn.set_pos(
            (
                BD_SZ - w_pawn.pos[0] - SQ_SZ,
                BD_SZ - w_pawn.pos[1] - SQ_SZ
            )
        )

    for b_pawn in piece_store['b_pawns']:
        b_pawn.set_pos(
            (
                BD_SZ - b_pawn.pos[0] - SQ_SZ,
                BD_SZ - b_pawn.pos[1] - SQ_SZ
            )
        )

    for w_piece in piece_store['w_pieces']:
        w_piece.set_pos(
            (
                BD_SZ - w_piece.pos[0] - SQ_SZ,
                BD_SZ - w_piece.pos[1] - SQ_SZ
            )
        )

    for b_piece in piece_store['b_pieces']:
        b_piece.set_pos(
            (
                BD_SZ - b_piece.pos[0] - SQ_SZ,
                BD_SZ - b_piece.pos[1] - SQ_SZ
            )
        )


def highlight_square(surface, color, rect_dim, width=3):
    r_left, r_top = rect_dim
    r_width = SQ_SZ
    r_height = SQ_SZ

    pygame.draw.rect(
        surface,
        color,
        pygame.Rect(r_left, r_top, r_width, r_height),
        width
    )


def next_turn(turn):
    if turn == 'White':
        return 'Black'
    return 'White'


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
                    k, _ = fetch_piece_loc((piece1.pos[0] - SQ_SZ, piece1.pos[1]))
                    if k:
                        allow_castling = False
                else:
                    k, _ = fetch_piece_loc((piece1.pos[0] + SQ_SZ, piece1.pos[1]))
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

def handle_bishop_move(sq1_pos, sq2_pos, valid_moves, turn):
    key1, idx1, piece1 = fetch_piece(sq1_pos)
    key2, idx2, piece2 = fetch_piece(sq2_pos)

    if not key2:
        if sq2_pos in valid_moves:
            piece1.move(sq2_pos)
            turn = next_turn(turn)

    else:
        if sq2_pos in valid_moves:
            # For all other pieces
            if piece1.colour != piece2.colour:
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
            # For all other pieces
            if piece1.colour != piece2.colour:
                # piece2.captured = True
                # piece2.set_pos = None
                del piece_store[key2][idx2]
                piece1.move(sq2_pos)

                turn = next_turn(turn)

    return turn

def handle_rook_move(sq1_pos, sq2_pos, valid_moves, turn):
    key1, idx1, piece1 = fetch_piece(sq1_pos)
    key2, idx2, piece2 = fetch_piece(sq2_pos)

    if not key2:
        if sq2_pos in valid_moves:
            piece1.move(sq2_pos)
            turn = next_turn(turn)

    else:
        if sq2_pos in valid_moves:
            # For all other pieces
            if piece1.colour != piece2.colour:
                # piece2.captured = True
                # piece2.set_pos = None
                del piece_store[key2][idx2]
                piece1.move(sq2_pos)

                turn = next_turn(turn)

    return turn

def handle_queen_move(sq1_pos, sq2_pos, valid_moves, turn):
    key1, idx1, piece1 = fetch_piece(sq1_pos)
    key2, idx2, piece2 = fetch_piece(sq2_pos)

    if not key2:
        if sq2_pos in valid_moves:
            piece1.move(sq2_pos)
            turn = next_turn(turn)

    else:
        if sq2_pos in valid_moves:
            # For all other pieces
            if piece1.colour != piece2.colour:
                # piece2.captured = True
                # piece2.set_pos = None
                del piece_store[key2][idx2]
                piece1.move(sq2_pos)

                turn = next_turn(turn)

    return turn