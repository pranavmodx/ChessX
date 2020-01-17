from board import SQ_SZ

class Piece:
    def __init__(self, colour='White', captured=False):
        self.colour = colour
        self.captured = captured

    def show(self, screen):
        screen_obj = screen.blit(self.img, self.pos)

    def set_pos(self, pos):
        self.pos = pos
        self.c_pos = (
            self.pos[0] + int(SQ_SZ // 2), self.pos[1] + int(SQ_SZ // 2)
        )

    def update_pos(self, pos):
        self.pos = pos
        self.c_pos = (
            pos[0] + int(SQ_SZ // 2), pos[1] + int(SQ_SZ // 2)
        )

    def update_capture_stat(self, captured):
        self.captured = captured

    def move(self, new_pos):
        self.update_pos(new_pos)