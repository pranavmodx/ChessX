import colour
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
    turn = 'White'
    is_flipped = False

    while not game_over:
        display_all(screen)

        if clicked_once == True:
            highlight_square(
                screen,
                colour.RED,
                sq_pos1
            )

            for valid_move in valid_moves:
                highlight_square(
                    screen, 
                    colour.GREEN, 
                    valid_move
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

                if piece != None and piece.colour == turn:
                    clicked_once = True
                    print('Piece 1 :', piece)

                    valid_moves = piece.valid_moves(is_flipped)
                else:
                    print('Empty square')

            elif event.type == pygame.MOUSEBUTTONDOWN and clicked_once:
                print('Click 2')
                clicked_once = False

                mouse_pos = pygame.mouse.get_pos()

                sq_pos2 = calc_sq_pos(mouse_pos)
                print('Sq pos 2 :', sq_pos2)

                if sq_pos2 != sq_pos1:
                    if turn == 'White':
                        turn = 'Black'
                    else:
                        turn = 'White'

                    piece2 = fetch_piece(sq_pos2)

                    if piece2 == None:
                        print('Empty square')
                        if sq_pos2 in valid_moves:
                            piece.move(sq_pos2)

                    else:
                        if sq_pos2 in valid_moves:
                            delete_piece(piece2)
                            piece.move(sq_pos2)

                        print('Piece 2 :', piece)
                        # piece2.captured = True 
                        ''' Doesn't quite work because 
                        the one in the list is unaffected'''
                        # For now it's ok, but later preserve state to move back & forth


        pygame.display.flip()


def main():
    init_pygame()

    screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
    screen.fill(colour.BLACK)

    gameplay(screen)

main()