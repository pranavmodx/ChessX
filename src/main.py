import window
import board
from pieces import (
    w_pawns, b_pawns,
    w_majors, b_majors
)
import colour
from config import *

import pygame


def init_pygame():
    '''For initializing and managing pygame module'''

    pygame.init()
    pygame.display.set_caption('ChessX')


def load_all_img():
    '''Load all required images (board, pieces)'''

    for w_pawn in w_pawns:
        w_pawn.load_img(pieces_rel_path + 'w_pawn' + img_ext)

    for i, w_piece in enumerate(w_majors):
    	w_piece.load_img(pieces_rel_path + 'w_' + img_names[i] + img_ext)

    for b_pawn in b_pawns:
        b_pawn.load_img(pieces_rel_path + 'b_pawn' + img_ext)

    for i, b_piece in enumerate(b_majors):
    	b_piece.load_img(pieces_rel_path + 'b_' + img_names[i] + img_ext)


def set_pos_all():
    '''Set position of all objects'''

    board.bd_obj.set_pos((board.bd_x, board.bd_y))

    x_change = board.x_pos
    for pawn in w_pawns:
        pawn.set_pos((x_change, board.down_y_pos - board.SQ_SZ)) 
        x_change += board.SQ_SZ

    for i, w_piece in enumerate(w_majors):
    	w_piece.set_pos((board.x_pos + (board.SQ_SZ * i), board.down_y_pos))

    x_change = board.x_pos
    for pawn in b_pawns:
        pawn.set_pos((x_change, board.up_y_pos + board.SQ_SZ)) 
        x_change += board.SQ_SZ

    for i, b_piece in enumerate(b_majors):
    	b_piece.set_pos((board.x_pos + (board.SQ_SZ * i), board.up_y_pos))


def display_all():
    '''Display(show) all objects'''

    board.bd_obj.show() 

    x_change = board.x_pos
    for pawn in w_pawns:
        if not pawn.captured:
            pawn.show() 
        x_change += board.SQ_SZ

    for w_piece in w_majors:
        if not w_piece.captured:
            w_piece.show()

    x_change = board.x_pos
    for pawn in b_pawns:
        if not pawn.captured:
            pawn.show() 
        x_change += board.SQ_SZ

    for b_piece in b_majors:
        if not b_piece.captured:
            b_piece.show()


def calc_sq_topleft(mouse_pos):
    coeff_x = int(mouse_pos[0] // board.SQ_SZ)
    coeff_y = int(mouse_pos[1] // board.SQ_SZ)

    return (int(board.SQ_SZ * coeff_x + 5), int(board.SQ_SZ * coeff_y + 5))


def piece_clicked(req_pos):
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


def gameplay():
    '''Main game loop'''

    game_over = False
    clicked_once = False

    while not game_over:
        display_all()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.MOUSEBUTTONUP and clicked_once:
                pass
                # board.bd_obj.highlight_square(
                #     window.screen, 
                #     colour.RED, 
                #     (sq_topleft[0] - 5, sq_topleft[1] - 5, bd.bd_obj.SQ_SZ, bd.bd_obj.SQ_SZ)
                # )

            elif event.type == pygame.MOUSEBUTTONDOWN and not clicked_once:
                print('Click 1')

                mouse_pos1 = pygame.mouse.get_pos()

                sq_topleft = calc_sq_topleft(mouse_pos1)

                # bd.bd_obj.highlight_square(
                #     window.screen, 
                #     colour.RED, 
                #     (sq_topleft[0] - 5, sq_topleft[1] - 5, bd.bd_obj.SQ_SZ, bd.bd_obj.SQ_SZ)
                # )

                piece = piece_clicked(sq_topleft)

                if piece != None:
                    clicked_once = True
                else:
                    print('Empty square')

            elif event.type == pygame.MOUSEBUTTONDOWN and clicked_once:
                print('Click 2')
                clicked_once = False

                mouse_pos2 = pygame.mouse.get_pos()

                sq_topleft = calc_sq_topleft(mouse_pos2)

                piece2 = piece_clicked(sq_topleft)

                if piece2 == None:
                    new_sq_tl = (sq_topleft[0], sq_topleft[1] - 5)
                    # if new_sq_tl in piece.valid_moves():
                    piece.move(new_sq_tl)
                else:
                    if piece2 != piece:
                        piece2.captured = True
                    piece.move(sq_topleft)
                        
    
        pygame.display.flip()


def main():
    init_pygame()

    load_all_img()
    set_pos_all()

    gameplay()

main()