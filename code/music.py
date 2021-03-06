from pygame import mixer
from settings import *

mixer.init()

def_snd = mixer.Sound(os.path.join('..', 'sounds', 'Main.ogg'))
matreshka_snd = mixer.Sound(os.path.join('..', 'sounds', 'matreshka.ogg'))
minecraft_1_snd = mixer.Sound(os.path.join('..', 'sounds', 'Mc1.ogg'))
minecraft_2_snd = mixer.Sound(os.path.join('..', 'sounds', 'Mc2.ogg'))
purchase_snd = mixer.Sound(os.path.join('..', 'sounds', 'purchase.ogg'))
hit_snd = mixer.Sound(os.path.join('..', 'sounds', 'hit.ogg'))
kill_snd = mixer.Sound(os.path.join('..', 'sounds', 'death.ogg'))
pick_snd = mixer.Sound(os.path.join('..', 'sounds', 'pick.ogg'))
crit_snd = mixer.Sound(os.path.join('..', 'sounds', 'sword.ogg'))

all_sounds = [
    def_snd,
    matreshka_snd,
    purchase_snd,
    hit_snd, kill_snd,
    minecraft_1_snd,
    minecraft_2_snd,
    pick_snd,
    crit_snd,
]

all_music = {5: def_snd, 6: minecraft_1_snd, 7: minecraft_2_snd, 8: matreshka_snd}


def set_all_volume(sounds, mult):
    for sound in sounds:
        sound.set_volume(mult/100)


if __name__ == '__main__':
    print('This module is not for direct run!')
