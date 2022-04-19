import pygame

from src.Globals import Globals
from src.Images import Images


class Bread:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.frame = 0
        Globals.breads.append(self)
        Globals.objs.append(self)
        self.stop = 60
        self.delay = 0

    def draw(self):
        if self.delay < self.stop / 6:
            bread = pygame.transform.scale(Images.BREAD_IMAGE[0], (Globals.FOOD_SIZE, Globals.FOOD_SIZE))
        elif (self.stop / 6) <= self.delay < (self.stop * 2 / 6):
            bread = pygame.transform.scale(Images.BREAD_IMAGE[1], (Globals.FOOD_SIZE, Globals.FOOD_SIZE))

        elif (self.stop * 2 / 6) <= self.delay < (self.stop * 3 / 6):
            bread = pygame.transform.scale(Images.BREAD_IMAGE[2], (Globals.FOOD_SIZE, Globals.FOOD_SIZE))

        elif (self.stop * 3 / 6) <= self.delay < (self.stop * 4 / 6):
            bread = pygame.transform.scale(Images.BREAD_IMAGE[3], (Globals.FOOD_SIZE, Globals.FOOD_SIZE))
        elif (self.stop * 4 / 6) <= self.delay < (self.stop * 5 / 6):
            bread = pygame.transform.scale(Images.BREAD_IMAGE[4], (Globals.FOOD_SIZE, Globals.FOOD_SIZE))
        else:
            bread = pygame.transform.scale(Images.BREAD_IMAGE[5], (Globals.FOOD_SIZE, Globals.FOOD_SIZE))
        self.delay += 1
        if self.delay == self.stop:
            Globals.objs.remove(self)
            Globals.breads.remove(self)
        Globals.window.blit(bread, (self.x, self.y))
