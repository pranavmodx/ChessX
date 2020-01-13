from window import *
import pygame


class Board:
    # def __init__(self, height, width):
    #     self.height = height
    #     self.width = width

    def load_img(self, path):
        self.img = pygame.image.load(path)
        # print(self.img.__dir__())
        self.size = self.img.get_height()

    def show(self):
        screen_obj = screen.blit(self.img, (self.pos[0], self.pos[1]))

    def set_pos(self, pos):
        screen_obj = screen.blit(self.img, (pos[0], pos[1]))
        self.pos = pos

    @staticmethod
    def highlight_square(surface, color, rect, width=3):
        left, top, rect_width, height = rect
        pygame.draw.rect(surface, color, pygame.Rect(left, top, rect_width, height), width)