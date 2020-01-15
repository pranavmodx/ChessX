import window
import pygame


class Board:
    def load_img(self, path):
        self.img = pygame.image.load(path)
        self.size = self.img.get_height()

    def show(self):
        screen_obj = window.screen.blit(self.img, self.pos)

    def set_pos(self, pos):
        self.pos = pos

    @staticmethod
    def highlight_square(surface, color, rect_dim, width=5):
        r_left, r_top, r_width, r_height = rect_dim
        pygame.draw.rect(surface, color, pygame.Rect(r_left, r_top, r_width, r_height), width)


bd_obj = Board()

board_rel_path = '../assets/img/board/'
img_ext = '.png'
bd_obj.load_img(board_rel_path + 'board' + img_ext)

# Board position
bd_x = window.S_WIDTH * 0.0
bd_y = window.S_HEIGHT * 0.0

# Board size
BD_SZ = bd_obj.size

# Square size
SQ_SZ = BD_SZ / 8

# Initial piece position
x_pos = bd_x + 5
up_y_pos = bd_y + 5
down_y_pos = up_y_pos + (BD_SZ - SQ_SZ)