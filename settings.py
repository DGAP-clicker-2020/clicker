import os

FPS = 60

window_width = 500
window_height = 750

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (31, 168, 31)
ORANGE = (241, 178, 64)
GRAY = (191, 191, 191)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)

COLORS = [RED, BLUE, GREEN, ORANGE, GRAY, YELLOW, WHITE, CYAN]

RADIUS = 80  # минимальный радиус цели
DR = 40  # возможное изменение радиуса цели

X_INDENT = 20  # отступ хп бара по x
Y_INDENT = 7  # отступ хп бара по y
healthbar_width = window_width - 2 * X_INDENT
healthbar_height = 100

INITIAL_TARGET_HP = 10
TARGET_HP_MULTIPLIER = 6

HAND_POWER_BONUS = 1
AFK_POWER_BONUS = 0.5

back_pictures = ['kpm_1.jpg', 'nk_1.jpg', 'bio_1.jpg']  # массив с названием картинок заднего фона

for i, pic in enumerate(back_pictures):
    back_pictures[i] = os.path.join('back_pictures', pic)  # нормальный путь к файлам картинок

if __name__ == '__main__':
    print('This module is not for direct run!')
