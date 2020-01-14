import window

import pygame


class Piece:
    def __init__(self, colour='White', captured=False):
        self.colour = colour
        self.captured = captured

    def load_img(self, img_path):
        self.img = pygame.image.load(img_path)

    def show(self):
        screen_obj = window.screen.blit(self.img, (self.pos[0], self.pos[1]))

    def set_pos(self, pos):
        self.pos = (int(pos[0]), int(pos[1]))
        self.c_pos = (self.pos[0] + int(75 // 2), self.pos[1] + int(75 // 2))

    def update_pos(self, pos):
        self.pos = pos
        self.c_pos = (pos[0] + int(75 // 2), pos[1] + int(75 // 2))

    def update_capture_stat(self, captured):
        self.captured = captured

    def move(self, coeff):
        new_pos = (self.pos[0] + 75 * coeff[0], self.pos[1] + 75 * coeff[1])

        self.update_pos(new_pos)

 
class Pawn(Piece): 
    value = 1 

    def __init__(self, p_no, colour='White', captured=False):
        super().__init__(colour, captured)
        self.p_no = p_no

    def __repr__(self):
        return f'Pawn{self.p_no + 1}({self.colour})'

    def __str__(self):
        return f'Pawn{self.p_no + 1}({self.colour})'

    def valid_moves():
        pass


class Knight(Piece):
    value = 3

    def __init__(self, k_no, colour='White', captured=False):
        super().__init__(colour, captured)
        self.k_no = k_no

    def __repr__(self):
        return f'Knight{self.k_no}({self.colour})'

    def __str__(self):
        return f'Knight{self.k_no}({self.colour})'

    def valid_moves():
        pass


class Bishop(Piece):
    value = 3

    def __init__(self, b_no, colour='White', captured=False):
        super().__init__(colour, captured)
        self.b_no = b_no

    def __repr__(self):
        return f'Bishop{self.b_no}({self.colour})'

    def __str__(self):
        return f'Bishop{self.b_no}({self.colour})'

    def valid_moves():
        pass


class Rook(Piece):
    value = 5

    def __init__(self, r_no, colour='White', captured=False):
        super().__init__(colour, captured)
        self.r_no = r_no

    def __repr__(self):
        return f'Rook{self.r_no}({self.colour})'

    def __str__(self):
        return f'Rook{self.r_no}({self.colour})'

    def valid_moves():
        pass


class Queen(Piece):
    value = 9

    def __repr__(self):
        return f'Queen({self.colour})'

    def __str__(self):
        return f'Queen({self.colour})'

    def valid_moves():
        pass


class King(Piece):
    value = 0

    def __repr__(self):
        return f'King({self.colour})'

    def __str__(self):
        return f'King({self.colour})'

    def valid_moves():
        pass