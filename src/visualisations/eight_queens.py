from board import Board
from pieces import Queen
from config import *

import pygame


class EightQueens():
    def __init__(self, screen):
        self.screen = screen
        self.init_board()

    def init_board(self):
        self.board = Board((BD_X, BD_Y))
        board_img_obj = pygame.image.load(
            '/Users/pranavmodx/Dev/gh_projects/ChessX/assets/img/board/board.png'
        )
        self.board.load_img(board_img_obj)

        self.queen = Queen()
        self.queen.pos = (0, 0)
        queen_img_obj = pygame.image.load(
            '/Users/pranavmodx/Dev/gh_projects/ChessX/assets/img/pieces/w_queen.png'
        )
        self.queen.load_img(queen_img_obj)