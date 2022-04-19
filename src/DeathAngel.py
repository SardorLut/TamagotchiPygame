import pygame

from src.Globals import Globals
from src.Images import Images


class DeathAngel:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.rect = pygame.Rect(x, y, Globals.ICON_SIZE, Globals.ICON_SIZE)
        Globals.angels.append(self)
        Globals.objs.append(self)

    def update(self):
        from src.Func import score_menu
        self.rect.y += 1
        for pet in Globals.pets:
            if self.rect.colliderect(pet.rect):
                Globals.objs.remove(self)
                Globals.angels.remove(self)
                score_menu(0)

    def draw(self):
        angel = pygame.transform.scale(Images.ANGEL_IMAGE, (Globals.ICON_SIZE, Globals.ICON_SIZE))
        Globals.window.blit(angel, (self.rect.x, self.rect.y))
