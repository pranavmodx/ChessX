from board import Board
from pieces import Knight
from config import *

import pygame


class KnightsTour():
    def __init__(self, screen):
        self.screen = screen
        self.init_board()

    def init_board(self):
        self.board = Board((BD_X, BD_Y))
        board_img_obj = pygame.image.load(
            '/Users/pranavmodx/Dev/gh_projects/ChessX/assets/img/board/board.png'
        )
        self.board.load_img(board_img_obj)

        self.knight = Knight()
        self.knight.pos = (0, 0)
        knight_img_obj = pygame.image.load(
            '/Users/pranavmodx/Dev/gh_projects/ChessX/assets/img/pieces/w_knight.png'
        )
        self.knight.load_img(knight_img_obj)

    def start(self):
        def isSafe(x, y, board):
            if x >= 0 and y >= 0 and x < 8 and y < 8 and board[x][y] == -1:
                return True
            return False

        def solveKT(n):
            board = [[-1 for i in range(n)]for i in range(n)]

            move_x = [2, 1, -1, -2, -2, -1, 1, 2] 
            move_y = [1, 2, 2, 1, -1, -2, -2, -1] 

            board[0][0] = 0
            # self.board.highlight_square(
            #     self.screen,
            #     Colour['RED'],
            #     self.knight.pos
            # )
            # pygame.display.update()

            pos = 1

            if(not solveKTUtil(n, board, 0, 0, move_x, move_y, pos)):
                print('Solution does not exist')
            else:
                # printSolution(n, board)
                print('Solution exists')

        def solveKTUtil(n, board, curr_x, curr_y, move_x, move_y, pos):
            if(pos == n**2):
                return True

            # Try all next moves from the current coordinate x, y
            for i in range(8):
                new_x = curr_x + move_x[i]
                new_y = curr_y + move_y[i]
                if(isSafe(new_x, new_y, board)):
                    board[new_x][new_y] = pos
                    # self.knight.move((new_x * 75, new_y * 75))
                    # self.board.highlight_square(
                    #     self.screen,
                    #     Colour['RED'],
                    #     (new_x * 75, new_y * 75)
                    # )
                    # pygame.display.update()
                    # pygame.time.delay(100)

                    if(solveKTUtil(n, board, new_x, new_y, move_x, move_y, pos+1)):
                        return True

                    # Backtracking
                    board[new_x][new_y] = -1
                    # self.knight.move((curr_x * 75, curr_y * 75))
                    # self.board.highlight_square(
                    #     self.screen,
                    #     Colour['GREEN'],
                    #     (new_x * 75, new_y * 75)
                    # )
                    # pygame.display.update()
                    # pygame.time.delay(100)
            return False

        solved = 0
        while True:
            self.board.display(self.screen)
            self.knight.display(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            if not solved:
                # solveKT(8)
                for i in range(2):
                    self.knight.move((75, 75))
                    self.knight.move((150, 150))
                # solved = 1
                pygame.time.delay(100)

            pygame.display.flip()
            
