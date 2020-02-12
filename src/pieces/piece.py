class Piece:
    def __init__(self, p_type, p_no, colour='White'):
        self.p_type = p_type
        self.p_no = p_no
        self.colour = colour
        # self.captured = captured

    def load_img(self, img):
        '''Loads image of piece'''
        self.img = img

    def size(self):
        return self.img.get_height()

    def display(self, screen):
        screen_obj = screen.blit(self.img, self.pos)

    def set_pos(self, pos):
        self.pos = pos

    def move(self, pos):
        self.pos = pos

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