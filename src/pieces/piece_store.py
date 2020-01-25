from board import BD_SZ, SQ_SZ, bd_x, bd_y
from .config import *

from .pawn import Pawn
from .knight import Knight
from .bishop import Bishop
from .rook import Rook
from .queen import Queen
from .king import King

import pygame


piece_store = {
    'w_pawns': [Pawn(i + 1) for i in range(8)],
    'b_pawns': [Pawn(i + 1, 'Black') for i in range(8)],
    'w_pieces': [
                    Rook(1),
                    Knight(1),
                    Bishop(1),
                    Queen(),
                    King(),
                    Bishop(2),
                    Knight(2),
                    Rook(2),
                ],
    'b_pieces': [
                    Rook(1, 'Black'),
                    Knight(1, 'Black'),
                    Bishop(1, 'Black'),
                    Queen(colour='Black'),
                    King(colour='Black'),
                    Bishop(2, 'Black'),
                    Knight(2, 'Black'),
                    Rook(2, 'Black'),
                ]
}


def load_all_img():
    '''Load all images of pieces'''

    for w_pawn in piece_store['w_pawns']:
        img_obj = pygame.image.load(
            pieces_rel_path + 'w_pawn' + img_ext
        )
        w_pawn.set_img(img_obj)

    for i, w_piece in enumerate(piece_store['w_pieces']):
        img_obj = pygame.image.load(
            pieces_rel_path + 'w_' + img_names[i] + img_ext
        )
        w_piece.set_img(img_obj)

    for b_pawn in piece_store['b_pawns']:
        img_obj = pygame.image.load(
            pieces_rel_path + 'b_pawn' + img_ext
        )
        b_pawn.set_img(img_obj)

    for i, b_piece in enumerate(piece_store['b_pieces']):
        img_obj = pygame.image.load(
            pieces_rel_path + 'b_' + img_names[i] + img_ext
        )
        b_piece.set_img(img_obj)


def set_pos_all():
    '''Set position of all objects'''

    x_change = 0
    for pawn in piece_store['w_pawns']:
        pawn.set_pos((bd_x + x_change, bd_y + BD_SZ - 2 * SQ_SZ)) 
        x_change += SQ_SZ

    for i, w_piece in enumerate(piece_store['w_pieces']):
        w_piece.set_pos((bd_x + SQ_SZ * i, bd_y + BD_SZ - SQ_SZ))

    x_change = 0
    for pawn in piece_store['b_pawns']:
        pawn.set_pos((bd_x + x_change, bd_y + SQ_SZ)) 
        x_change += SQ_SZ

    for i, b_piece in enumerate(piece_store['b_pieces']):
        b_piece.set_pos((bd_x + SQ_SZ * i, bd_y))


def main():
    load_all_img()
    set_pos_all()

main()