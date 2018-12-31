from gameBoardClass import *
from enumeratedValues import *
import pygame

# enumerated types allows for numeric values to have a name. It's more of a band-aid then a fix.
class Pacman(object):
    def __init__(self, board, start):
        '''
        :param board: the game board that will be played on
        :param start: the starting point of the Pacman
        :return: None
        '''
        self.board = board
        self.X, self.Y = start
        self.board.board[self.X][self.Y] = PACMAN


    def move(self, direction, screen, squareSize, radius):
        '''
        Moves the Pacman
        :param direction: which way will he go
        :param screen: the game screen
        :param squareSize: the square size that is drawn on
        :param radius: the radius of the circle
        :return: None
        '''
        # overwrite the pacman with a black square and set its position to empty
        self.board.board[self.X][self.Y] = EMPTY
        pygame.draw.rect(screen, BLACK, (self.X*squareSize, self.Y*squareSize, squareSize, squareSize))

        if direction == UP:
            # if up is a valid move for the pacman
            if self.board.board[self.X][self.Y-1] >= 1:
                # set the new position to the pacman and redraw him
                self.board.board[self.X][self.Y-1] = PACMAN
                self.Y -= 1
                pygame.draw.circle(screen, WHITE, (squareSize*(self.X)+radius,squareSize*(self.Y)+radius), radius)
            elif self.board.board[self.X][self.Y-1] == -1:
                # up must not have been valid so redraw him in his current position. Note that the user will not see
                # pacman flicker since pygame update has not been called.
                self.board.board[self.X][self.Y] = PACMAN
                pygame.draw.circle(screen, WHITE, (squareSize*(self.X)+radius,squareSize*(self.Y)+radius), radius)

        # the rest of the directions are the same logic as above
        elif direction == LEFT:
            if self.board.board[self.X-1][self.Y] >= 1:
                self.board.board[self.X-1][self.Y] = PACMAN
                self.X -= 1
                pygame.draw.circle(screen, WHITE, (squareSize*(self.X)+radius,squareSize*(self.Y)+radius), radius)
            elif self.board.board[self.X-1][self.Y] == -1:
                self.board.board[self.X][self.Y] = PACMAN
                pygame.draw.circle(screen, WHITE, (squareSize*(self.X)+radius,squareSize*(self.Y)+radius), radius)

        elif direction == DOWN:
            if self.board.board[self.X][self.Y+1] >= 1:
                self.board.board[self.X][self.Y+1] = PACMAN
                self.Y += 1
                pygame.draw.circle(screen, WHITE, (squareSize*(self.X)+radius,squareSize*(self.Y)+radius), radius)
            elif self.board.board[self.X][self.Y+1] == -1:
                self.board.board[self.X][self.Y] = PACMAN
                pygame.draw.circle(screen, WHITE, (squareSize*(self.X)+radius,squareSize*(self.Y)+radius), radius)

        elif direction == RIGHT:
            if self.board.board[self.X+1][self.Y] >= 1:
                self.board.board[self.X+1][self.Y] = PACMAN
                self.X += 1
                pygame.draw.circle(screen, WHITE, (squareSize*(self.X)+radius,squareSize*(self.Y)+radius), radius)
            elif self.board.board[self.X+1][self.Y] == -1:
                self.board.board[self.X][self.Y] = PACMAN
                pygame.draw.circle(screen, WHITE, (squareSize*(self.X)+radius,squareSize*(self.Y)+radius), radius)

