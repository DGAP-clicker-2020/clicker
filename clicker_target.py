# classes specification module

from pygame.draw import *
from random import choice

from clicker_settings import *


class Target:
    def __init__(self,
                 x=window_width // 2,
                 y=window_height // 2 + 20,
                 r=RADIUS + DR,
                 hp=10,):
        self.x = x
        self.y = y
        self.r = r
        self.color = choice(COLORS)
        self.max_hp = self.hp = hp
        self.died = False

    def check_click(self, event):
        if (event.pos[0] - self.x) ** 2 + (event.pos[1] - self.y) ** 2 < int(self.r) ** 2:
            return True
        else:
            return False

    def click_hurt(self, power):
        self.hp -= power
        self.r = RADIUS + DR * self.hp / self.max_hp
        self.check_died()

    def afk_hurt(self, power):
        self.hp -= power
        self.r = RADIUS + DR * self.hp / self.max_hp
        self.check_died()

    def check_died(self):
        if self.hp <= 0:
            self.died = True

    def draw(self, surface):
        circle(surface, self.color, (self.x, self.y), int(self.r))
        self.draw_hp_bar(surface)

    def draw_hp_bar(self, surface):
        rect(surface, BLUE, (0 + X_INDENT, 0 + Y_INDENT, healthbar_width, healthbar_height), 5)

        green_factor = self.hp / self.max_hp
        red_factor = 1 - green_factor

        rect(surface, (255 * (red_factor if red_factor < 1 else 1),
                       255 * (green_factor if green_factor > 0 else 0), 0),
             (X_INDENT, Y_INDENT, healthbar_width * green_factor, healthbar_height))


if __name__ == '__main__':
    print('This module is not for direct run!')
