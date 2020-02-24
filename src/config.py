# Image path specifications
board_rel_path = '../assets/img/board/'
flip_board_rel_path = '../assets/img/icons/'
reset_board_rel_path = '../assets/img/icons/'
pieces_rel_path = '../assets/img/pieces/'

img_names = [
    'rook',
    'knight',
    'bishop',
    'queen', 
    'king', 
    'bishop',  
    'knight',
    'rook', 
]
img_ext = '.png'

# Screen size
S_WIDTH = 600
S_HEIGHT = 600

# Board position (relative to screen)
BD_X = S_WIDTH * 0
BD_Y = S_HEIGHT * 0

# Board size
BD_SZ = 600
SQ_SZ = BD_SZ / 8

# Main colours
Colour = {
    'BLACK' : (0, 0, 0),
    'WHITE' : (255, 255, 255),
    'RED' : (255, 0, 0),
    'GREEN' : (0, 255, 0),
    'BLUE' : (0, 0, 255),
}
