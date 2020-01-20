import colour
from config import S_WIDTH, S_HEIGHT
from board import SQ_SZ
from utilities import (
    display_all,
    calc_sq_pos,
    fetch_piece_loc,
    delete_piece,
    flip_board,
    highlight_square
)

import pygame


def init_pygame():
    '''For initializing and managing pygame module'''

    pygame.init()
    pygame.display.set_caption('ChessX')


def gameplay(screen):
    '''Main game loop'''

    game_over = False
    clicked_once = False
    turn = 'White'
    is_flipped = False

    while not game_over:
        # Display board and highlight screen
        display_all(screen)

        if clicked_once == True:
            highlight_square(screen, colour.RED, sq_pos1)

            for valid_move in valid_moves:
                highlight_square(screen, colour.GREEN, valid_move)

        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # Click 1
            elif event.type == pygame.MOUSEBUTTONDOWN and not clicked_once:
                mouse_pos = pygame.mouse.get_pos()

                sq_pos1 = calc_sq_pos(mouse_pos)

                idx1, pieces1 = fetch_piece_loc(sq_pos1) 

                if pieces1 and pieces1[idx1].colour == turn:    
                    clicked_once = True

                    if pieces1[idx1].p_type == 'Pawn':
                        valid_moves = pieces1[idx1].valid_moves(is_flipped)
                    # else:
                    #     valid_moves = pieces1[idx1].valid_moves()

            # Click 2
            elif event.type == pygame.MOUSEBUTTONDOWN and clicked_once:
                clicked_once = False

                mouse_pos = pygame.mouse.get_pos()

                sq_pos2 = calc_sq_pos(mouse_pos)

                # If new click pos is not the same as first
                if sq_pos2 != sq_pos1:
                    idx2, pieces2 = fetch_piece_loc(sq_pos2)
                    p_type = pieces1[idx1].p_type

                    dist_x = abs(sq_pos2[0] - sq_pos1[0])
                    dist_y = abs(sq_pos2[1] - sq_pos1[1])
                    print(dist_x)
                    print(dist_y)

                    # If empty square
                    if not pieces2:
                        if p_type == 'Pawn':
                            if dist_x != SQ_SZ and sq_pos2 in valid_moves:
                                if turn == 'White':
                                    turn = 'Black'
                                else:
                                    turn = 'White'
                                pieces1[idx1].move(sq_pos2)

                                if pieces1[idx1].start_pos == True:
                                    pieces1[idx1].start_pos = False

                        else:
                            if sq_pos2 in valid_moves:
                                if turn == 'White':
                                    turn = 'Black'
                                else:
                                    turn = 'White'

                                pieces1[idx1].move(sq_pos2)

                    # If piece present
                    else:
                        if sq_pos2 in valid_moves:
                            pos = pieces2[idx2].pos

                            if turn == 'White':
                                # If there's a piece directly in front of pawn
                                # 1 or 2 squares (2 if at start pos)
                                if p_type == 'Pawn' and (dist_y != SQ_SZ and dist_y != 2 * SQ_SZ and dist_x == 0) or dist_x == SQ_SZ:
                                    pieces2[idx2].captured = True
                                    pieces1[idx1].move(sq_pos2)

                                    turn = 'Black'

                                # else:

                            else:
                                if p_type == 'Pawn' and (dist_y != SQ_SZ and dist_y != 2 * SQ_SZ and dist_x == 0) or dist_x == SQ_SZ:
                                    pieces2[idx2].captured = True
                                    pieces1[idx1].move(sq_pos2)

                                    turn = 'White'
                                
                                # else:


        pygame.display.flip()


def main():
    init_pygame()

    screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
    screen.fill(colour.BLACK)

    gameplay(screen)

main()