import os

import pygame


class Images:
    BORDER = pygame.image.load("assets/border.png").convert_alpha()
    WHITE_TOMA_IMAGE = [pygame.image.load(os.path.join('assets', 'toma_1.png')),
                        pygame.image.load(os.path.join('assets', 'toma_2.png')),
                        pygame.image.load(os.path.join('assets', 'toma_3.png'))]
    GREEN_TOMA_IMAGE = [pygame.image.load(os.path.join('assets', 'GreenToma_1.png')),
                        pygame.image.load(os.path.join('assets', 'GreenToma_2.png')),
                        pygame.image.load(os.path.join('assets', 'GreenToma_3.png'))]
    BLUE_TOMA_IMAGE = [pygame.image.load(os.path.join('assets', 'BlueToma_1.png')),
                       pygame.image.load(os.path.join('assets', 'BlueToma_2.png')),
                       pygame.image.load(os.path.join('assets', 'BlueToma_3.png'))]
    EGG_IMAGE = [pygame.image.load(os.path.join('assets', 'egg_1.png')),
                 pygame.image.load(os.path.join('assets', 'egg_2.png')),
                 pygame.image.load(os.path.join('assets', 'egg_3.png')),
                 pygame.image.load(os.path.join('assets', 'egg_4.png')),
                 pygame.image.load(os.path.join('assets', 'egg_5.png'))]
    BAR = pygame.image.load(os.path.join('assets', 'bar.png'))
    BAR_SHT = pygame.image.load(os.path.join('assets', 'bar_sht.png'))
    EATING_IMAGE = pygame.image.load(os.path.join('assets', 'eating.png'))
    BREAD_IMAGE = [pygame.image.load(os.path.join('assets', 'bread_1.png')),
                   pygame.image.load(os.path.join('assets', 'bread_2.png')),
                   pygame.image.load(os.path.join('assets', 'bread_3.png')),
                   pygame.image.load(os.path.join('assets', 'bread_4.png')),
                   pygame.image.load(os.path.join('assets', 'bread_5.png')),
                   pygame.image.load(os.path.join('assets', 'bread_6.png'))]
    HYGIENE_IMAGE = pygame.image.load(os.path.join('assets', 'hygiene.png'))
    INJECT_IMAGE = pygame.image.load(os.path.join('assets', 'inject.png'))
    FUN_IMAGE = pygame.image.load(os.path.join('assets', 'fun.png'))
    BALL_IMAGE = pygame.image.load(os.path.join('assets', 'ball.png'))
    ANGEL_IMAGE = pygame.image.load(os.path.join('assets', 'death_angel.png'))
