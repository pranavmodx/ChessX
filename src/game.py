import colour
from config import S_WIDTH, S_HEIGHT
from board import SQ_SZ
from utilities import (
    display_all,
    calc_sq_pos,
    highlight_square,
    flip_board,
    fetch_piece,
    handle_pawn_move,
    handle_bishop_move,
    handle_knight_move,
    handle_rook_move,
    handle_queen_move,
    handle_king_move,
)

import pygame


def init_pygame():
    '''For initializing and managing pygame module'''

    pygame.init()
    pygame.display.set_caption('ChessX')


def gameplay(screen):
    '''Main game loop'''

    game_over = False
    is_flipped = False
    clicked_once = False
    turn = 'White'
    valid_moves = []

    while not game_over:
        # Display board and highlight screen
        display_all(screen)

        if clicked_once == True:
            highlight_square(screen, colour.RED, sq1_pos)

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

                sq1_pos = calc_sq_pos(mouse_pos)

                key1, idx1, piece1 = fetch_piece(sq1_pos)

                if piece1 and piece1.colour == turn:
                    clicked_once = True

                    if piece1.p_type == 'Pawn':
                        valid_moves = piece1.valid_moves(is_flipped)
                    else:
                        valid_moves = piece1.valid_moves()

            # Click 2
            elif event.type == pygame.MOUSEBUTTONDOWN and clicked_once:
                clicked_once = False

                mouse_pos = pygame.mouse.get_pos()
                sq2_pos = calc_sq_pos(mouse_pos)

                # If second click is not the same as first, move the piece
                if sq2_pos != sq1_pos:
                    if piece1.p_type == 'Pawn':
                        turn = handle_pawn_move(sq1_pos, sq2_pos, valid_moves, turn)

                    elif piece1.p_type == 'Bishop':
                        turn = handle_bishop_move(sq1_pos, sq2_pos, valid_moves, turn)

                    elif piece1.p_type == 'Knight':
                        turn = handle_knight_move(sq1_pos, sq2_pos, valid_moves, turn)

                    elif piece1.p_type == 'Rook':
                        turn = handle_rook_move(sq1_pos, sq2_pos, valid_moves, turn)

                    elif piece1.p_type == 'Queen':
                        turn = handle_queen_move(sq1_pos, sq2_pos, valid_moves, turn)

                    elif piece1.p_type == 'King':
                        turn = handle_king_move(sq1_pos, sq2_pos, valid_moves, turn)

        pygame.display.flip()


def main():
    init_pygame()

    screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT + SQ_SZ))
    screen.fill(colour.BLACK)

    gameplay(screen)

main()