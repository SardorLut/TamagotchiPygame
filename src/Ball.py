from src.Globals import Globals
import pygame
from src.Images import Images
class Ball:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.frame = 0
        Globals.balls.append(self)
        Globals.objs.append(self)
        self.stop = 60
        self.delay = 0

    def draw(self):
        ball = pygame.transform.scale(Images.BALL_IMAGE, (40, 40))
        self.delay += 1
        if self.delay == self.stop:
            Globals.objs.remove(self)
            Globals.balls.remove(self)
        if self.delay <= self.stop / 2:
            self.y -= 9.5
        else:
            self.y += 9.5
        Globals.window.blit(ball, (self.x, self.y))
