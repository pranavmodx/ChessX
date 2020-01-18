from board import SQ_SZ

class Piece:
    def __init__(self, p_type, p_no, colour='White', captured=False):
        self.p_type = p_type
        self.p_no = p_no
        self.colour = colour
        self.captured = captured

    def set_img(self, img):
        self.img = img

    def img_size(self):
        return self.img

    def show(self, screen):
        screen_obj = screen.blit(self.img, self.pos)

    def set_pos(self, pos):
        self.pos = pos
        self.c_pos = (
            self.pos[0] + SQ_SZ // 2, self.pos[1] + SQ_SZ // 2
        )

    def move(self, pos):
        self.pos = pos
        self.c_pos = (
            pos[0] + SQ_SZ // 2, pos[1] + SQ_SZ // 2
        )

    def __repr__(self):
        if self.p_no:
            return f"{self.p_type}{self.p_no + 1}('{self.colour}')"
        else:
            return f"{self.p_type}('{self.colour}')"

    def __str__(self):
        if self.p_no:
            return f"{self.colour} {self.p_type} {self.p_no}"
        else:
            return f"{self.colour} {self.p_type}"