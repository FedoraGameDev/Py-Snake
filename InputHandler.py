import pygame
from Controller import Controller
from pygame import *
from Exceptions import *
from Controller import Controller

def HandleInput():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            raise ExitException()
        elif event.type == KEYDOWN:

            if event.key == K_UP or event.key == K_w:
                Controller.Vertical = 1
            elif event.key == K_DOWN or event.key == K_s:
                Controller.Vertical = -1

            if event.key == K_LEFT or event.key == K_a:
                Controller.Horizontal = -1
            elif event.key == K_RIGHT or event.key == K_d:
                Controller.Horizontal = 1
        
        elif event.type == KEYUP:
            if event.key == K_UP or event.key == K_w or event.key == K_DOWN or event.key == K_s:
                Controller.Vertical = 0
            elif event.key == K_RIGHT or event.key == K_d or event.key == K_LEFT or event.key == K_a:
                Controller.Horizontal = 0