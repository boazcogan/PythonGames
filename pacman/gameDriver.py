from gameBoardClass import *
from ghost import *
from pacman import *
import pygame
import sys
import time

class gameDriver(object):
    '''
    The game driver will manage the individual game components and run the game.
    The graphical display belongs to the game driver.
    '''
    def __init__(self, size, ghosts):
        # assertions to determine if the game is running properly
        assert ghosts < 5, "to many ghosts, please use a number between 1 and 4"
        assert ghosts > 0, "not enough ghosts, please use a number between 1 and 4"
        assert type(ghosts) == int, "ghosts requires an integer value"
        assert type(size) == int, "the board size requires an integer value"
        assert size > 15, "the board must be at least of size 15"
        if size%2 == 0:
            size += 1
        # Ensure that the size is odd and start a ghost at each corner
        self.board = Board(size)
        self.size = size
        ghostLocations = [(1,1),(1,size-2),(size-2,size-2), (size-2, 1)]
        homeZones = [
            [[0,0],[len(self.board.board)//2,len(self.board.board)//2]],
            [[len(self.board.board)//2,0],[len(self.board.board),len(self.board.board)//2]],
            [[0,len(self.board.board)//2],[len(self.board.board)//2,len(self.board.board)]],
            [[len(self.board.board)//2,len(self.board.board)//2],[len(self.board.board),len(self.board.board)]]
                    ]

        self.ghosts = [Ghost(self.board, BLUE, ghostLocations[i], homeZones[i]) for i in range(len(ghostLocations))]
        self.pacman = Pacman(self.board, (size//2,size//2))
        # all internal elements were appropriately allocated so initialize the graphical window
        pygame.init()
        # TODO: allow the window and square size to be dynamic
        self.squareSize = 25
        winSize = (self.squareSize * size, self.squareSize * size)
        self.screen = pygame.display.set_mode(winSize)
        self.radius = self.squareSize//2-self.squareSize//10

    def print(self):
        # print the board for debugging purposes
        self.board.print()

    def getPacMove(self):
        # primitive move manager no longer in use
        pacMove = input('Enter a move (w,a,s,d): ')
        if pacMove == 'q':
            exit()
        return MOVEDICT[pacMove]

    def GameOver(self):
        # if there are no more munchies the pacman wins
        if (sum(sum(self.board.board == MUNCHIE))) == 0:
            print("Congratulations you found all the munchies")
            return True
        # if there is pacman the game continues
        if sum(sum(self.board.board == PACMAN)) != 0:
            return False
        # if there is no pacman the ghosts win
        print("Oh no, you've been caught by a ghost!")
        return True

    def playGame(self):
        # manage the game run instance
        GameRunning = True
        # draw the game window
        self.drawGame()
        pygame.display.update()
        # tic for the games internal clock
        tic = time.time()
        while GameRunning:
            toc = time.time()
            if toc-tic > 1:
                for ghost in self.ghosts:
                    ghost.Move(self.screen, self.squareSize, self.radius)
                tic = toc
                pygame.display.update()
                GameRunning = not self.GameOver()

            # while the game is running, get all the events
            for event in pygame.event.get():
                # for each event handle is, if its a quit then quit
                # otherwise if its a key pressed then handle it
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYUP:
                    # if the key pressed is one of the ones that is known how to handle then
                    # pass the character value of the unicode character to the MOVEDICT to determine
                    # where the user wants to move
                    UIN = chr(event.key)
                    if UIN in MOVEDICT.keys():
                        # let the pacman move
                        self.pacman.move(MOVEDICT[UIN], self.screen, self.squareSize, self.radius)
                        pygame.display.update()
                        GameRunning = not self.GameOver()

    def drawGame(self):
        # initially the game must be drawn, all munchies are small yellow dots, all ghosts are blue circles
        # all Pacmen are yellow circles, and all walls are puple squares.
        for col in range(self.size):
            for row in range(self.size):
                if self.board.board[col][row] == MUNCHIE:
                    pygame.draw.circle(self.screen, YELLOW,
                                       (self.squareSize*(col)+self.squareSize//4+self.radius//2,self.squareSize*(row)+self.squareSize//4+self.radius//2), self.radius//2)
                elif self.board.board[col][row] == GHOST:
                    pygame.draw.circle(self.screen, BLUE,
                                       (self.squareSize*(col)+self.radius,self.squareSize*(row)+self.radius), self.radius)
                elif self.board.board[col][row] == PACMAN:
                    pygame.draw.circle(self.screen, WHITE,
                                       (self.squareSize*(col)+self.radius,self.squareSize*(row)+self.radius), self.radius)
                elif self.board.board[col][row] == WALL:
                    pygame.draw.rect(self.screen, PURPLE,
                                     (self.squareSize*(col), self.squareSize*(row), self.squareSize, self.squareSize), 5)

if __name__ == '__main__':
    game = gameDriver(17,4)
    game.playGame()
