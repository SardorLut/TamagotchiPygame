import pygame

from src.Ball import Ball
from src.Globals import Globals
from src.Images import Images


class Fun(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x, self.y = x, y
        self.rect = pygame.Rect(x, y, Globals.ICON_SIZE, Globals.ICON_SIZE)

    def update(self, mouse):
        if self.rect.collidepoint(mouse) and len(Globals.objs) == 0:
            Ball(150, 410)
            if Globals.FUN + 10 >= 100:
                Globals.FUN = 100
            else:
                Globals.FUN += 10

    def draw(self):
        fun = pygame.transform.scale(Images.FUN_IMAGE, (Globals.ICON_SIZE, Globals.ICON_SIZE))
        Globals.window.blit(fun, (self.rect.x, self.rect.y))