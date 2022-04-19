import pygame


class Globals:
    # переменные
    WIDTH, HEIGHT = 700, 600
    FPS = 30
    BG_COLOR = (160, 180, 130)
    FUN = 50
    HUNGER = 50
    HYGIENE = 50
    ICON_SIZE = 48
    FOOD_SIZE = 100
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    # списки
    eggs = []
    pets = []
    breads = []
    injections = []
    objs = []
    balls = []
    angels = []
