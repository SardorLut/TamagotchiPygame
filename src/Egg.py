import pygame

from src.Globals import Globals
from src.Images import Images
from src.Pet import Pet


class Egg:
    """Яйцо, при исчезновении появиться питомец"""
    def __init__(self, colour, x, y):
        """Инициализация яйца, положение и размер"""
        self.x, self.y = x, y
        self.colour = colour
        self.delay = 0
        self.size_of_egg = 100
        Globals.objs.append(self)
        self.stop = 120

    def draw(self):
        """Отрисовать на экране яйцо, через определенное время родить питомца и удалить яйцо"""
        if self.delay != self.stop:
            if self.delay < self.stop / 6:
                egg = pygame.transform.scale(Images.EGG_IMAGE[0], (self.size_of_egg, self.size_of_egg * 1.2))
            elif (self.stop / 6) <= self.delay < (self.stop / 3):
                egg = pygame.transform.scale(Images.EGG_IMAGE[1], (self.size_of_egg, self.size_of_egg * 1.2))
            elif (self.stop / 3) <= self.delay < (self.stop / 2):
                egg = pygame.transform.scale(Images.EGG_IMAGE[2], (self.size_of_egg, self.size_of_egg * 1.2))
            elif (self.stop / 2) <= self.delay < (self.stop * 5 / 6):
                egg = pygame.transform.scale(Images.EGG_IMAGE[3], (self.size_of_egg, self.size_of_egg * 1.2))
            else:
                egg = pygame.transform.scale(Images.EGG_IMAGE[4], (self.size_of_egg, self.size_of_egg * 1.2))
            Globals.window.blit(egg, (self.x, self.y))
            self.delay += 1
        else:
            x, y = 250, 300
            Pet(self.colour, 250, 300)
            Globals.objs.remove(self)
