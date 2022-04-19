import pygame

from src.Button import Button
from src.DeathAngel import DeathAngel
from src.Func import score_menu, get_font
from src.Globals import Globals
from src.Images import Images


class Pet:
    def __init__(self, colour, x, y):
        self.x, self.y = x, y
        self.colour = colour
        self.delay = 0
        self.rect = pygame.Rect(x, y, 120, 150)
        self.delay_status = 0
        self.delay_age = 0
        self.rect = pygame.Rect(x, y, 80, 80)
        self.age_m = 0
        self.age_y = 0
        Globals.pets.append(self)

    def __change_status(self):
        if self.delay_status == Globals.FPS:
            Globals.HUNGER -= 1
            Globals.HYGIENE -= 1
            Globals.FUN -= 1
            if Globals.HUNGER <= 0 or Globals.FUN <= 0 or Globals.HYGIENE <= 0:
                if len(Globals.angels) == 0:
                    DeathAngel(250, 100)
                    DeathAngel(310, 100)
            self.delay_status = 0
        else:
            self.delay_status += 1

    def age(self):
        if self.delay_age == Globals.FPS / 2:
            self.age_m += 1
            if self.age_m == 12:
                self.age_m = 0
                self.age_y += 1
            self.delay_age = 0
            if self.age_y == 18:
                score_menu(1)
        else:
            self.delay_age += 1
        Month = Button(image=None, pos=(600, 235), text_input="M>", font=get_font(20),
                       base_color="#000000", hovering_color=None)
        M = str(self.age_m)
        Month_num = Button(image=None, pos=(632, 235), text_input=M, font=get_font(20),
                           base_color="#000000", hovering_color=None)
        Y = str(self.age_y)
        Year = Button(image=None, pos=(600, 210), text_input="Y>", font=get_font(20),
                      base_color="#000000", hovering_color=None)
        Year_num = Button(image=None, pos=(632, 210), text_input=Y, font=get_font(20),
                          base_color="#000000", hovering_color=None)
        for button in [Month, Year, Month_num, Year_num]:
            button.update(Globals.window)

    def draw(self):
        self.age()
        if self.colour == 'white':
            TOMA = Images.WHITE_TOMA_IMAGE
        elif self.colour == 'blue':
            TOMA = Images.BLUE_TOMA_IMAGE
        else:
            TOMA = Images.GREEN_TOMA_IMAGE
        if self.delay < Globals.FPS / 2:
            toma = pygame.transform.scale(TOMA[0], (120, 150))
            if TOMA != Images.WHITE_TOMA_IMAGE:
                toma.set_colorkey('white')
        else:
            toma = pygame.transform.scale(TOMA[1], (120, 150))
            if TOMA != Images.WHITE_TOMA_IMAGE:
                toma.set_colorkey('white')
        self.delay += 1
        if self.delay == Globals.FPS:
            self.delay = 0
        self.__change_status()
        Globals.window.blit(toma, (self.x, self.y))