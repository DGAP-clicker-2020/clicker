import pygame as pg
from pygame import mixer

pg.mixer.init()

bg_snd = pg.mixer.Sound('../sounds/Main.ogg')
purchase_snd = pg.mixer.Sound('../sounds/purchase.ogg')
hit_snd = pg.mixer.Sound('../sounds/hit.ogg')
kill_snd = pg.mixer.Sound('../sounds/death.ogg')
pick_snd = pg.mixer.Sound('../sounds/pick.ogg')


def back_sound():
    pg.mixer.music.load('../sounds/Main.ogg')
    bg_snd.play(-1, 0, 3000)
    mixer.music.set_volume(0.005)


if __name__ == '__main__':
    print('This module is not for direct run!')









