import colour
from config import S_WIDTH, S_HEIGHT
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
                print('Click 1')

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
                print('Click 2')

                clicked_once = False

                mouse_pos = pygame.mouse.get_pos()

                sq_pos2 = calc_sq_pos(mouse_pos)

                if sq_pos2 != sq_pos1:
                    idx2, pieces2 = fetch_piece_loc(sq_pos2)

                    if not pieces2:
                        if sq_pos2 in valid_moves:
                            if turn == 'White':
                                turn = 'Black'
                            else:
                                turn = 'White'

                            pieces1[idx1].move(sq_pos2)

                    else:
                        if sq_pos2 in valid_moves:
                            if turn == 'White':
                                turn = 'Black'
                            else:
                                turn = 'White'

                            pieces2[idx2].captured = True

                            pieces1[idx1].move(sq_pos2)


        pygame.display.flip()


def main():
    init_pygame()

    screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
    screen.fill(colour.BLACK)

    gameplay(screen)

main()