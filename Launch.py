import pygame
from DisplayManager import DisplayManager
from GameState import GameState
from GameBoard import GameBoard
import InputHandler
import Controller
from Exceptions import *
from pygame.locals import *

GAME_WIDTH = 30
GAME_HEIGHT = 30

pygame.init()
DisplayManager.init(GAME_WIDTH, GAME_HEIGHT)
GameBoard.init(GAME_WIDTH, GAME_HEIGHT)
GameState.init(int(GAME_WIDTH / 2), int(GAME_HEIGHT / 2), GAME_WIDTH, GAME_HEIGHT)
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

def Launch():
    gameRunning = True
    while gameRunning:
        clock.tick(60)

        try:
            DisplayManager.reset()

            InputHandler.HandleInput()
            GameState.tick()
            
            DisplayManager.draw_player(GameState.playerX, GameState().playerY)
            DisplayManager.draw_trail()
            DisplayManager.draw_border()
            DisplayManager.draw_candies()

            DisplayManager.draw()
        
        except GameWinException:
            print("Game Won!")
            gameRunning = False
        
        except GameLoseException:
            print("Game Lost!")
            GameBoard.init(GAME_WIDTH, GAME_HEIGHT)
            GameState.init(int(GAME_WIDTH / 2), int(GAME_HEIGHT / 2), GAME_WIDTH, GAME_HEIGHT)

        except ExitException:
            print("Application Closing.")
            return
        
Launch()