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
            Injection(x=77, y=410)
            max = 100
            get = 10
            if Globals.HYGIENE + get >= max:
                Globals.HYGIENE = max
            else:
                Globals.HYGIENE += get

    def draw(self):
        """Отрисовать на экране иконку"""
        hygiene = pygame.transform.scale(Images.HYGIENE_IMAGE, (Globals.ICON_SIZE, Globals.ICON_SIZE))
        Globals.window.blit(hygiene, (self.rect.x, self.rect.y))
