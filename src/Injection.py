import pygame

from src.Globals import Globals
from src.Images import Images


class Injection:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.frame = 0
        Globals.injections.append(self)
        Globals.objs.append(self)
        self.stop = 60
        self.delay = 0

    def draw(self):
        inject = pygame.transform.scale(Images.INJECT_IMAGE, (200, 30))
        self.delay += 1
        if self.delay == self.stop:
            Globals.objs.remove(self)
            Globals.injections.remove(self)
        Globals.window.blit(inject, (self.x, self.y))
