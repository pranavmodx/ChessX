from window import *
from board import Board
from pieces import (
    Piece, 
    Pawn, Knight, Bishop, Rook, Queen, King
)

import pygame

def init_pygame():
    pygame.init()
    pygame.display.set_caption('ChessX')

init_pygame()


# Create and load board object
chess_board = Board()
chess_board.load_img('../assets/img/board/chessboard_mod.png')

# Set board position
board_X = S_WIDTH * 0.0
board_Y = S_HEIGHT * 0.0
chess_board.set_pos((board_X, board_Y))

# Board size
BOARD_SIZE = chess_board.size

# Square size
SQ_SIZE = BOARD_SIZE / 8

# Initial piece position
x_pos = board_X + 5
up_y_pos = board_Y + 5
down_y_pos = up_y_pos + (BOARD_SIZE - SQ_SIZE)

# Create and load piece objects
# White pawns
w_pawns_list = []
for i in range(8):
    p = Pawn()
    p.load_img('../assets/img/pieces/w_pawn.png')
    w_pawns_list.append(p)

# White major pieces
w_king = King()
w_king.load_img('../assets/img/pieces/w_king.png')

w_queen = Queen()
w_queen.load_img('../assets/img/pieces/w_queen.png')

w_rook1 = Rook()
w_rook1.load_img('../assets/img/pieces/w_rook.png')
w_rook2 = Rook()
w_rook2.load_img('../assets/img/pieces/w_rook.png')

w_bishop1 = Bishop()
w_bishop1.load_img('../assets/img/pieces/w_bishop.png')
w_bishop2 = Bishop()
w_bishop2.load_img('../assets/img/pieces/w_bishop.png')

w_knight1 = Knight()
w_knight1.load_img('../assets/img/pieces/w_knight.png')
w_knight2 = Knight()
w_knight2.load_img('../assets/img/pieces/w_knight.png')

w_pieces_list = [w_rook1, w_knight1, w_bishop1, w_queen, 
                w_king, w_bishop2, w_knight2, w_rook2]

# Black pawns
b_pawns_list = []
for i in range(8):
    p = Pawn('Black')
    p.load_img('../assets/img/pieces/b_pawn.png')
    b_pawns_list.append(p)

# Black major pieces
b_king = King('Black')
b_king.load_img('../assets/img/pieces/b_king.png')

b_queen = Queen('Black')
b_queen.load_img('../assets/img/pieces/b_queen.png')

b_rook1 = Rook('Black')
b_rook1.load_img('../assets/img/pieces/b_rook.png')
b_rook2 = Rook('Black')
b_rook2.load_img('../assets/img/pieces/b_rook.png')

b_bishop1 = Bishop('Black')
b_bishop1.load_img('../assets/img/pieces/b_bishop.png')
b_bishop2 = Bishop('Black')
b_bishop2.load_img('../assets/img/pieces/b_bishop.png')

b_knight1 = Knight('Black')
b_knight1.load_img('../assets/img/pieces/b_knight.png')
b_knight2 = Knight('Black')
b_knight2.load_img('../assets/img/pieces/b_knight.png')

b_pieces_list = [b_rook1, b_knight1, b_bishop1, b_queen, 
                b_king, b_bishop2, b_knight2, b_rook2]


# Set position of pieces
# White
x_change = x_pos
for pawn in w_pawns_list:
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

# Black
x_change = x_pos
for pawn in b_pawns_list:
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


# Game loop
def gameplay():
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                idx = int(mouse_pos[0] // SQ_SIZE)
                # print(idx)

                pawn = w_pawns_list[idx]
                # print(f'mouse_pos : {mouse_pos}, pos : {pawn.pos} center_pos : {pawn.center_pos}')
                if abs(mouse_pos[0] - pawn.center_pos[0]) < 32 and \
                    abs(mouse_pos[1] - pawn.center_pos[1]) < 32:
                    pawn.update_pos((pawn.pos[0], pawn.pos[1] - 75), 
                                    (pawn.center_pos[0], pawn.center_pos[1] - 75))
                    # print(f'update_pos : {pawn.pos}, update_center_pos : {pawn.center_pos}')

                pawn = b_pawns_list[idx]
                if abs(mouse_pos[0] - pawn.center_pos[0]) < 32 and \
                    abs(mouse_pos[1] - pawn.center_pos[1]) < 32:
                    pawn.update_pos((pawn.pos[0], pawn.pos[1] + 75), 
                                    (pawn.center_pos[0], pawn.center_pos[1] + 75))

                piece = w_pieces_list[idx]
                if abs(mouse_pos[0] - piece.center_pos[0]) < 32 and \
                    abs(mouse_pos[1] - piece.center_pos[1]) < 32:
                    piece.update_pos((piece.pos[0], piece.pos[1] - 150), 
                                    (piece.center_pos[0], piece.center_pos[1] - 150))

                piece = b_pieces_list[idx]
                if abs(mouse_pos[0] - piece.center_pos[0]) < 32 and \
                    abs(mouse_pos[1] - piece.center_pos[1]) < 32:
                    piece.update_pos((piece.pos[0], piece.pos[1] + 150), 
                                    (piece.center_pos[0], piece.center_pos[1] + 150))
                
        # Display board 
        chess_board.show() 
        # chess_board.highlight_square(screen, RED, (75*3, 75*3, 75, 75))

        # Display white pieces
        x_change = x_pos
        for pawn in w_pawns_list:
            pawn.show() 
            x_change += SQ_SIZE

        w_rook1.show()
        w_bishop1.show()
        w_knight1.show()
        w_queen.show()
        w_king.show()
        w_bishop2.show()
        w_knight2.show()
        w_rook2.show()

        # Display Black pieces
        x_change = x_pos
        for pawn in b_pawns_list:
            pawn.show() 
            x_change += SQ_SIZE
        
        b_rook1.show()
        b_bishop1.show()
        b_knight1.show()
        b_queen.show()
        b_king.show()
        b_bishop2.show()
        b_knight2.show()
        b_rook2.show()


        pygame.display.flip()


gameplay()