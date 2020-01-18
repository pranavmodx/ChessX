import board
from pieces.config import x_pos
from pieces.pieces import (
    w_pawns, b_pawns,
    w_majors, b_majors
)

def display_all(screen):
    '''Display(show) all objects'''

    board.bd_obj.show(screen) 

    x_change = x_pos
    for pawn in w_pawns:
        if not pawn.captured:
            pawn.show(screen) 
        x_change += board.SQ_SZ

    for w_piece in w_majors:
        if not w_piece.captured:
            w_piece.show(screen)

    x_change = x_pos
    for pawn in b_pawns:
        if not pawn.captured:
            pawn.show(screen) 
        x_change += board.SQ_SZ

    for b_piece in b_majors:
        if not b_piece.captured:
            b_piece.show(screen)


def calc_sq_pos(mouse_pos):
    '''Calculates and returns topleft position of the square clicked'''

    coeff_x = int(mouse_pos[0] // board.SQ_SZ)
    coeff_y = int(mouse_pos[1] // board.SQ_SZ)

    return (int(board.SQ_SZ * coeff_x + 5), int(board.SQ_SZ * coeff_y + 5))


def fetch_piece(req_pos):
    '''Fetches piece present at a given position'''

    found = 0

    for w_pawn in w_pawns:
        if w_pawn.pos == req_pos:
            found = 1
            return w_pawn

    if found == 0:
        for w_piece in w_majors:
            if w_piece.pos == req_pos:
                found = 1
                return w_piece

    if found == 0:
        for b_pawn in b_pawns:
            if b_pawn.pos == req_pos:
                found = 1
                return b_pawn

    if found == 0:
        for b_piece in b_majors:
            if b_piece.pos == req_pos:
                found = 1
                return b_piece

    return None


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
