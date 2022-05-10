from __future__ import annotations
import pygame

from src.Ball import Ball
from src.Globals import Globals
from src.Images import Images


class Fun(pygame.sprite.Sprite):
    """Иконка веселья на экране, при нажатии повеселить питомца"""
    def __init__(self, x, y):
        """Инициализации иконки на экране, его положение"""
        pygame.sprite.Sprite.__init__(self)
        self.x, self.y = x, y
        self.rect = pygame.Rect(x, y, Globals.ICON_SIZE, Globals.ICON_SIZE)

    def update(self, mouse):
        """При нажатии на иконку веселься, развеселить питомца"""
        if self.rect.collidepoint(mouse) and len(Globals.objs) == 0:
            x, y = 150, 410
            max = 100
            get = 10
            Ball(x, y)
            if Globals.FUN + get >= max:
                Globals.FUN = max
            else:
                Globals.FUN += get

    def draw(self):
        """Отрисовать на экране иконку"""
        fun = pygame.transform.scale(Images.FUN_IMAGE, (Globals.ICON_SIZE, Globals.ICON_SIZE))
        Globals.window.blit(fun, (self.rect.x, self.rect.y))
