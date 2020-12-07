from pygame import mixer
from settings import *

mixer.init()

bg_snd = mixer.Sound(os.path.join('..', 'sounds', 'Main.ogg'))
purchase_snd = mixer.Sound(os.path.join('..', 'sounds', 'purchase.ogg'))
hit_snd = mixer.Sound(os.path.join('..', 'sounds', 'hit.ogg'))
kill_snd = mixer.Sound(os.path.join('..', 'sounds', 'death.ogg'))
pick_snd = mixer.Sound(os.path.join('..', 'sounds', 'pick.ogg'))


def back_sound():
    bg_snd.play(-1, 0, 3000)


if __name__ == '__main__':
    print('This module is not for direct run!')
