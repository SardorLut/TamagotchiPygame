import pygame

from src.Globals import Globals
from src.Images import Images
from src.Injection import Injection


class Hygiene(pygame.sprite.Sprite):
    """Иконка гигиены на экране, при нажатии увеличить гигиену питомца питомца"""
    def __init__(self, x, y):
        """Инициализации иконки на экране, его положение"""
        pygame.sprite.Sprite.__init__(self)
        self.x, self.y = x, y
        self.rect = pygame.Rect(x, y, Globals.ICON_SIZE, Globals.ICON_SIZE)

    def update(self, mouse):
        """При нажатии на иконку гигиены, сделать укол питомцу"""
        if self.rect.collidepoint(mouse) and len(Globals.objs) == 0:
            Injection(77, 410)
            if Globals.HYGIENE + 10 >= 100:
                Globals.HYGIENE = 100
            else:
                Globals.HYGIENE += 10

    def draw(self):
        """Отрисовать на экране иконку"""
        hygiene = pygame.transform.scale(Images.HYGIENE_IMAGE, (Globals.ICON_SIZE, Globals.ICON_SIZE))
        Globals.window.blit(hygiene, (self.rect.x, self.rect.y))
