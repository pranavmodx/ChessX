import colour
from config import S_WIDTH, S_HEIGHT
from board import SQ_SZ
from pieces.piece_store import piece_store
from utilities import (
    display_all,
    calc_sq_pos,
    fetch_piece_loc,
    delete_piece,
    flip_board,
    highlight_square, 
    next_turn
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

                key1, idx1 = fetch_piece_loc(sq1_pos)

                if key1 and piece_store[key1][idx1].colour == turn:
                    clicked_once = True

                    piece1_type = piece_store[key1][idx1].p_type

                    if piece1_type == 'Pawn':
                        valid_moves = piece_store[key1][idx1].valid_moves(is_flipped)
                    else:
                        valid_moves = piece_store[key1][idx1].valid_moves()

            # Click 2
            elif event.type == pygame.MOUSEBUTTONDOWN and clicked_once:
                clicked_once = False

                mouse_pos = pygame.mouse.get_pos()

                sq2_pos = calc_sq_pos(mouse_pos)

                # If second click is not the same as first, move the piece
                if sq2_pos != sq1_pos:
                    key2, idx2 = fetch_piece_loc(sq2_pos)

                    dist_x = sq2_pos[0] - sq1_pos[0]
                    dist_y = sq2_pos[1] - sq1_pos[1]

                    # If piece not present (empty square)
                    if not key2:
                        if piece1_type == 'Pawn':
                            if dist_x == 0 and sq2_pos in valid_moves:
                                piece_store[key1][idx1].move(sq2_pos)
                                if piece_store[key1][idx1].start_pos == True:
                                    piece_store[key1][idx1].start_pos = False

                                turn = next_turn(turn)

                        elif piece1_type == 'King':
                            if sq2_pos in valid_moves:
                                piece_store[key1][idx1].move(sq2_pos)
                                piece_store[key1][idx1].start_pos = False

                                # Checking for castling
                                if abs(dist_x) == 2 * SQ_SZ:
                                    rook1 = piece_store[key1][0]
                                    rook2 = piece_store[key1][-1]

                                    # Short castling
                                    if sq1_pos[0] < sq2_pos[0] and rook2.start_pos:
                                        rook2.move((rook2.pos[0] - 2 * SQ_SZ, rook2.pos[1]))
                                        rook2.start_pos = False
                                    # Long castling
                                    elif sq1_pos[0] > sq2_pos[0] and rook1.start_pos:
                                        rook1.move((rook1.pos[0] + 3 * SQ_SZ, rook1.pos[1]))
                                        rook1.start_pos = False

                                turn = next_turn(turn)

                        # For all other pieces
                        else:
                            if sq2_pos in valid_moves:
                                piece_store[key1][idx1].move(sq2_pos)

                                if piece1_type == 'Rook' and piece_store[key1][idx1].start_pos:
                                    piece_store[key1][idx1].start_pos = False

                                turn = next_turn(turn)

                    # If piece present
                    else:
                        if sq2_pos in valid_moves:
                            # If there's a piece directly in front of pawn
                            # 1 or 2 squares (2 if at start pos)
                            if piece1_type == 'Pawn':
                                if (abs(dist_y) != SQ_SZ and abs(dist_y) != 2 * SQ_SZ) or abs(dist_x) == SQ_SZ:
                                    if piece_store[key1][idx1].colour != piece_store[key2][idx2].colour:
                                        # pieces2[idx2].captured = True
                                        del piece_store[key2][idx2]

                                        piece_store[key1][idx1].move(sq2_pos)
                                        if piece_store[key1][idx1].start_pos == True:
                                            piece_store[key1][idx1].start_pos = False

                                        turn = next_turn(turn)

                            # For all other pieces
                            else:
                                if piece_store[key1][idx1].colour != piece_store[key2][idx2].colour:
                                    # pieces2[idx2].captured = True
                                    del piece_store[key2][idx2]
                                    piece_store[key1][idx1].move(sq2_pos)

                                    turn = next_turn(turn)


        pygame.display.flip()


def main():
    init_pygame()

    screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
    screen.fill(colour.BLACK)

    gameplay(screen)

main()