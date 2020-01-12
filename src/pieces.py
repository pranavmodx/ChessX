from window import *
import pygame


class Piece:
    # def __init__(self, pos=None, img_path=None):
    #     if img_path != None:
    #         self.img = pygame.image.load(img_path)
    #     self.pos = pos

    def load_img(self, img_path):
        self.img = pygame.image.load(img_path)

    def show(self):
        screen_obj = screen.blit(self.img, (self.pos[0], self.pos[1]))

    def set_pos(self, pos):
        screen_obj = screen.blit(self.img, (pos[0], pos[1]))
        self.pos = pos

    def update_pos(self, pos):
        self.pos = pos


class Pawn(Piece):
    pass


class Knight(Piece):
    pass


class Bishop(Piece):
    pass


class Rook(Piece):
    pass


class Queen(Piece):
    pass


class King(Piece):
    pass