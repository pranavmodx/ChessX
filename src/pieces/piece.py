class Piece:
    def __init__(self, p_no=None, colour='White', is_captured=False):
        self.p_no = p_no
        self.colour = colour
        self.is_captured = is_captured
        self.pos = None
        self.img = None

    def load_img(self, img):
        '''Loads image of piece'''
        self.img = img

    def size(self):
        '''Returns size (or default size) of piece image'''
        try:
            sz = self.img.get_height()
            return sz
        except:
            return 75  # Change later :P

    def display(self, screen):
        '''Displays image on screen'''
        screen_obj = screen.blit(self.img, self.pos)

    def set_pos(self, pos):
        '''Set initial position of piece'''
        self.pos = pos

    def move(self, pos):
        '''Move piece to required position'''
        self.pos = pos

    def __repr__(self):
        if self.p_no:
            return f"{type(self).__name__}{self.p_no + 1}('{self.colour}')"
        else:
            return f"{type(self).__name__}('{self.colour}')"

    def __str__(self):
        if self.p_no:
            return f"{self.colour} {type(self).__name__} {self.p_no}"
        else:
            return f"{self.colour} {type(self).__name__}"
