import sys

import pygame

from src.Button import Button
from src.Eating import Eating
from src.Egg import Egg
from src.Fun import Fun
from src.Globals import Globals
from src.Hygiene import Hygiene
from src.Images import Images

pygame.init()
clock = pygame.time.Clock()


def get_font(size):
    return pygame.font.Font("font/font.ttf", size)


def ui():
    """Пользовательский интерфейс"""
    x_bar, y_bar = 124, 24
    bar_sht_size_x, bar_sht_size_y = 11, 8
    bar = pygame.transform.scale(Images.BAR, (x_bar, y_bar))
    bar_sht = pygame.transform.scale(Images.BAR_SHT, (bar_sht_size_x, bar_sht_size_y))
    hygiene_x, hygiene_y = 300, 20
    hunger_x, hunger_y = 120, 20
    fun_x, fun_y = 480, 20
    hygiene = Button(image=None, pos=(hygiene_x, hygiene_y), text_input="HYGIENE", font=get_font(16),
                     base_color="#000000", hovering_color=None)
    hunger = Button(image=None, pos=(hunger_x, hunger_y), text_input="HUNGER", font=get_font(16),
                    base_color="#000000", hovering_color=None)
    fun = Button(image=None, pos=(fun_x, fun_y), text_input="FUN", font=get_font(16),
                 base_color="#000000", hovering_color=None)
    for i in range(3):
        x = 56 + 180 * i
        y = 40
        Globals.window.blit(bar, (x, y))
    for i in range(int(Globals.HUNGER / 10)):
        x = 62 + 11 * i
        y = 48
        Globals.window.blit(bar_sht, (x, y))
    for i in range(int(Globals.HYGIENE / 10)):
        x = 242 + 11 * i
        y = 48
        Globals.window.blit(bar_sht, (x, y))
    for i in range(int(Globals.FUN / 10)):
        x = 422 + 11 * i
        y = 48
        Globals.window.blit(bar_sht, (x, y))
    for button in [hunger, hygiene, fun]:
        button.update(Globals.window)


def draw_border():
    """Нарисовать экранчик для питомца"""
    x, y = 0, -50
    border = pygame.transform.scale(Images.BORDER, (Globals.HEIGHT, Globals.WIDTH))
    Globals.window.blit(border, (x, y))


def del_all():
    """Сбросить все"""
    Globals.pets = []
    Globals.angels = []
    Globals.objs = []
    Globals.HUNGER = 50
    Globals.FUN = 50
    Globals.HYGIENE = 50


def game(colour):
    """Основной game loop"""
    del_all()
    play = True
    Egg(colour, x=250, y=330)
    eat = Eating(x=80, y=530)
    hygiene = Hygiene(x=250, y=530)
    fun = Fun(x=410, y=530)
    all_icons = pygame.sprite.Group()
    all_icons.add(eat, hygiene, fun)
    while play:
        Globals.window.fill(Globals.BG_COLOR)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for icon in all_icons:
                    icon.update(event.pos)
        draw_border()
        eat.draw()
        hygiene.draw()
        fun.draw()
        for obj in Globals.objs:
            obj.draw()
        for angel in Globals.angels:
            angel.update()
        for pet in Globals.pets:
            pet.draw()
        ui()
        pygame.display.update()
        clock.tick(Globals.FPS)


def score_menu(stat):
    """Экран статистики"""
    while True:
        Globals.window.fill(Globals.BG_COLOR)
        menu_mouse_pos = pygame.mouse.get_pos()
        if stat:
            res = Button(image=None, pos=(350, 50),
                         text_input="YOU WIN!!!", font=get_font(70), base_color="#030801", hovering_color=None)
        else:
            res = Button(image=None, pos=(350, 50),
                         text_input="YOU LOSE", font=get_font(70), base_color="#030801", hovering_color=None)
        quit_button = Button(image=None, pos=(350, 300),
                             text_input="QUIT", font=get_font(50), base_color="#030801", hovering_color="White")
        menu = Button(image=None, pos=(350, 200),
                      text_input="BACK TO MENU", font=get_font(50), base_color="#030801", hovering_color="White")
        res.update(Globals.window)
        for button in [menu, quit_button]:
            button.change_color(menu_mouse_pos)
            button.update(Globals.window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu.check_for_input(menu_mouse_pos):
                    main_menu()
                if quit_button.check_for_input(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()


def main_menu():
    """Главное меню"""
    while True:
        Globals.window.fill(Globals.BG_COLOR)
        menu_mouse_pos = pygame.mouse.get_pos()

        menu_text = get_font(30).render("MAIN MENU", True, "#000000")
        menu_rect = menu_text.get_rect(center=(350, 30))

        play = Button(image=None, pos=(350, 100),
                      text_input="PLAY", font=get_font(40), base_color="#030801", hovering_color="White")
        quit_button = Button(image=None, pos=(350, 180),
                             text_input="QUIT", font=get_font(40), base_color="#030801", hovering_color="White")

        Globals.window.blit(menu_text, menu_rect)

        for button in [play, quit_button]:
            button.change_color(menu_mouse_pos)
            button.update(Globals.window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play.check_for_input(menu_mouse_pos):
                    pet_menu()
                if quit_button.check_for_input(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()


def pet_menu():
    """Экран выбора питомца"""
    while True:
        Globals.window.fill(Globals.BG_COLOR)
        menu_mouse_pos = pygame.mouse.get_pos()

        white_toma = Button(image=None, pos=(100, 250),
                            text_input="Mametchi", font=get_font(20), base_color="#030801", hovering_color="White")
        blue_toma = Button(image=None, pos=(350, 250),
                           text_input="Gozarutchi", font=get_font(20), base_color="#030801", hovering_color="White")
        green_toma = Button(image=None, pos=(600, 250),
                            text_input="Lovelitchi", font=get_font(20), base_color="#030801", hovering_color="White")
        for button in [white_toma, blue_toma, green_toma]:
            button.change_color(menu_mouse_pos)
            button.update(Globals.window)
        height, width = 120, 150
        x_1, y_1 = 40, 80
        x_2, y_2 = 280, 80
        x_3, y_3 = 520, 80
        white = pygame.transform.scale(Images.WHITE_TOMA_IMAGE[2], (height, width))
        Globals.window.blit(white, (x_1, y_1))
        blue = pygame.transform.scale(Images.BLUE_TOMA_IMAGE[2], (height, width))
        blue.set_colorkey('white')
        Globals.window.blit(blue, (x_2, y_2))
        green = pygame.transform.scale(Images.GREEN_TOMA_IMAGE[2], (height, width))
        green.set_colorkey('white')
        Globals.window.blit(green, (x_3, y_3))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if white_toma.check_for_input(menu_mouse_pos):
                    game('white')
                if blue_toma.check_for_input(menu_mouse_pos):
                    game('blue')
                if green_toma.check_for_input(menu_mouse_pos):
                    game('green')
        pygame.display.update()
