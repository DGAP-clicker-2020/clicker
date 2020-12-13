from pygame.draw import *
from random import choice
from pygame import gfxdraw
import pygame
import os
import random

from settings import *
from ui import large_font
import ui
import music
import auxiliary_functions as func




class Target:
    def __init__(self,
                 x=WINDOW_WIDTH // 2,
                 y=WINDOW_HEIGHT // 2 + 20,
                 r=RADIUS + DR,
                 scale=1,
                 size_rect=target1_surf.get_rect(center=(250, 400)),
                 hp=10, ):
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
        self.scale = scale
        self.color = choice(COLORS)  # цвет
        self.max_hp = self.hp = hp  # максимальное начальное здоровье
        self.died = False  # флаг смерти
        self.kill_snd = music.kill_snd
        self.hit_snd = music.hit_snd
        self.crit_snd = music.crit_snd
        self.size_rect = size_rect
        self.pic = pic = choice(pics)
        self.size = pic

    def check_click(self, event):
        """
        Проверка клика по цели
        :rtype: bool
        :param event: pygame event
        :return: True или False в зависимости от попадания по цели
        """
        #if (event.pos[0] - self.x) ** 2 + (event.pos[1] - self.y) ** 2 < int(self.r) ** 2:

        if (event.pos[0] >= self.x - 100 + self.scale
                and event.pos[0] <= self.x + 100 - self.scale
                and event.pos[1] >= self.y - 150 + 1.5 * self.scale
                and event.pos[1] <= self.y + 150 - 1.5 * self.scale):

            self.hit_snd.play()
            return True

        else:
            return False

    def hurt(self, power, crit_chance, crit_multi):
        """
        Обрабатывает нанесение урона цели с учетом шанса крита
        :param power: сила урона
        :param crit_chance: шанс крита
        :param crit_multi: множитель урона
        """
        damage_txt = ui.render_outline('DAMAGE' + str(power), ui.pygame.font.Font(TERMINATOR_FONT_PATH, 13), RED, BLACK, 1)
        crit_txt = ui.render_outline('CRIT', ui.pygame.font.Font(TERMINATOR_FONT_PATH, 25), RED, BLACK, 1)
        chance = randint(0, 100)
        if chance >= crit_chance:
            self.hp -= power
            ui.screen.blit(damage_txt, (randint(300, 400), randint(300, 500)))
        else:
            self.hp -= power * crit_multi
            self.crit_snd.play()
            print('CRIT x' + str(crit_multi))
            ui.screen.blit(crit_txt, (200, 200))
        #self.r = RADIUS + DR * self.hp / self.max_hp
        self.scale += 1
        if self.scale <= 12:
            self.size = pygame.transform.scale(self.pic, (
            200 - 2*self.scale, 300 - 3*self.scale))
            self.size_rect = self.size.get_rect(center=(250, 400))

        self.check_died()

    def afk_hurt(self, power):  # добавил функцию отдельно, чтобы не учитывать криты и чтобы
                                                                            # объект уменьшался только когда его бьют
        """
        Обрабатывает нанесение афк урона цели
        :param power: сила урона

        """
        self.hp -= power
        #self.r = RADIUS + DR * self.hp / self.max_hp
        self.check_died()

    def check_died(self):
        """
        Проверяет, умерла ли цель
        """
        if self.hp <= 0:
            self.died = True
            self.kill_snd.play()

    def draw(self, surface):
        """
        Рисует цель на экране
        :param surface: экран
        """
        surface.blit(self.size, self.size_rect)
        #gfxdraw.aacircle(surface, int(self.x), int(self.y), int(self.r), self.color)  # сглаженный круг
        #gfxdraw.filled_circle(surface, int(self.x), int(self.y), int(self.r), self.color)
        self.draw_hp_bar(surface)

    def draw_hp_bar(self, surface):
        """
        Рисует хп бар на экране
        :param surface: экран
        """
        rect(surface, BLUE, (X_INDENT, Y_INDENT, HEALTH_BAR_WIDTH, HEALTH_BAR_HEIGHT), 5)

        green_factor = self.hp / self.max_hp
        red_factor = 1 - green_factor

        rect(surface, (255 * (red_factor if red_factor < 1 else 1),
                       255 * (green_factor if green_factor > 0 else 0), 0),
             (X_INDENT + 3, Y_INDENT + 3, (HEALTH_BAR_WIDTH - 3) * green_factor, HEALTH_BAR_HEIGHT - 6))

        hp_text_1 = large_font.render(func.to_fixed(self.hp + 1 if self.hp < 0.5 else self.hp), True, BLACK)
        hp_text_2 = large_font.render('/', True, BLACK)
        hp_text_3 = large_font.render(func.to_fixed(self.max_hp), True, BLACK)
        surface.blit(hp_text_1, (X_INDENT + (HEALTH_BAR_WIDTH - hp_text_2.get_width()) / 2 - hp_text_1.get_width(),
                                 Y_INDENT + (HEALTH_BAR_HEIGHT - hp_text_1.get_height()) / 2))
        surface.blit(hp_text_2, (X_INDENT + (HEALTH_BAR_WIDTH - hp_text_2.get_width()) / 2,
                                 Y_INDENT + (HEALTH_BAR_HEIGHT - hp_text_2.get_height()) / 2))
        surface.blit(hp_text_3, (X_INDENT + (HEALTH_BAR_WIDTH + hp_text_2.get_width()) / 2,
                                 Y_INDENT + (HEALTH_BAR_HEIGHT - hp_text_3.get_height()) / 2))


if __name__ == '__main__':
    print('This module is not for direct run!')
