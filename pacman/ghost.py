import numpy as np
from gameBoardClass import *
from enumeratedValues import *

# currently ghosts are a very simple class with no actual functionality yet, evenually they will be managed by
# some form of AI
class Ghost(object):
    '''
    Ghosts will have an AI component added once the game is more playable
    '''
    def __init__(self, board, start):
        '''
        :param board: the game board that will be played on
        :param start: the starting point of the Pacman
        :return: None
        '''
        self.board = board
        self.X, self.Y = start
        self.board.board[self.X][self.Y] = GHOST

    def move(self, direction):
        '''
        :param direction: u,l,d,r for up down left right
        :return:
        '''
        self.board.board[self.X][self.Y] = EMPTY
        if direction == UP and self.board.board[self.X][self.Y-1] != -1:
            self.board.board[self.X][self.Y-1] = GHOST
            self.Y -= 1
        elif direction == LEFT and self.board.board[self.X-1][self.Y] != -1:
            self.board.board[self.X-1][self.Y] = GHOST
            self.X -= 1
        elif direction == DOWN and self.board.board[self.X][self.Y+1] != -1:
            self.board.board[self.X][self.Y+1] = GHOST
            self.Y += 1
        elif direction == RIGHT and self.board.board[self.X+1][self.Y] != -1:
            self.board.board[self.X+1][self.Y] = GHOST
            self.X += 1