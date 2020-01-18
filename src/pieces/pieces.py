from board import BD_SZ, SQ_SZ
from .config import *

from .pawn import Pawn
from .knight import Knight
from .bishop import Bishop
from .rook import Rook
from .queen import Queen
from .king import King

import pygame


w_pawns = []
for i in range(8):
    p = Pawn(i + 1)
    w_pawns.append(p)

b_pawns = []
for i in range(8):
    p = Pawn(i + 1, 'Black')
    b_pawns.append(p)

w_majors = [
    Rook(1),
    Knight(1),
    Bishop(1),
    Queen(),
    King(),
    Bishop(2),
    Knight(2),
    Rook(2),
]

b_majors = [
    Rook(1, 'Black'),
    Knight(1, 'Black'),
    Bishop(1, 'Black'),
    Queen('Black'),
    King('Black'),
    Bishop(2, 'Black'),
    Knight(2, 'Black'),
    Rook(2, 'Black'),
]


def load_all_img():
    '''Load all images of pieces'''

    for w_pawn in w_pawns:
        img_obj = pygame.image.load(
            pieces_rel_path + 'w_pawn' + img_ext
        )
        w_pawn.set_img(img_obj)

    for i, w_piece in enumerate(w_majors):
        img_obj = pygame.image.load(
            pieces_rel_path + 'w_' + img_names[i] + img_ext
        )
        w_piece.set_img(img_obj)

    for b_pawn in b_pawns:
        img_obj = pygame.image.load(
            pieces_rel_path + 'b_pawn' + img_ext
        )
        b_pawn.set_img(img_obj)

    for i, b_piece in enumerate(b_majors):
        img_obj = pygame.image.load(
            pieces_rel_path + 'b_' + img_names[i] + img_ext
        )
        b_piece.set_img(img_obj)


def set_pos_all():
    '''Set position of all objects'''

    x_change = x_pos
    for pawn in w_pawns:
        pawn.set_pos((x_change, down_y_pos - SQ_SZ)) 
        x_change += SQ_SZ

    for i, w_piece in enumerate(w_majors):
        w_piece.set_pos((x_pos + (SQ_SZ * i), down_y_pos))

    x_change = x_pos
    for pawn in b_pawns:
        pawn.set_pos((x_change, up_y_pos + SQ_SZ)) 
        x_change += SQ_SZ

    for i, b_piece in enumerate(b_majors):
        b_piece.set_pos((x_pos + (SQ_SZ * i), up_y_pos))


def main():
    load_all_img()
    set_pos_all()

main()