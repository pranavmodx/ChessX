from window import *
import pygame


class Piece:
    def __init__(self, colour='White', captured=False):
        self.colour = colour
        self.captured = captured

    def load_img(self, img_path):
        self.img = pygame.image.load(img_path)

    def show(self):
        screen_obj = screen.blit(self.img, (self.pos[0], self.pos[1]))

    def set_pos(self, pos):
        screen_obj = screen.blit(self.img, (pos[0], pos[1]))
        self.pos = screen_obj.topleft
        self.center_pos = screen_obj.center

    def update_pos(self, pos, center_pos):
        self.pos = pos
        self.center_pos = center_pos

    def update_capture_stat(self, captured):
        self.captured = captured

    def move(self, obj, new_pos):
        pass

class Pawn(Piece): 
    value = 1

    # def __init__(self, colour='White', captured=False):
    # super().__init__(colour, captured)

    def valid_moves():
        pass


class Knight(Piece):
    value = 3

    def valid_moves():
        pass


class Bishop(Piece):
    value = 3

    def valid_moves():
        pass


class Rook(Piece):
    value = 5

    def valid_moves():
        pass


class Queen(Piece):
    value = 9

    def valid_moves():
        pass


class King(Piece):
    value = 0

    def valid_moves():
        pass