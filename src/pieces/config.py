from board import BD_SZ, SQ_SZ, bd_x, bd_y

# Image path specifications
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


# Initial piece position
x_pos = bd_x + 5
up_y_pos = bd_y + 5
down_y_pos = up_y_pos + (BD_SZ - SQ_SZ)

# Piece image size
p_size = 65
