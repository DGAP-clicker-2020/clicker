# classes specification module

import pygame
from pygame.draw import *
from random import choice

from clicker_settings import *


class Target:
    def __init__(self,
                 x=window_width // 2,
                 y=window_height // 2 + 20,
                 r=50,
                 hp=30,):
        self.x = x
        self.y = y
        self.r = r
        self.color = choice(COLORS)
        self.hp = hp
        self.died = False

    def check_click(self, event):
        if (event.pos[0] - self.x) ^ 2 + (event.pos[1] - self.y) ^ 2 < self.r:
            return True
        else:
            return False

    def hurt(self, power):
        self.hp -= power
        self.check_died()

    def check_died(self):
        if self.hp <= 0:
            self.died = True

    def draw(self, surface):
        circle(surface, self.color, (self.x, self.y), self.r)
