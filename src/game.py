import colour
from board import bd_obj
from config import S_WIDTH, S_HEIGHT
from utilities import (
    display_all,
    calc_sq_pos,
    fetch_piece,
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

    while not game_over:
        display_all(screen)

        if clicked_once == True:
                highlight_square(
                    screen,
                    colour.RED,
                    (sq_pos1[0] - 5, sq_pos1[1] - 5)
                )

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN and not clicked_once:
                # flip_board()
                print('Click 1')

                mouse_pos1 = pygame.mouse.get_pos()

                sq_pos1 = calc_sq_pos(mouse_pos1)
                print('Sq pos 1 :', sq_pos1)

                piece = fetch_piece(sq_pos1)

                if piece != None:
                    clicked_once = True
                    print('Piece 1 :', piece)
                else:
                    print('Empty square')

            elif event.type == pygame.MOUSEBUTTONDOWN and clicked_once:
                print('Click 2')
                clicked_once = False

                mouse_pos = pygame.mouse.get_pos()

                sq_pos2 = calc_sq_pos(mouse_pos)
                print('Sq pos 2 :', sq_pos2)

                if sq_pos2 != sq_pos1:
                    piece2 = fetch_piece(sq_pos2)

                    if piece2 == None:
                        print('Empty square')
                        # if new_sq_tl in piece.valid_moves():
                        piece.move(sq_pos2)
                    else:
                        print('Piece 2 :', piece)
                        piece2.captured = True
                        delete_piece(piece2)
                        piece.move(sq_pos2)


        pygame.display.flip()


def main():
    init_pygame()

    screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
    screen.fill(colour.BLACK)

    gameplay(screen)

main()