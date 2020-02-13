from board import Board
from move import Move
from config import *
import pygame


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('ChessX')

        self.screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT + 75))
        self.screen.fill(Colour['WHITE'])

        self.board = Board((BD_X, BD_Y))
        self.board.load_all_img()
        self.board.set_pos_all()
        # self.board.display_all(self.screen)

        flip_board_pos = (int(S_WIDTH / 2.2), int(S_HEIGHT + (self.board.BD_SZ / 8) / 4))
        flip_board_icon = self.screen.blit(
            pygame.image.load(flip_board_rel_path + 'flip_board' + img_ext), 
            flip_board_pos,
        )

        self.move = Move()


    # Helper methods
    def delete_piece(self, board, piece):
        '''Deletes a given piece from the list of self.pieces'''

        if self.move.turn == 'White':
            if piece.p_type == 'Pawn':
                board.pieces['w_pawns'].remove(piece)
            else:
                board.pieces['w_pieces'].remove(piece)

        else:
            if piece.p_type == 'Pawn':
                board.pieces['b_pawns'].remove(piece)
            else:
                board.pieces['b_pieces'].remove(piece)

    
    # Main method
    def start(self):
        '''Main game loop'''

        sq1_pos = None
        sq2_pos = None
        game_over = False
        clicked_once = False

        while not game_over:
            # Display board and highlight screen
            self.board.display_all(self.screen)

            if clicked_once:
                self.board.highlight_square(self.screen, Colour['RED'], sq1_pos)

                for valid_move in self.move.valid_moves:
                    # print(valid_move)
                    self.board.highlight_square(self.screen, Colour['GREEN'], valid_move)

            # Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                # Click 1
                elif event.type == pygame.MOUSEBUTTONDOWN and not clicked_once:
                    mouse_pos = pygame.mouse.get_pos()

                    # Flip board
                    pos = (int(S_WIDTH / 2.2), S_HEIGHT + int(75 / 4))
                    if mouse_pos[0] in range(pos[0], pos[0] + 100) and \
                        mouse_pos[1] in range(pos[1], pos[1] + 100):
                        self.board.flip_board()
                        if self.board.is_flipped == False:
                            self.board.is_flipped = True
                        else:
                            self.board.is_flipped = False
                        continue

                    sq1_pos = self.board.calc_sq_pos(mouse_pos)
                    print(sq1_pos)
                    self.piece1 = self.move.fetch_piece_by_turn(self.board, sq1_pos)
                    print(self.piece1)

                    if self.piece1 and self.piece1.colour == self.move.turn:
                        clicked_once = True
                        self.move.valid_moves = self.piece1.valid_moves()

                # Click 2
                elif event.type == pygame.MOUSEBUTTONDOWN and clicked_once:
                    clicked_once = False

                    mouse_pos = pygame.mouse.get_pos()
                    sq2_pos = self.board.calc_sq_pos(mouse_pos)

                    # If second click is not the same as first, move the piece
                    if sq2_pos != sq1_pos and sq2_pos in self.move.valid_moves:
                        self.move.handle_piece(self.board, sq1_pos, sq2_pos)

            pygame.display.flip()


def main():
    new_game = Game()
    new_game.start()

main()