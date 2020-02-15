from config import *
from pieces import (
    Pawn,
    Bishop,
    Knight,
    Rook,
    Queen,
    King
)
import pygame


class Board:
    def __init__(self, pos):
        # Board attributes
        self.pos = pos
        self.is_flipped = False
        self.king_pos = {
            'White': None,
            'Black': None,
        }

        # Piece attributes
        self.pieces = {
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

    def load_img(self, img):
        '''Loads the board image'''
        
        self.img = img
        self.BD_SZ = self.img.get_height()
        self.SQ_SZ = self.BD_SZ / 8

    def load_all_img(self):
        '''Loads the images of board and all the pieces'''

        board_img_obj = pygame.image.load(board_rel_path + 'board' + img_ext)
        self.load_img(board_img_obj)

        for w_pawn in self.pieces['w_pawns']:
            img_obj = pygame.image.load(
                pieces_rel_path + 'w_pawn' + img_ext
            )
            w_pawn.load_img(img_obj)

        for i, w_piece in enumerate(self.pieces['w_pieces']):
            img_obj = pygame.image.load(
                pieces_rel_path + 'w_' + img_names[i] + img_ext
            )
            w_piece.load_img(img_obj)

        for b_pawn in self.pieces['b_pawns']:
            img_obj = pygame.image.load(
                pieces_rel_path + 'b_pawn' + img_ext
            )
            b_pawn.load_img(img_obj)

        for i, b_piece in enumerate(self.pieces['b_pieces']):
            img_obj = pygame.image.load(
                pieces_rel_path + 'b_' + img_names[i] + img_ext
            )
            b_piece.load_img(img_obj)

    def display_all(self, screen):
        '''Displays the board and all the pieces'''

        bd_scrn_obj = screen.blit(self.img, self.pos)

        for piece_list in self.pieces.values():
            for piece in piece_list:
                # if not piece.captured:
                piece.display(screen)

    def set_pos(self, pos):
        '''Sets or changes the position of board'''
        self.pos = pos

    def set_pos_all(self):
        '''Sets the position of all the pieces'''
        
        x_change = 0
        for pawn in self.pieces['w_pawns']:
            pawn.set_pos((BD_X + x_change, BD_Y + self.BD_SZ - 2 * self.SQ_SZ)) 
            x_change += self.SQ_SZ

        for i, w_piece in enumerate(self.pieces['w_pieces']):
            w_piece.set_pos((BD_X + self.SQ_SZ * i, BD_Y + self.BD_SZ - self.SQ_SZ))

        x_change = 0
        for pawn in self.pieces['b_pawns']:
            pawn.set_pos((BD_X + x_change, BD_Y + self.SQ_SZ)) 
            x_change += self.SQ_SZ

        for i, b_piece in enumerate(self.pieces['b_pieces']):
            b_piece.set_pos((BD_X + self.SQ_SZ * i, BD_Y))

        self.king_pos['White'] = self.pieces['w_pieces'][4].pos
        self.king_pos['Black'] = self.pieces['b_pieces'][4].pos

    def flip_board(self):
        '''Flips the board and the pieces'''
        
        for w_pawn in self.pieces['w_pawns']:
            w_pawn.set_pos(
                (
                    self.BD_SZ - w_pawn.pos[0] - self.SQ_SZ,
                    self.BD_SZ - w_pawn.pos[1] - self.SQ_SZ
                )
            )

        for b_pawn in self.pieces['b_pawns']:
            b_pawn.set_pos(
                (
                    self.BD_SZ - b_pawn.pos[0] - self.SQ_SZ,
                    self.BD_SZ - b_pawn.pos[1] - self.SQ_SZ
                )
            )

        for w_piece in self.pieces['w_pieces']:
            w_piece.set_pos(
                (
                    self.BD_SZ - w_piece.pos[0] - self.SQ_SZ,
                    self.BD_SZ - w_piece.pos[1] - self.SQ_SZ
                )
            )

        for b_piece in self.pieces['b_pieces']:
            b_piece.set_pos(
                (
                    self.BD_SZ - b_piece.pos[0] - self.SQ_SZ,
                    self.BD_SZ - b_piece.pos[1] - self.SQ_SZ
                )
            )


    def calc_sq_pos(self, mouse_pos):
        '''Calculates and returns topleft position of the square clicked'''
        
        coeff_x = mouse_pos[0] // self.SQ_SZ
        coeff_y = mouse_pos[1] // self.SQ_SZ

        return (self.SQ_SZ * coeff_x, self.SQ_SZ * coeff_y)


    def highlight_square(self, surface, color, rect_dim, width=3):
        '''Highlights a particular square'''

        r_left, r_top = rect_dim
        r_width = self.SQ_SZ
        r_height = self.SQ_SZ

        pygame.draw.rect(
            surface,
            color,
            pygame.Rect(r_left, r_top, r_width, r_height),
            width
        )

    def fetch_piece_by_turn(self, turn, req_pos):
        '''Fetches piece (by turn) present at a given position on the board'''

        if turn == 'White':
            for w_pawn in self.pieces['w_pawns']:
                if w_pawn.pos == req_pos:
                    return w_pawn

            for w_piece in self.pieces['w_pieces']:
                if w_piece.pos == req_pos:
                    return w_piece

        else:
            for b_pawn in self.pieces['b_pawns']:
                if b_pawn.pos == req_pos:
                    return b_pawn

            for b_piece in self.pieces['b_pieces']:
                if b_piece.pos == req_pos:
                    return b_piece

        return None

    def fetch_piece(self, req_pos):
        '''Fetches piece present at a given position on the board'''
        
        for pieces in self.pieces.values():
            for piece in pieces:
                if piece.pos == req_pos:
                    return piece

        return None

    def delete_piece(self, turn, piece):
        '''Deletes a given piece from the list of pieces'''

        if turn == 'Black':
            if piece.p_type == 'Pawn':
                self.pieces['w_pawns'].remove(piece)
            else:
                self.pieces['w_pieces'].remove(piece)

        else:
            if piece.p_type == 'Pawn':
                self.pieces['b_pawns'].remove(piece)
            else:
                self.pieces['b_pieces'].remove(piece)

