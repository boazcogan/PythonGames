from enumeratedValues import *
import wallGeneration


class Board(object):
    '''
    A class that is meant to manage the game board for a pacman game
    '''
    def __init__(self, size=15):
        '''
        :param size: the size of the gameBoard
        :return: none
        '''
        # generate the board
        board = wallGeneration.maze(size,size)
        # set all falses to munchies
        Munchies = (board == False) * MUNCHIE
        # set all trues to walls
        board = board * WALL
        board = board + Munchies
        self.board = board

    def print(self):
        '''
        :return: easy display of internal game board structure
        '''
        print(self.board.view())

if __name__ == "__main__":
    board = Board(7)
    board.print()
