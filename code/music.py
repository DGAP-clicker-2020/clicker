from pygame import mixer
from settings import *

mixer.init()

bg_snd = mixer.Sound(os.path.join('..', 'sounds', 'Main.ogg'))
matreshka_snd = mixer.Sound(os.path.join('..', 'sounds', 'matreshka.ogg'))
purchase_snd = mixer.Sound(os.path.join('..', 'sounds', 'purchase.ogg'))
hit_snd = mixer.Sound(os.path.join('..', 'sounds', 'hit.ogg'))
kill_snd = mixer.Sound(os.path.join('..', 'sounds', 'death.ogg'))
pick_snd = mixer.Sound(os.path.join('..', 'sounds', 'pick.ogg'))

all_sounds = [bg_snd, matreshka_snd, purchase_snd, hit_snd, kill_snd, pick_snd]


def set_all_volume(sounds, mult):
    for sound in sounds:
        vol = sound.get_volume()
        sound.set_volume(min(vol * mult / 100, 1.0))


if __name__ == '__main__':
    print('This module is not for direct run!')
