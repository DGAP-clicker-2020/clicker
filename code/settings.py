import os
import pygame
from random import randint

FPS = 60

DEBUG_FLAG = False

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 750

NOT_ENOUGH_MONEY_COLOR = (128, 128, 128)
ENOUGH_MONEY_COLOR = DEFAULT_BUTTON_COLOR = (51, 153, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (31, 168, 31)
ORANGE = (241, 178, 64)
GRAY = (191, 191, 191)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
GOLD = (255, 215, 0)

COLORS = [RED, BLUE, GREEN, ORANGE, GRAY, YELLOW, WHITE, CYAN]

RADIUS = 80  # минимальный радиус цели
DR = 40  # возможное изменение радиуса цели

X_INDENT = 20  # отступ хп бара по x
Y_INDENT = 7  # отступ хп бара по y
HEALTH_BAR_WIDTH = WINDOW_WIDTH - 2 * X_INDENT
HEALTH_BAR_HEIGHT = 100

INITIAL_TARGET_HP = 10
TARGET_HP_MULTIPLIER = 6

HAND_POWER_BONUS = 0.2
AFK_POWER_BONUS = 0.1

TERMINATOR_FONT_PATH = os.path.join('..', 'fonts', 'terminator.ttf')
SONICBT_FONT_PATH = os.path.join('..', 'fonts', 'SonicBT.otf')

BACK_PICTURES = ['kpm_1.jpg', 'bio_1.jpg', 'nk_1.jpg', 'mipt_logo.jpg', 'KSP.jpg']  # массив с названием картинок заднего фона

SHOP_BACK_PICTURES = {num + 7: pic for num, pic in enumerate(BACK_PICTURES)}

BACK_PICTURES = {pic: os.path.join('..', 'back_pictures', pic) for pic in BACK_PICTURES}

target1_surf = pygame.image.load(os.path.join('..', 'target_pics', 'fizika.jpg'))
target2_surf = pygame.image.load(os.path.join('..', 'target_pics', 'animatronik.jpg'))
target3_surf = pygame.image.load(os.path.join('..', 'target_pics', 'matan1.jpg'))
target4_surf = pygame.image.load(os.path.join('..', 'target_pics', 'analit.jpg'))
target5_surf = pygame.image.load(os.path.join('..', 'target_pics', 'labnik.jpg'))

pics = [target1_surf, target2_surf, target3_surf, target4_surf, target5_surf]
target1_rect = target1_surf.get_rect(center=(250, 400))

if __name__ == '__main__':
    print('This module is not for direct run!')
