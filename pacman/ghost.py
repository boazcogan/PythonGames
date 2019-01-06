import numpy as np
from gameBoardClass import *
from enumeratedValues import *
from random import shuffle
import pygame

# currently ghosts are a very simple class with no actual functionality yet, evenually they will be managed by
# some form of AI
class Ghost(object):
    '''
    Ghosts will have an AI component added once the game is more playable
    '''
    def __init__(self, board, color, start, homeZone):
        '''
        :param board: the game board that will be played on
        :param start: the starting point of the Pacman
        :return: None
        '''

        self.board = board
        self.X, self.Y = start
        self.board.board[self.X][self.Y] = GHOST
        self.home = homeZone
        self.color = color
        self.onMunchie = True


    def HandleMove(self, direction, isWandering, screen, squareSize, radius):
        '''
        :param direction: u,l,d,r for up down left right
        :return:
        '''
        self.board.board[self.X][self.Y] = EMPTY
        if not self.onMunchie:
            pygame.draw.rect(screen, BLACK, (self.X*squareSize, self.Y*squareSize, squareSize, squareSize))
        else:
            pygame.draw.rect(screen, BLACK, (self.X*squareSize, self.Y*squareSize, squareSize, squareSize))
            pygame.draw.circle(screen, YELLOW,
                                       (squareSize*self.X+squareSize//4+radius//2,squareSize*self.Y+squareSize//4+radius//2), radius//2)
            self.board.board[self.X][self.Y] = MUNCHIE


        if direction == UP and self.board.board[self.X][self.Y-1] != WALL:
            if self.board.board[self.X][self.Y-1] == MUNCHIE:
                self.onMunchie = True
            else:
                self.onMunchie = False
            self.board.board[self.X][self.Y-1] = GHOST
            self.Y -= 1
            pygame.draw.circle(screen, self.color, (squareSize*(self.X)+radius,squareSize*(self.Y)+radius), radius)
            return True

        elif direction == LEFT and self.board.board[self.X-1][self.Y] != WALL:
            if self.board.board[self.X-1][self.Y] == MUNCHIE:
                self.onMunchie = True
            else:
                self.onMunchie = False
            self.board.board[self.X-1][self.Y] = GHOST
            self.X -= 1
            pygame.draw.circle(screen, self.color, (squareSize*(self.X)+radius,squareSize*(self.Y)+radius), radius)
            return True

        elif direction == DOWN and self.board.board[self.X][self.Y+1] != WALL:
            if self.board.board[self.X][self.Y+1] == MUNCHIE:
                self.onMunchie = True
            else:
                self.onMunchie = False
            self.board.board[self.X][self.Y+1] = GHOST
            self.Y += 1
            pygame.draw.circle(screen, self.color, (squareSize*(self.X)+radius,squareSize*(self.Y)+radius), radius)
            return True

        elif direction == RIGHT and self.board.board[self.X+1][self.Y] != WALL:
            if self.board.board[self.X+1][self.Y] == MUNCHIE:
                self.onMunchie = True
            else:
                self.onMunchie = False
            self.board.board[self.X+1][self.Y] = GHOST
            self.X += 1
            pygame.draw.circle(screen, self.color, (squareSize*(self.X)+radius,squareSize*(self.Y)+radius), radius)
            return True

        else:
            self.board.board[self.X][self.Y] = GHOST
            pygame.draw.circle(screen, self.color, (squareSize*(self.X)+radius,squareSize*(self.Y)+radius), radius)
            return False

    def Move(self, screen, squareSize, radius):
        """
        If there is a visible pacman nearby move towards it, otherwise wander around the home zone
        :return:
        """
        if self.IsPacVisible():
            pass
        else:
            self.Wander(screen, squareSize, radius)
        pass

    def IsPacVisible(self):
        '''
        :return: Direction if pacman is visible, False otherwise
        '''
        return False

    def Wander(self, screen, squareSize, radius):
        moves = [UP,DOWN,LEFT,RIGHT]
        shuffle(moves)
        for direction in moves:
            if self.HandleMove(direction, True, screen, squareSize, radius):
                return True
        return False