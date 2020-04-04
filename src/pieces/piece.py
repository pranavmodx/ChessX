class Piece:
    def __init__(self, p_no=None, colour='White'):
        self.p_no = p_no
        self.colour = colour
        self.captured = False

    def load_img(self, img):
        '''Loads image of piece'''
        self.img = img

    def size(self):
        '''Returns size (or default size) of piece image'''

        try:
            sz = self.img.get_height()
            return sz
        except:
            return 75 # Change later :P

    def display(self, screen):
        '''Displays image on screen'''

        screen_obj = screen.blit(self.img, self.pos)

    def set_pos(self, pos):
        self.pos = pos

    def move(self, pos):
        self.pos = pos

    def next_turn(self):
        if self.colour == 'White':
            return 'Black'
        else:
            return 'White'

    def __repr__(self):
        if self.p_no:
            return f"{type(self).__name__}{self.p_no + 1}('{self.colour}')"
        else:
            return f"{self.p_type}('{self.colour}')"

    def __str__(self):
        if self.p_no:
            return f"{self.colour} {type(self).__name__} {self.p_no}"
        else:
            return f"{self.colour} {type(self).__name__}"