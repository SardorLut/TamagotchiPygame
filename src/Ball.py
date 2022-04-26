import pygame

from src.Globals import Globals
from src.Images import Images


class Ball:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.frame = 0
        Globals.objs.append(self)
        self.stop = 60
        self.delay = 0

    def draw(self):
        ball = pygame.transform.scale(Images.BALL_IMAGE, (40, 40))
        self.delay += 1
        if self.delay == self.stop:
            Globals.objs.remove(self)
        speed_of_balloon = 9.5
        if self.delay <= self.stop / 2:
            self.y -= speed_of_balloon
        else:
            self.y += speed_of_balloon
        Globals.window.blit(ball, (self.x, self.y))
