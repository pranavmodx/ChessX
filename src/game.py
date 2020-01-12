import pygame
pygame.init()

# Display size
S_WIDTH = 600
S_HEIGHT = 600

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
pygame.display.set_caption('ChessX')

screen.fill(BLACK)

# Images
# Board
chess_board = pygame.image.load('../assets/img/board/chessboard_mod.png')

# White pieces
w_king = pygame.image.load('../assets/img/pieces/w_king.png')
w_queen = pygame.image.load('../assets/img/pieces/w_queen.png')
w_rook = pygame.image.load('../assets/img/pieces/w_rook.png')
w_bishop = pygame.image.load('../assets/img/pieces/w_bishop.png')
w_knight = pygame.image.load('../assets/img/pieces/w_knight.png')
w_pawn = pygame.image.load('../assets/img/pieces/w_pawn.png')

# Black pieces
b_king = pygame.image.load('../assets/img/pieces/b_king.png')
b_queen = pygame.image.load('../assets/img/pieces/b_queen.png')
b_rook = pygame.image.load('../assets/img/pieces/b_rook.png')
b_bishop = pygame.image.load('../assets/img/pieces/b_bishop.png')
b_knight = pygame.image.load('../assets/img/pieces/b_knight.png')
b_pawn = pygame.image.load('../assets/img/pieces/b_pawn.png')


# Board size
BOARD_SIZE = 600

# Square size
SQ_SIZE = BOARD_SIZE / 8

# Board position
board_X = S_WIDTH * 0.0
board_Y = S_HEIGHT * 0.0

# Initial piece position
x_pos = board_X + 5
up_y_pos = board_Y + 5
down_y_pos = up_y_pos + (BOARD_SIZE - SQ_SIZE)

# Game loop
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Display board
    screen.blit(chess_board, (board_X, board_Y))

    # Display black pieces
    screen.blit(b_rook, ((x_pos + (SQ_SIZE * 0), up_y_pos)))
    screen.blit(b_knight, ((x_pos + (SQ_SIZE * 1), up_y_pos)))
    screen.blit(b_bishop, ((x_pos + (SQ_SIZE * 2), up_y_pos)))
    screen.blit(b_queen, ((x_pos + (SQ_SIZE * 3), up_y_pos)))
    screen.blit(b_king, ((x_pos + (SQ_SIZE * 4), up_y_pos)))
    screen.blit(b_bishop, ((x_pos + (SQ_SIZE * 5), up_y_pos)))
    screen.blit(b_knight, ((x_pos + (SQ_SIZE * 6), up_y_pos)))
    screen.blit(b_rook, ((x_pos + (SQ_SIZE * 7), up_y_pos)))

    x_change = x_pos
    for i in range(8):
        screen.blit(b_pawn, (x_change, up_y_pos + SQ_SIZE))
        x_change += SQ_SIZE
    
    # Display white pieces
    screen.blit(w_rook, (x_pos + (SQ_SIZE * 0), down_y_pos))
    screen.blit(w_knight, (x_pos + (SQ_SIZE * 1), down_y_pos))
    screen.blit(w_bishop, (x_pos + (SQ_SIZE * 2), down_y_pos))
    screen.blit(w_queen, (x_pos + (SQ_SIZE * 3), down_y_pos))
    screen.blit(w_king, (x_pos + (SQ_SIZE * 4), down_y_pos))
    screen.blit(w_bishop, (x_pos + (SQ_SIZE * 5), down_y_pos))
    screen.blit(w_knight, (x_pos + (SQ_SIZE * 6), down_y_pos))
    screen.blit(w_rook, (x_pos + (SQ_SIZE * 7), down_y_pos))

    x_change = x_pos
    for i in range(8):
        screen.blit(w_pawn, (x_change, down_y_pos - SQ_SIZE))
        x_change += SQ_SIZE

    pygame.display.flip()



