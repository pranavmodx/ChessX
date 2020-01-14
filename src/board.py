import window
import pygame


class Board:
    def load_img(self, path):
        self.img = pygame.image.load(path)
        self.size = self.img.get_height()

    def show(self):
        screen_obj = window.screen.blit(self.img, (self.pos[0], self.pos[1]))

    def set_pos(self, pos):
        self.pos = pos

    @staticmethod
    def highlight_square(surface, color, rect_dim, width=3):
        left, top, r_width, height = rect_dim
        pygame.draw.rect(surface, color, pygame.Rect(left, top, r_width, height), width)