from pygame import mixer
from settings import *

mixer.init()

bg_snd = mixer.Sound('../sounds/Main.ogg')
purchase_snd = mixer.Sound('../sounds/purchase.ogg')
hit_snd = mixer.Sound('../sounds/hit.ogg')
kill_snd = mixer.Sound('../sounds/death.ogg')
pick_snd = mixer.Sound('../sounds/pick.ogg')


def back_sound():
    mixer.music.load('../sounds/Main.ogg')
    bg_snd.play(-1, 0, 3000)
    mixer.music.set_volume(snd_volume)


if __name__ == '__main__':
    print('This module is not for direct run!')









