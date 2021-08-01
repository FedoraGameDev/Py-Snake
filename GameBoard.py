import random
from Exceptions import *

EMPTY = 0
CANDY = 1
PLAYER = 2
TRAIL = 3

class GameBoard:
    board = None
    trail = []
    candies = []
    candiesCollected = 0
    maxCandies = 0

    @classmethod
    def init(cls, boardWidth, boardHeight):
        cls.board = [[0] * boardWidth for i in range(boardHeight)]
        cls.trail = []
        cls.candies = []
        cls.candiesCollected = 0
        cls.maxCandies = (boardWidth * boardHeight) - 5

    @classmethod
    def setPlayerPosition(cls, playerX, playerY):
        if cls.board[playerX][playerY] == TRAIL:
            raise GameLoseException()
            
        addTail = False
        if cls.board[playerX][playerY] == CANDY:
            addTail = True
            cls.candies.remove((playerX, playerY))
            cls.addCandy()
            cls.candiesCollected += 1
        
        if len(cls.trail) == 0:
            addTail = True

        cls.clearBoard()
        cls.board[playerX][playerY] = PLAYER
        for i in cls.trail:
            cls.board[i[0]][i[1]] = TRAIL
        for i in cls.candies:
            cls.board[i[0]][i[1]] = CANDY
        cls.trail.append((playerX, playerY))
        if not addTail:
            del(cls.trail[0])
    
    @classmethod
    def addCandy(cls, posX = -1, posY = -1):
        if (posX == -1):
            posX = random.randrange(len(cls.board[0]))
        if (posY == -1):
            posY = random.randrange(len(cls.board))

        if cls.board[posX][posY] == TRAIL or cls.board[posX][posY] == PLAYER:
            cls.addCandy()
            return

        cls.candies.append((posX, posY))

    @classmethod
    def clearBoard(cls):
        cls.board = [[0] * len(cls.board[0]) for i in range(len(cls.board))]