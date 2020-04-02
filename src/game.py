from board import Board
from config import *
import pygame


class Game:
    def __init__(self):
        # Initialize pygame module
        pygame.init()
        pygame.display.set_caption('ChessX')

        # Initialize screen
        self.screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT + 75))
        self.screen.fill(Colour['WHITE'])

        # Initialize board
        self.board = Board((BD_X, BD_Y))
        self.board.load_all_img()
        self.board.set_pos_all()

        # Set flip board icon
        flip_board_pos = (int(S_WIDTH / 2.2), int(S_HEIGHT + (self.board.BD_SZ / 8) / 4))
        flip_board_icon = self.screen.blit(
            pygame.image.load(flip_board_rel_path + 'flip_board' + img_ext), 
            flip_board_pos,
        )

        # Set reset board icon
        reset_board_pos = (int(S_WIDTH / 2.2) + 100, int(S_HEIGHT + (self.board.BD_SZ / 8) / 4))
        reset_board_icon = self.screen.blit(
            pygame.image.load(reset_board_rel_path + 'reset_board' + img_ext), 
            reset_board_pos,
        )

        # Initialize game parameters
        self.turn = 'White'
        self.valid_moves = []
        self.under_check = False

    def next_turn(self):
        if self.turn == 'White':
            self.turn = 'Black'
        else:
            self.turn = 'White'
    
    # Main method
    def start(self):
        '''Main game loop'''

        sq1_pos = None
        sq2_pos = None
        game_over = False
        clicked_once = False
        move_status = ''

        while not game_over:
            # Display board
            self.board.display_all(self.screen)

            # Highlight squares
            if clicked_once:
                self.board.highlight_square(self.screen, Colour['RED'], sq1_pos)

                for valid_move in self.valid_moves:
                    self.board.highlight_square(self.screen, Colour['GREEN'], valid_move)

            # Highlight king if under check
            if self.under_check:
                self.board.highlight_square(self.screen, Colour['RED'], self.board.king_pos[self.turn])

            # Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                # Click 1
                elif event.type == pygame.MOUSEBUTTONDOWN and not clicked_once:
                    mouse_pos = pygame.mouse.get_pos()
                    print(mouse_pos)

                    # Flip board
                    pos = (int(S_WIDTH / 2.2), S_HEIGHT + int(75 / 4))
                    if mouse_pos[0] in range(pos[0], pos[0] + 100) and \
                        mouse_pos[1] in range(pos[1], pos[1] + 100):
                        self.board.flip_board()

                    # Reset board
                    pos2 = (int(S_WIDTH / 2.2) + 100, S_HEIGHT + int(75 / 4))
                    if mouse_pos[0] in range(pos2[0], pos2[0] + 100) and \
                        mouse_pos[1] in range(pos2[1], pos2[1] + 100):
                        del self.board
                        self.board = Board((BD_X, BD_Y))
                        self.board.load_all_img()
                        self.board.set_pos_all()
                        self.turn = 'White'


                    sq1_pos = self.board.calc_sq_pos(mouse_pos)
                    print(sq1_pos)
                    print(self.board.get_notation(sq1_pos))
                    piece1 = self.board.fetch_piece_by_turn(sq1_pos, self.turn)
                    if piece1:
                        print(piece1)
                        print(piece1.pos)

                    if piece1 and piece1.colour == self.turn:
                        clicked_once = True
                        # Pawn valid moves - handle flip board
                        if type(piece1).__name__ == 'Pawn':
                            self.valid_moves = piece1.valid_moves(self.board.is_flipped)
                        else:
                            self.valid_moves = piece1.valid_moves() # For highlighting beforehand

                # Click 2
                elif event.type == pygame.MOUSEBUTTONDOWN and clicked_once:
                    clicked_once = False

                    mouse_pos = pygame.mouse.get_pos()
                    sq2_pos = self.board.calc_sq_pos(mouse_pos)

                    # If second click is not the same as first, move the piece
                    if sq2_pos != sq1_pos and sq2_pos in self.valid_moves:
                        if not self.under_check:
                            move_status = piece1.handle_move(self.board, sq1_pos, sq2_pos)
                        else:
                            move_status = piece1.handle_move(self.board, sq1_pos, sq2_pos, self.under_check)
                        print(move_status)
                        if move_status == 1:
                            self.next_turn()
                        elif move_status == -1:
                            self.next_turn()
                            self.under_check = True

            pygame.display.flip()


def main():
    new_game = Game()
    new_game.start()

main()