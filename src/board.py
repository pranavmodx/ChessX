from config import *
from pieces import (
    Pawn,
    Bishop,
    Knight,
    Rook,
    Queen,
    King,
)
import pygame

class Board:
    def __init__(self, pos):
        # Board attributes
        self.pos = pos
        self.is_flipped = False
        self.init_notation_params()
        self.set_notation()

        self.init_all_pieces()

        # Move params
        self.turn = 'White'
        self.valid_moves = []
        self.king_pos = {
            'White': None,
            'Black': None,
        }
        self.under_check = False

    def init_all_pieces(self):
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

    def init_notation_params(self):
        self.coords = [
            (x,y) 
            for x in range(0,BD_SZ,SQ_SZ) 
            for y in range(BD_SZ - SQ_SZ, -SQ_SZ, -SQ_SZ)
        ]
        self.files = [chr(x) for x in range(97,105)]
        self.ranks = list(range(1,9))
        self.notations = [
            f'{fil}{rank}' 
            for rank in self.ranks 
            for fil in self.files
        ]

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
                if not piece.captured:
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

    def set_next_turn(self):
        '''Switches the turn to next player'''
        if self.turn == 'White':
            self.turn = 'Black'
        else:
            self.turn = 'White'

    def get_next_turn(self):
        '''Returns the next turn'''
        if self.turn == 'White':
            return 'Black'
        else:
            return 'White'

    def set_notation(self):
        self.annotations = {
            key:value for (key,value) in 
            zip(sorted(
                    sorted(
                        self.notations, key=lambda x: x[1], reverse=self.is_flipped), 
                        key=lambda x: x[0], 
                        reverse=self.is_flipped
                    ),
                self.coords
            )
        }
        
    def get_notation(self, req_coord):
        for notation, coord in self.annotations.items():
            if coord == req_coord:
                return notation

    def flip_board(self):
        '''Flips the board and the pieces'''

        self.is_flipped = not self.is_flipped
        print(self.is_flipped)

        # Update position of all pieces
        for pieces in self.pieces.values():
            for piece in pieces:
                piece.set_pos(
                    (
                        self.BD_SZ - piece.pos[0] - self.SQ_SZ,
                        self.BD_SZ - piece.pos[1] - self.SQ_SZ
                    )
                )

        # Update king_pos
        self.king_pos['White'] = self.pieces['w_pieces'][4].pos
        self.king_pos['Black'] = self.pieces['b_pieces'][4].pos

        # Update notations
        self.set_notation()

    def calc_sq_pos(self, mouse_pos):
        '''Calculates and returns topleft position of the square clicked'''
        
        coeff_x = mouse_pos[0] // self.SQ_SZ
        coeff_y = mouse_pos[1] // self.SQ_SZ

        return (self.SQ_SZ * coeff_x, self.SQ_SZ * coeff_y)

    @staticmethod
    def calc_sq_dist(sq1_pos, sq2_pos):
        return (
            sq2_pos[0] - sq1_pos[0],
            sq2_pos[1] - sq1_pos[1],
        )

    def highlight_square(self, surface, color, rect_dim, width=3):
        '''Highlights a particular square with a specified colour'''

        r_left, r_top = rect_dim
        r_width = self.SQ_SZ
        r_height = self.SQ_SZ

        pygame.draw.rect(
            surface,
            color,
            pygame.Rect(r_left, r_top, r_width, r_height),
            width
        )

    def fetch_piece_by_turn(self, req_pos, turn):
        '''Fetches piece (by turn) present at a given position on the board'''

        if turn == 'White':
            for w_pawn in self.pieces['w_pawns']:
                if w_pawn.pos == req_pos and not w_pawn.captured:
                    return w_pawn

            for w_piece in self.pieces['w_pieces']:
                if w_piece.pos == req_pos and not w_piece.captured:
                    return w_piece

        else:
            for b_pawn in self.pieces['b_pawns']:
                if b_pawn.pos == req_pos and not b_pawn.captured:
                    return b_pawn

            for b_piece in self.pieces['b_pieces']:
                if b_piece.pos == req_pos and not b_piece.captured:
                    return b_piece

        return None

    def fetch_piece(self, req_pos):
        '''Fetches piece present at a given position on the board'''
        
        for pieces in self.pieces.values():
            for piece in pieces:
                if piece.pos == req_pos and not piece.captured:
                    return piece

        return None

    def delete_piece(self, turn, piece):
        '''Deletes a given piece from the list of pieces'''

        if turn == 'Black':
            if type(piece).__name__ == 'Pawn':
                self.pieces['w_pawns'].remove(piece)
            else:
                self.pieces['w_pieces'].remove(piece)

        else:
            if type(piece).__name__ == 'Pawn':
                self.pieces['b_pawns'].remove(piece)
            else:
                self.pieces['b_pieces'].remove(piece)

    def is_controlled_sq(self, req_pos, turn):
        '''Checks whether a square is controlled by a piece'''

        # Along knight routes (L)
        knight = Knight(0)
        knight.set_pos(req_pos)
        for move in knight.valid_moves():
            piece = self.fetch_piece(move)
            if piece and type(piece).__name__ == 'Knight' and piece.colour != turn:
                del knight
                return True

        # Along diagonals
        bishop = Bishop(0)
        bishop.set_pos(req_pos)
        for move in bishop.valid_moves():
            piece = self.fetch_piece(move)
            dist_x = move[0] - req_pos[0]
            dist_y = move[1] - req_pos[1]

            if piece and (type(piece).__name__ == 'Bishop' or \
                type(piece).__name__ == 'Queen') and \
                piece.colour != turn and \
                not piece.move_through(self, req_pos, dist_x, dist_y):
                del bishop
                return True

        # Along ranks and files
        rook = Rook(0)
        rook.set_pos(req_pos)
        for move in rook.valid_moves():
            piece = self.fetch_piece(move)
            dist_x = move[0] - req_pos[0]
            dist_y = move[1] - req_pos[1]

            if piece and (type(piece).__name__ == 'Rook' or \
                type(piece).__name__ == 'Queen') and \
                piece.colour != turn and \
                not piece.move_through(self, req_pos, dist_x, dist_y):
                del rook
                return True

        # King opposition
        king = King()
        king.set_pos(req_pos)
        for move in king.valid_moves():
            piece = self.fetch_piece(move)
            if piece and type(piece).__name__ == 'King' and piece.colour != turn:
                del king
                return True

        # Pawns
        if turn == 'White':
            pawn = Pawn()
        else:
            pawn = Pawn(colour='Black')
        pawn.set_pos(req_pos)
        for move in pawn.valid_moves(self.is_flipped):
            # If directly in front/back
            if move[0] - req_pos[0] == 0:
                continue
            piece = self.fetch_piece(move)
            if piece and type(piece).__name__ == 'Pawn' and piece.colour != turn:
                del pawn
                return True

        return False

