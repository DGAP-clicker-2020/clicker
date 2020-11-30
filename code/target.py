from pygame.draw import *
from random import choice
from pygame import gfxdraw
from settings import *
from ui import large_font


def to_fixed(num_obj, digits=0):
    return f"{num_obj:.{digits}f}"


def calculate_hp(kills):
    return INITIAL_TARGET_HP + kills ** 1.5


class Target:
    def __init__(self,
                 x=window_width // 2,
                 y=window_height // 2 + 20,
                 r=RADIUS + DR,
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
        gfxdraw.aacircle(surface, int(self.x), int(self.y), int(self.r), self.color)  # сглаженный круг
        gfxdraw.filled_circle(surface, int(self.x), int(self.y), int(self.r), self.color)
        self.draw_hp_bar(surface)

    def draw_hp_bar(self, surface):
        """
        Рисует хп бар на экране
        :param surface: экран
        """
        rect(surface, BLUE, (X_INDENT, Y_INDENT, healthbar_width, healthbar_height), 5)

        green_factor = self.hp / self.max_hp
        red_factor = 1 - green_factor

        rect(surface, (255 * (red_factor if red_factor < 1 else 1),
                       255 * (green_factor if green_factor > 0 else 0), 0),
             (X_INDENT + 3, Y_INDENT + 3, healthbar_width * green_factor - 3, healthbar_height - 6))

        hp_text_1 = large_font.render(str(format(self.hp, '.0f')), True, BLACK)
        hp_text_2 = large_font.render('/', True, BLACK)
        hp_text_3 = large_font.render(str(format(self.max_hp, '.0f')), True, BLACK)
        surface.blit(hp_text_1, (X_INDENT + (healthbar_width - hp_text_2.get_width()) / 2 - hp_text_1.get_width(),
                                 Y_INDENT + (healthbar_height - hp_text_1.get_height()) / 2))
        surface.blit(hp_text_2, (X_INDENT + (healthbar_width - hp_text_2.get_width()) / 2,
                                 Y_INDENT + (healthbar_height - hp_text_2.get_height()) / 2))
        surface.blit(hp_text_3, (X_INDENT + (healthbar_width + hp_text_2.get_width()) / 2,
                                 Y_INDENT + (healthbar_height - hp_text_3.get_height()) / 2))


if __name__ == '__main__':
    print('This module is not for direct run!')
