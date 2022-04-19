import pygame

from src.Globals import Globals
from src.Images import Images
from src.Injection import Injection


class Hygiene(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x, self.y = x, y
        self.rect = pygame.Rect(x, y, Globals.ICON_SIZE, Globals.ICON_SIZE)

    def update(self, mouse):
        if self.rect.collidepoint(mouse) and len(Globals.objs) == 0:
            Injection(77, 410)
            if Globals.HYGIENE + 10 >= 100:
                Globals.HYGIENE = 100
            else:
                Globals.HYGIENE += 10

    def draw(self):
        hygiene = pygame.transform.scale(Images.HYGIENE_IMAGE, (Globals.ICON_SIZE, Globals.ICON_SIZE))
        Globals.window.blit(hygiene, (self.rect.x, self.rect.y))
