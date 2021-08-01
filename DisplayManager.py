import pygame
from pygame import *
from GameBoard import GameBoard

class DisplayManager:
    screen = None
    background = None
    blockWidth = 15
    blockHeight = 15

    @classmethod
    def init(cls, width, height):
        cls.screen = pygame.display.set_mode(((width + 2) * cls.blockWidth, (height + 2) * cls.blockHeight))
        cls.background = pygame.Surface(cls.screen.get_size())
        cls.background = cls.background.convert()
        cls.background.fill((0, 0, 0))
        cls.reset()

    @classmethod
    def reset(cls):
        cls.screen.blit(cls.background, (0, 0))

    @staticmethod
    def draw():
        pygame.display.flip()

    @classmethod
    def draw_player(cls, posX, posY):
        pygame.draw.rect(
            cls.screen,
            (255, 255, 255),
            ((posX + 1) * cls.blockWidth, (posY + 1) * cls.blockHeight, cls.blockWidth, cls.blockHeight),
            0
        )
    
    @classmethod
    def draw_candies(cls):
        for candy in GameBoard.candies:
            pygame.draw.rect(
                cls.screen,
                (0, 255, 255),
                ((candy[0] + 1) * cls.blockWidth, (candy[1] + 1) * cls.blockHeight, cls.blockWidth, cls.blockHeight),
                0
            )
    
    @classmethod
    def draw_trail(cls):
        for trail in GameBoard.trail:
            pygame.draw.rect(
                cls.screen,
                (255, 255, 255),
                ((trail[0] + 1) * cls.blockWidth, (trail[1] + 1) * cls.blockHeight, cls.blockWidth, cls.blockHeight),
                0
            )

    @classmethod
    def draw_border(cls):
        (width, height) = cls.screen.get_size()
        walls = [
            (0, 0, width, cls.blockHeight),
            (0, 0, cls.blockWidth, height),
            (0, height - cls.blockHeight, width, cls.blockHeight),
            (width - cls.blockWidth, 0, cls.blockWidth, width)
        ]
        for wall in walls:
            pygame.draw.rect(
                cls.screen,
                (255, 255, 255),
                wall,
                0
            )