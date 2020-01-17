import colour
from config import *
from utilities import (
    display_all,
    calc_sq_topleft,
    piece_clicked
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

    while not game_over:
        display_all(screen)

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

    screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
    screen.fill(colour.BLACK)

    gameplay(screen)

main()