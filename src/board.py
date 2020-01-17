from config import *
import pygame


class Board:
    def load_img(self, path):
        self.img = pygame.image.load(path)
        self.size = self.img.get_height()

    def show(self, screen):
        screen_obj = screen.blit(self.img, self.pos)

    def set_pos(self, x, y):
        self.pos = (x, y)

    @staticmethod
    def highlight_square(surface, color, rect_dim, width=5):
        r_left, r_top, r_width, r_height = rect_dim
        pygame.draw.rect(
            surface, 
            color, 
            pygame.Rect(r_left, r_top, r_width, r_height), 
            width
        )


bd_obj = Board()
bd_obj.load_img(board_rel_path + 'board' + img_ext)

# Board position
bd_x = S_WIDTH * 0.0
bd_y = S_HEIGHT * 0.0

bd_obj.set_pos(bd_x, bd_y)

# Board size
BD_SZ = bd_obj.size

# Square size
SQ_SZ = BD_SZ / 8