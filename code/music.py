from pygame import mixer
from settings import *

mixer.init()

bg_snd = mixer.Sound(os.path.join('..', 'sounds', 'Main.ogg'))
matreshka_snd = mixer.Sound(os.path.join('..', 'sounds', 'matreshka.ogg'))
purchase_snd = mixer.Sound(os.path.join('..', 'sounds', 'purchase.ogg'))
hit_snd = mixer.Sound(os.path.join('..', 'sounds', 'hit.ogg'))
kill_snd = mixer.Sound(os.path.join('..', 'sounds', 'death.ogg'))
pick_snd = mixer.Sound(os.path.join('..', 'sounds', 'pick.ogg'))


if __name__ == '__main__':
    print('This module is not for direct run!')
