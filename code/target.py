from pygame.draw import *
from random import choice, randint

from settings import *
from ui import large_font
import ui
import music
import auxiliary_functions as func


class DamageText:
    def __init__(self,
                 text_info,
                 power,
                 x=randint(300, 400),
                 y=randint(300, 500),
                 color=RED,
                 font=TERMINATOR_FONT_PATH,
                 scale=13,
                 ):
        """
        Сборщик класса DamageText
        :param text_info: информация в надписи
        :param power: сила урона
        :param x: координата x
        :param y: координата y
        :param color: цвет
        :param font: шрифт
        :param scale: размер текста
        """
        self.text_info = text_info
        self.power = power
        self.x = x
        self.y = y
        self.color = color
        self.font = font
        self.scale = scale
        self.count = 0
        self.die = False

        if self.power == 'crit':
            self.text = ui.render_outline(self.text_info,
                                          ui.pygame.font.Font(TERMINATOR_FONT_PATH, 30), self.color, BLACK, 1)
            self.x = 160
            self.y = 200

        elif self.text_info is not None:
            self.text = ui.render_outline(self.text_info + ' ' + str(self.power),
                                          ui.pygame.font.Font(TERMINATOR_FONT_PATH, 13), self.color, BLACK, 1)
        else:
            self.text = ui.render_outline('', ui.pygame.font.Font(TERMINATOR_FONT_PATH, 13),
                                          self.color, BLACK, 1)

    def draw(self):
        if not self.die:
            ui.screen.blit(self.text, (self.x, self.y))
            self.count += 1
            self.check_die()

    def check_die(self):
        if self.count >= 120:
            self.die = True


class Target:
    def __init__(self,
                 x=WINDOW_WIDTH // 2,
                 y=WINDOW_HEIGHT // 2 + 20,
                 r=RADIUS + DR,
                 scale=1,
                 size_rect=target1_surf.get_rect(center=(250, 400)),
                 hp=10,
                 ):
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
        self.damage_text = DamageText(None, None)

    def check_click(self, event):
        """
        Проверка клика по цели
        :rtype: bool
        :param event: pygame event
        :return: True или False в зависимости от попадания по цели
        """
        if (
                self.x - 100 + round(12 * self.scale / (12 + self.scale))
                <= event.pos[0] <=
                self.x + 100 - round(12 * self.scale / (12 + self.scale))
                and
                self.y - 150 + round(18 * self.scale / (12 + self.scale))
                <= event.pos[1] <=
                self.y + 150 - round(18 * self.scale / (12 + self.scale))
        ):
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
        chance = randint(0, 100)
        if chance >= crit_chance:
            self.hp -= power
            self.damage_text = DamageText('DAMAGE', power, x=randint(100, 300), y=randint(300, 600))
        else:
            self.hp -= power * crit_multi
            self.crit_snd.play()
            self.damage_text = DamageText('CRIT x' + str(crit_multi), 'crit')
        self.scale += 1
        self.size = pygame.transform.scale(self.pic, (
            200 - round(24 * self.scale / (12 + self.scale)), 300 - round(36 * self.scale / (12 + self.scale))))
        self.size_rect = self.size.get_rect(center=(250, 400))

        self.check_died()

    def afk_hurt(self, power):
        """
        Обрабатывает нанесение афк урона цели
        :param power: сила урона

        """
        self.hp -= power
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
