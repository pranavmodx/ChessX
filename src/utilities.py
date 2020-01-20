from board import bd_obj, BD_SZ, SQ_SZ
from pieces.pieces import (
    w_pawns, b_pawns,
    w_pieces, b_pieces
)

import pygame


def display_all(screen):
    '''Display(show) all objects'''

    bd_obj.show(screen)

    for w_pawn in w_pawns:
        if not w_pawn.captured:
            w_pawn.show(screen)

    for w_piece in w_pieces:
        if not w_piece.captured:
            w_piece.show(screen)

    for b_pawn in b_pawns:
        if not b_pawn.captured:
            b_pawn.show(screen) 

    for b_piece in b_pieces:
        if not b_piece.captured:
            b_piece.show(screen)


def calc_sq_pos(mouse_pos):
    '''Calculates and returns topleft position of the square clicked'''

    coeff_x = mouse_pos[0] // SQ_SZ
    coeff_y = mouse_pos[1] // SQ_SZ

    return (SQ_SZ * coeff_x, SQ_SZ * coeff_y)


def fetch_piece_loc(req_pos):
    '''Fetches piece present at a given position'''

    found = 0

    for i, w_pawn in enumerate(w_pawns):
        if w_pawn.pos == req_pos:
            found = 1
            return i, w_pawns

    if found == 0:
        for i, w_piece in enumerate(w_pieces):
            if w_piece.pos == req_pos:
                found = 1
                return i, w_pieces

    if found == 0:
        for i, b_pawn in enumerate(b_pawns):
            if b_pawn.pos == req_pos:
                found = 1
                return i, b_pawns

    if found == 0:
        for i, b_piece in enumerate(b_pieces):
            if b_piece.pos == req_pos:
                found = 1
                return i, b_pieces

    return None, None


def delete_piece(piece):
    '''Deletes a given piece from the list of pieces'''

    if piece.p_type == 'Pawn':
        if piece.colour == 'White':
            w_pawns.remove(piece)
        else:
            b_pawns.remove(piece)

    else:
        if piece.colour == 'White':
            w_majors.remove(piece)
        else:
            b_majors.remove(piece)


def flip_board():
    for w_pawn in w_pawns:
        w_pawn.set_pos(
            (
                BD_SZ - w_pawn.pos[0] - SQ_SZ,
                BD_SZ - w_pawn.pos[1] - SQ_SZ
            )
        )

    for b_pawn in b_pawns:
        b_pawn.set_pos(
            (
                BD_SZ - b_pawn.pos[0] - SQ_SZ,
                BD_SZ - b_pawn.pos[1] - SQ_SZ
            )
        )

    for w_major in w_majors:
        w_major.set_pos(
            (
                BD_SZ - w_major.pos[0] - SQ_SZ,
                BD_SZ - w_major.pos[1] - SQ_SZ
            )
        )

    for b_major in b_majors:
        b_major.set_pos(
            (
                BD_SZ - b_major.pos[0] - SQ_SZ,
                BD_SZ - b_major.pos[1] - SQ_SZ
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


# def validate_pawn_