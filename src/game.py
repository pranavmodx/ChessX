from board import Board
from config import *
import pygame

class Game:
    def __init__(self):
        self.init_pygame()
        self.init_board()
        self.set_icons()

        # Initialize game parameters
        self.turn = 'White'
        self.valid_moves = []

    def init_pygame(self):
        '''Initializes pygame and sets screen'''

        pygame.init()
        pygame.display.set_caption('ChessX')
        # Initialize screen
        self.screen = pygame.display.set_mode(
            (S_WIDTH, S_HEIGHT + SQ_SZ)
        )
        self.screen.fill(Colour['WHITE'])

    def init_board(self):
        '''Initializes Chess game board and pieces'''

        self.board = Board((BD_X, BD_Y))
        self.board.load_all_img()
        self.board.set_pos_all()
        self.board.annotate_board()

    def set_icons(self):
        '''Sets game icons'''

        # Flip board icon
        flip_board_pos = (
            int(S_WIDTH / 2.2), 
            int(S_HEIGHT + (self.board.BD_SZ / 8) / 4)
        )
        flip_board_icon = self.screen.blit(
            pygame.image.load(
                flip_board_rel_path + 'flip_board' + img_ext
            ), 
            flip_board_pos,
        )
        # Reset board icon
        reset_board_pos = (
            int(S_WIDTH / 2.2) + 100, 
            int(S_HEIGHT + (self.board.BD_SZ / 8) / 4)
        )
        reset_board_icon = self.screen.blit(
            pygame.image.load(
                reset_board_rel_path + 'reset_board' + img_ext
            ), 
            reset_board_pos,
        )

    def set_next_turn(self):
        '''Switches the turn to next player'''

        if self.turn == 'White':
            self.turn = 'Black'
        else:
            self.turn = 'White'

    # Main method
    def start(self):
        '''Main method for game loop'''

        sq1_pos = None
        sq2_pos = None
        game_over = False
        clicked_once = False
        move_status = ''

        mouse_pos = None

        def highlight_move():
            # Highlight non-king square
            if clicked_once:
                self.board.highlight_square(
                    self.screen, 
                    Colour['RED'], 
                    sq1_pos
                )

                for valid_move in self.valid_moves:
                    self.board.highlight_square(
                        self.screen, Colour['GREEN'], 
                        valid_move
                    )

            # Highlight king's square if under check
            if self.board.under_check:
                self.board.highlight_square(
                    self.screen, 
                    Colour['RED'], 
                    self.board.king_pos[self.turn]
                )

        def handle_flip():
            # Flip board
            pos = (int(S_WIDTH / 2.2), S_HEIGHT + int(SQ_SZ / 4))
            if mouse_pos[0] in range(pos[0], pos[0] + 100) and \
                mouse_pos[1] in range(pos[1], pos[1] + 100):
                self.board.flip_board()

        def handle_reset():
            # Reset board
            pos = (
                int(S_WIDTH / 2.2) + 100, S_HEIGHT + int(SQ_SZ / 4)
            )
            if mouse_pos[0] in range(pos[0], pos[0] + 100) and \
                mouse_pos[1] in range(pos[1], pos[1] + 100):
                del self.board
                self.board = Board((BD_X, BD_Y))
                self.board.load_all_img()
                self.board.set_pos_all()
                self.board.annotate_board()
                self.turn = 'White'

        # Game loop
        while not game_over:
            # Display board
            self.board.display_all(self.screen)

            # Highlight moves
            highlight_move()

            # Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                # Click 1
                elif event.type == pygame.MOUSEBUTTONDOWN and \
                    not clicked_once:
                    mouse_pos = pygame.mouse.get_pos()

                    handle_flip()
                    handle_reset()

                    sq1_pos = self.board.calc_sq_pos(mouse_pos)
                    piece1 = self.board.fetch_piece_by_turn(
                        sq1_pos, self.turn
                    )
                    if type(piece1).__name__ == 'King':
                        print(piece1.pos)
                        print(self.board.king_pos[self.turn])
                        print(piece1.valid_moves())

                    if piece1 and piece1.colour == self.turn:
                        clicked_once = True
                        # To handle special flip board case for pawns
                        if type(piece1).__name__ == 'Pawn':
                            self.valid_moves = piece1.valid_moves(
                                self.board.is_flipped
                            )
                        else:
                            self.valid_moves = piece1.valid_moves() 
                            # For highlighting beforehand

                # Click 2
                elif event.type == pygame.MOUSEBUTTONDOWN and clicked_once:
                    clicked_once = False

                    mouse_pos = pygame.mouse.get_pos()
                    sq2_pos = self.board.calc_sq_pos(mouse_pos)

                    # If second click is not the same as first, move the piece
                    if sq2_pos != sq1_pos and sq2_pos in self.valid_moves:
                        move_status = piece1.handle_move(
                            self.board, sq1_pos, sq2_pos
                        )
                        if move_status == 1:
                            self.set_next_turn()

            pygame.display.flip()


def main():
    new_game = Game()
    new_game.start()

main()