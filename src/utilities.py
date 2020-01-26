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


def calc_sq_pos(mouse_pos):
    '''Calculates and returns topleft position of the square clicked'''

    coeff_x = mouse_pos[0] // SQ_SZ
    coeff_y = mouse_pos[1] // SQ_SZ

    return (SQ_SZ * coeff_x, SQ_SZ * coeff_y)


def fetch_piece_by_turn(req_pos, turn):
    '''Fetches piece (by turn) present at a given position on the board'''

    if turn == 'White':
        for idx, w_pawn in enumerate(piece_store['w_pawns']):
            if w_pawn.pos == req_pos:
                return w_pawn

        for idx, w_piece in enumerate(piece_store['w_pieces']):
            if w_piece.pos == req_pos:
                return w_piece

    else:
        for idx, b_pawn in enumerate(piece_store['b_pawns']):
            if b_pawn.pos == req_pos:
                return b_pawn

        for idx, b_piece in enumerate(piece_store['b_pieces']):
            if b_piece.pos == req_pos:
                return b_piece

    return None


def fetch_piece(req_pos):
    '''Fetches piece present at a given position on the board'''

    for idx, w_pawn in enumerate(piece_store['w_pawns']):
        if w_pawn.pos == req_pos:
            return w_pawn

    for idx, w_piece in enumerate(piece_store['w_pieces']):
        if w_piece.pos == req_pos:
            return w_piece

    for idx, b_pawn in enumerate(piece_store['b_pawns']):
        if b_pawn.pos == req_pos:
            return b_pawn

    for idx, b_piece in enumerate(piece_store['b_pieces']):
        if b_piece.pos == req_pos:
            return b_piece

    return None


def king_is_present(req_pos, turn):
    if turn == 'White':
        for w_piece in piece_store['w_pieces']:
            if w_piece.p_type == 'King' and w_piece.pos == req_pos:
                return True
    else:
        for b_piece in piece_store['b_pieces']:
            if b_piece.p_type == 'King' and b_piece.pos == req_pos:
                return True

    return False


def delete_piece(piece, turn):
    '''Deletes a given piece from the list of pieces'''

    if turn == 'White':
        if piece.p_type == 'Pawn':
            piece_store['w_pawns'].remove(piece)
        else:
            piece_store['w_pieces'].remove(piece)

    else:
        if piece.p_type == 'Pawn':
            piece_store['b_pawns'].remove(piece)
        else:
            piece_store['b_pieces'].remove(piece)


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


