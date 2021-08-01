from Controller import Controller
from Exceptions import *
from GameBoard import GameBoard

Direction_Count = 4
Up = 0
Right = 1
Down = 2
Left = 3

MinUpdateDelay = 5
MaxUpdateDelay = 30
CandiesHeldAtMinUpdate = 30

class GameState:
    playerX = 0
    playerY = 0
    maxX = 0
    maxY = 0
    playerDir = Up

    UpdateDelay = 0
    TimeSinceUpdate = 0

    @classmethod
    def init(cls, x, y, maxX, maxY):
        cls.playerDir = Up
        cls.playerX = x
        cls.playerY = y
        cls.maxX = maxX
        cls.maxY = maxY
        cls.UpdateDelay = MaxUpdateDelay
        cls.TimeSinceUpdate = 0
        GameBoard.addCandy(x, y - 3)

    @classmethod
    def tick(cls):
        cls.TimeSinceUpdate += 1
        if (cls.TimeSinceUpdate >= cls.UpdateDelay):
            cls.TurnPlayer()
            cls.MovePlayer()
            cls.CheckPlayerCollisions()
            GameBoard.setPlayerPosition(cls.playerX, cls.playerY)
            cls.TimeSinceUpdate -= cls.UpdateDelay
            if cls.UpdateDelay > MinUpdateDelay:
                cls.UpdateDelay = cls.remap(GameBoard.candiesCollected, 0, CandiesHeldAtMinUpdate, MaxUpdateDelay, MinUpdateDelay)
                if cls.UpdateDelay < MinUpdateDelay:
                    cls.UpdateDelay = MinUpdateDelay

    @staticmethod
    def remap(value, oldMin, oldMax, newMin, newMax):
        return (((value - oldMin) * (newMax - newMin)) / (oldMax - oldMin)) + newMin
    
    @classmethod
    def TurnPlayer(cls):
        if cls.playerDir == Up or cls.playerDir == Down:
            if Controller.Horizontal == -1:
                cls.playerDir = Right
            elif Controller.Horizontal == 1:
                cls.playerDir = Left
        elif cls.playerDir == Left or cls.playerDir == Right:
            if Controller.Vertical == 1:
                cls.playerDir = Up
            elif Controller.Vertical == -1:
                cls.playerDir = Down
        pass
    
    @classmethod
    def MovePlayer(cls):
        if cls.playerDir == Up:
            cls.playerY -= 1
        elif cls.playerDir == Down:
            cls.playerY += 1
        elif cls.playerDir == Right:
            cls.playerX -= 1
        elif cls.playerDir == Left:
            cls.playerX += 1
    
    @classmethod
    def CheckPlayerCollisions(cls):
        boundsCheckX = cls.playerX < 0 or cls.playerX > cls.maxX
        boundsCheckY = cls.playerY < 0 or cls.playerY > cls.maxY
        if boundsCheckX or boundsCheckY:
            raise GameLoseException()
    
    @staticmethod
    def TurnRight(direction):
        return (direction + 1) % Direction_Count

    @staticmethod
    def TurnLeft(direction):
        return (direction + Direction_Count - 1) % Direction_Count