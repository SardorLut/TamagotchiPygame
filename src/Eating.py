import pygame

from src.Bread import Bread
from src.Globals import Globals
from src.Images import Images


class Eating(pygame.sprite.Sprite):
    """Иконка еды на экране, при нажатии накормить питомца"""
    def __init__(self, x, y):
        """Инициализации иконки на экране, его положение"""
        pygame.sprite.Sprite.__init__(self)
        self.x, self.y = x, y
        self.rect = pygame.Rect(x, y, Globals.ICON_SIZE, Globals.ICON_SIZE)

    def update(self, mouse):
        """При нажатии на иконку еды, накормить питомца"""
        if self.rect.collidepoint(mouse) and len(Globals.objs) == 0:
            Bread(350, 150)
            if Globals.HUNGER + 10 >= 100:
                Globals.HUNGER = 100
            else:
                Globals.HUNGER += 10

    def draw(self):
        """Отрисовать иконку еды на экране"""
        eating = pygame.transform.scale(Images.EATING_IMAGE, (Globals.ICON_SIZE, Globals.ICON_SIZE))
        Globals.window.blit(eating, (self.rect.x, self.rect.y))
