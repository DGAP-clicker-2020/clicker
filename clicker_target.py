from pygame.draw import *
import pygame

from clicker_settings import *
from clicker_ui import lower_font, large_font


def to_fixed(num_obj, digits=0):
    return f"{num_obj:.{digits}f}"


class Target:
    def __init__(self,
                 x=window_width // 2,
                 y=window_height // 2 + 20,
                 r=RADIUS + DR,
                 hp=10,):
        """
        Сборщик класса Target
        :param x: координата центра x
        :param y: координата центра y
        :param r: радиус цели
        :param hp: здоровье цели
        """
        self.x = x
        self.y = y
        self.r = r
        self.color = choice(COLORS)  # цвет
        self.max_hp = self.hp = hp  # максимальное начальное здоровье
        self.died = False  # флаг смерти

    def check_click(self, event):
        """
        Проверка клика по цели
        :rtype: bool
        :param event: pygame event
        :return: True или False в зависимости от попадания по цели
        """
        if (event.pos[0] - self.x) ** 2 + (event.pos[1] - self.y) ** 2 < int(self.r) ** 2:
            return True
        else:
            return False

    def hurt(self, power):
        """
        Обрабатывает нанесение урона цели
        :param power: сила урона
        """

        self.hp -= power
        self.r = RADIUS + DR * self.hp / self.max_hp
        self.check_died()

    def check_died(self):
        """
        Проверяет, умерла ли цель
        """
        if self.hp <= 0:
            self.died = True

    def draw(self, surface):
        """
        Рисует цель на экране
        :param surface: экран
        """
        circle(surface, self.color, (self.x, self.y), int(self.r))
        self.draw_hp_bar(surface)

    def draw_hp_bar(self, surface):
        """
        Рисует хп бар на экране
        :param surface: экран
        """
        rect(surface, BLUE, (0 + X_INDENT, 0 + Y_INDENT, healthbar_width, healthbar_height), 5)

        green_factor = self.hp / self.max_hp
        red_factor = 1 - green_factor

        rect(surface, (255 * (red_factor if red_factor < 1 else 1),
                       255 * (green_factor if green_factor > 0 else 0), 0),
             (X_INDENT, Y_INDENT, healthbar_width * green_factor, healthbar_height))

        hp_text = large_font.render(str(to_fixed(self.hp, 0))+'/'+str(self.max_hp), 0, BLACK)
        surface.blit(hp_text, (healthbar_width // 3, healthbar_height // 2 - 10))


def draw_back_picture(name, surface):
    """рисует задний фон
    type name(названия файла): string"""
    surface.blit(pygame.image.load(name), (0, 0, window_width, window_height))


if __name__ == '__main__':
    print('This module is not for direct run!')
