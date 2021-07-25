from board import Board
from config import *

from visualisations.knights_tour import KnightsTour

import pygame
import pygame_menu


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.screen.fill(Colour['WHITE'])
        self.init_board()
        # self.set_icons()        

    def init_board(self):
        '''Initializes Chess game board and pieces'''

        self.board = Board((BD_X, BD_Y))
        self.board.load_all_img()
        self.board.set_pos_all()

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

    # Main method
    def start(self):
        '''Main method for game loop'''

        sq1_pos = None
        sq2_pos = None
        game_over = False
        clicked_once = False
        move_status = -1

        mouse_pos = None

        def highlight_move():
            # Highlight non-king square
            if clicked_once:
                self.board.highlight_square(
                    self.screen,
                    Colour['RED'],
                    sq1_pos
                )

                for valid_move in self.board.valid_moves:
                    self.board.highlight_square(
                        self.screen, Colour['GREEN'],
                        valid_move
                    )

            # Highlight king's square if under check
            if self.board.under_check:
                self.board.highlight_square(
                    self.screen,
                    Colour['RED'],
                    self.board.king_pos[self.board.turn]
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
                self.init_board()

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
                        sq1_pos, self.board.turn
                    )
                    # print(self.board.get_sq_notation(sq1_pos))
                    # print(self.board.annotations.items())
                    # print(self.board.get_sq_coord(self.board.get_sq_notation(sq1_pos)))
                    # if type(piece1).__name__ == 'King':
                    #     print(piece1.pos)
                    #     print(self.board.king_pos[self.board.turn])
                    #     print(piece1.valid_moves())

                    if piece1 and piece1.colour == self.board.turn:
                        clicked_once = True
                        # To handle special flip board case for pawns
                        if type(piece1).__name__ == 'Pawn':
                            self.board.valid_moves = piece1.valid_moves(
                                self.board.is_flipped
                            )
                        else:
                            self.board.valid_moves = piece1.valid_moves()
                            # For highlighting beforehand

                # Click 2
                elif event.type == pygame.MOUSEBUTTONDOWN and clicked_once:
                    clicked_once = False

                    mouse_pos = pygame.mouse.get_pos()
                    sq2_pos = self.board.calc_sq_pos(mouse_pos)

                    # If second click is not the same as first, move the piece
                    if sq2_pos != sq1_pos and sq2_pos in self.board.valid_moves:
                        # print(self.board.get_sq_notation(sq2_pos))
                        move_status = piece1.handle_move(
                            self.board, sq1_pos, sq2_pos
                        )
                        if move_status == 1:
                            self.board.show_move(piece1)
                            self.board.is_checkmate()
                            self.board.set_next_turn()

            pygame.display.flip()


def init_pygame():
    '''Initializes pygame and returns screen object'''

    pygame.init()
    pygame.display.set_caption('ChessX')
    # Initialize screen
    screen = pygame.display.set_mode(
        # (S_WIDTH, S_HEIGHT + SQ_SZ)
        (S_WIDTH, S_HEIGHT)
    )

    return screen


def game_menu(screen):
    def start_game():
        new_game = Game(screen)
        new_game.start()

    def start_visualisation():
        new_tour = KnightsTour(screen)
        new_tour.start()

    menu = pygame_menu.Menu(height=S_HEIGHT,
                            width=S_WIDTH,
                            theme=pygame_menu.themes.THEME_DEFAULT,
                            title='ChessX')

    menu.add_button('Play', start_game)
    menu.add_button('Visualisation', start_visualisation)
    menu.add_button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(screen)


def main():
    screen = init_pygame()
    game_menu(screen)
        

main()
