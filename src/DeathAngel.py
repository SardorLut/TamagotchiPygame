from __future__ import annotations
import pygame
from src.Globals import Globals
from src.Images import Images
import src.Func


class DeathAngel:
    """Появление ангела при окончании игры"""
    def __init__(self, x, y):
        """Инициализация ангела, его координаты"""
        self.score_menu = src.Func.score_menu
        self.x, self.y = x, y
        self.rect = pygame.Rect(x, y, Globals.ICON_SIZE, Globals.ICON_SIZE)
        Globals.angels.append(self)
        Globals.objs.append(self)

    def update(self):
        """
        Изменить положение ангела на экране,
        при столкновении с питомцем закончить игру
        """
        self.rect.y += 1
        for pet in Globals.pets:
            if self.rect.colliderect(pet.rect):
                Globals.objs.remove(self)
                Globals.angels.remove(self)
                self.score_menu(0)

    def draw(self):
        """Отрисовать на экране ангела"""
        angel = pygame.transform.scale(Images.ANGEL_IMAGE, (Globals.ICON_SIZE, Globals.ICON_SIZE))
        Globals.window.blit(angel, (self.rect.x, self.rect.y))
