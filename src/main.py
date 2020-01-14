import window
from board import Board
from pieces import (
    Piece, 
    Pawn, Knight, Bishop, Rook, Queen, King
)

import pygame


def init_pygame():
    '''For initializing and managing pygame module'''

    pygame.init()
    pygame.display.set_caption('ChessX')


# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

window.screen.fill(BLACK)

# Create all objects
board = Board()

# Pieces
w_pawns = []
for i in range(8):
    p = Pawn(i)
    w_pawns.append(p)

b_pawns = []
for i in range(8):
    p = Pawn(i, 'Black')
    b_pawns.append(p)

w_king = King()
w_queen = Queen()
w_rook1 = Rook(1)
w_rook2 = Rook(2)
w_bishop1 = Bishop(1)
w_bishop2 = Bishop(2)
w_knight1 = Knight(1)
w_knight2 = Knight(2)

w_pieces = [w_rook1, w_knight1, w_bishop1, w_queen, 
            w_king, w_bishop2, w_knight2, w_rook2]

b_king = King('Black')
b_queen = Queen('Black')
b_rook1 = Rook(1, 'Black')
b_rook2 = Rook(2, 'Black')
b_bishop1 = Bishop(1, 'Black')
b_bishop2 = Bishop(2, 'Black')
b_knight1 = Knight(1, 'Black')
b_knight2 = Knight(2, 'Black')

b_pieces = [b_rook1, b_knight1, b_bishop1, b_queen, 
            b_king, b_bishop2, b_knight2, b_rook2]


# Board position
board_X = window.S_WIDTH * 0.0
board_Y = window.S_HEIGHT * 0.0

# Board size
BOARD_SIZE = 600

# Square size
SQ_SIZE = BOARD_SIZE / 8

# Initial piece position
x_pos = board_X + 5
up_y_pos = board_Y + 5
down_y_pos = up_y_pos + (BOARD_SIZE - SQ_SIZE)


p_img_rel_path = '../assets/img/pieces/'
b_img_rel_path = '../assets/img/board/'
img_ext = '.png'

def load_all_img():
    '''Load all required images (board, pieces)'''

    board.load_img(b_img_rel_path + 'chessboard_mod' + img_ext)

    for w_pawn in w_pawns:
        w_pawn.load_img(p_img_rel_path + 'w_pawn' + img_ext)
    w_king.load_img(p_img_rel_path + 'w_king' + img_ext)
    w_queen.load_img(p_img_rel_path + 'w_queen' + img_ext)
    w_rook1.load_img(p_img_rel_path + 'w_rook' + img_ext)
    w_rook2.load_img(p_img_rel_path + 'w_rook' + img_ext)
    w_bishop1.load_img(p_img_rel_path + 'w_bishop' + img_ext)
    w_bishop2.load_img(p_img_rel_path + 'w_bishop' + img_ext)
    w_knight1.load_img(p_img_rel_path + 'w_knight' + img_ext)
    w_knight2.load_img(p_img_rel_path + 'w_knight' + img_ext)

    for b_pawn in b_pawns:
        b_pawn.load_img(p_img_rel_path + 'b_pawn' + img_ext)
    b_king.load_img(p_img_rel_path + 'b_king' + img_ext)
    b_queen.load_img(p_img_rel_path + 'b_queen' + img_ext)
    b_rook1.load_img(p_img_rel_path + 'b_rook' + img_ext)
    b_rook2.load_img(p_img_rel_path + 'b_rook' + img_ext)
    b_bishop1.load_img(p_img_rel_path + 'b_bishop' + img_ext)
    b_bishop2.load_img(p_img_rel_path + 'b_bishop' + img_ext)
    b_knight1.load_img(p_img_rel_path + 'b_knight' + img_ext)
    b_knight2.load_img(p_img_rel_path + 'b_knight' + img_ext)


def set_pos_all():
    '''Set position of all objects'''

    board.set_pos((board_X, board_Y))

    x_change = x_pos
    for pawn in w_pawns:
        pawn.set_pos((x_change, down_y_pos - SQ_SIZE)) 
        x_change += SQ_SIZE

    w_rook1.set_pos((x_pos + (SQ_SIZE * 0), down_y_pos))
    w_knight1.set_pos((x_pos + (SQ_SIZE * 1), down_y_pos))
    w_bishop1.set_pos((x_pos + (SQ_SIZE * 2), down_y_pos))
    w_queen.set_pos((x_pos + (SQ_SIZE * 3), down_y_pos))
    w_king.set_pos((x_pos + (SQ_SIZE * 4), down_y_pos))
    w_bishop2.set_pos((x_pos + (SQ_SIZE * 5), down_y_pos))
    w_knight2.set_pos((x_pos + (SQ_SIZE * 6), down_y_pos))
    w_rook2.set_pos((x_pos + (SQ_SIZE * 7), down_y_pos))

    x_change = x_pos
    for pawn in b_pawns:
        pawn.set_pos((x_change, up_y_pos + SQ_SIZE)) 
        x_change += SQ_SIZE

    b_rook1.set_pos((x_pos + (SQ_SIZE * 0), up_y_pos))
    b_knight1.set_pos((x_pos + (SQ_SIZE * 1), up_y_pos))
    b_bishop1.set_pos((x_pos + (SQ_SIZE * 2), up_y_pos))
    b_queen.set_pos((x_pos + (SQ_SIZE * 3), up_y_pos))
    b_king.set_pos((x_pos + (SQ_SIZE * 4), up_y_pos))
    b_bishop2.set_pos((x_pos + (SQ_SIZE * 5), up_y_pos))
    b_knight2.set_pos((x_pos + (SQ_SIZE * 6), up_y_pos))
    b_rook2.set_pos((x_pos + (SQ_SIZE * 7), up_y_pos))


def display_all():
    '''Display(show) all objects'''

    board.show() 

    x_change = x_pos
    for pawn in w_pawns:
        pawn.show() 
        x_change += SQ_SIZE

    for w_piece in w_pieces:
        w_piece.show()

    x_change = x_pos
    for pawn in b_pawns:
        pawn.show() 
        x_change += SQ_SIZE
    
    for b_piece in b_pieces:
        b_piece.show()


def gameplay():
    '''Main game loop'''

    game_over = False
    mouse_pos1 = ()
    mouse_pos2 = ()
    clicked_once = False

    while not game_over:
        display_all()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN and not clicked_once:
                # if piece_present:
                    # clicked_once = True

                # clicked_once = True
                # mouse_pos1 = pygame.mouse.get_pos()
                # print('Click 1', mouse_pos1)
                
                # # Selects right square
                # coeff_x1 = int(mouse_pos1[0] // SQ_SIZE)
                # coeff_y1 = int(mouse_pos1[1] // SQ_SIZE)

                # board.highlight_square(window.screen, RED, 
                #                         (SQ_SIZE * coeff_x1, SQ_SIZE * coeff_y1, SQ_SIZE, SQ_SIZE))

            elif event.type == pygame.MOUSEBUTTONDOWN and clicked_once:
                # clicked_once = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # mouse_pos2 = pygame.mouse.get_pos()
                    # print('Click 2', mouse_pos2)

                    # coeff_x2 = int(mouse_pos2[0] // SQ_SIZE)
                    # coeff_y2 = int(mouse_pos2[1] // SQ_SIZE)

                    # idx = int(mouse_pos1[0] // SQ_SIZE)
                    # piece = w_pieces[idx]
                    # print('Old', piece.pos, piece.c_pos)
                    # piece.move((coeff_y1, coeff_y2))
                    # print('New', piece.pos, piece.c_pos)

                    # board.highlight_square(window.screen, RED, 
                    #                         (SQ_SIZE * coeff_x2, SQ_SIZE * coeff_y2, SQ_SIZE, SQ_SIZE))
    
        pygame.display.flip()


def main():
    init_pygame()

    load_all_img()
    set_pos_all()

    gameplay()

main()