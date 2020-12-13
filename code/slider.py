import pygame
from typing import Tuple


class Slider:
    def __init__(
            self,
            surface: pygame.surface.Surface,
            x: int,
            y: int,
            width=0,
            height=0,
            thin=0,
            color: Tuple[int] = None,
            color_ext: Tuple[int] = None,
            player=None
    ):
        """
        Сборщик класса Slider
        :param surface: поверхность для прорисовки
        :param x: координата x левого конца слайдера
        :param y: координата y левого конца слайдера
        :param width: ширина слайдера
        :param height: высота слайдера
        :param thin: толщина полосочки слайдера
        :param color: цвет ползунка
        :param color_ext: цвет полосочки
        :param player: игрок
        """
        self.surface = surface
        self.x = x
        self.y = y
        self.thin = thin
        self.width = width
        self.height = height
        self.color = color or (224, 224, 224)
        self.color_ext = color_ext
        self.player = player
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.slide_x = self.x + self.player.audio_volume / 100 * self.width
        self.slide_y = self.y + self.height // 2

    def draw(self):
        """
        Метод отвечает за прорисовку слайдера
        """
        self.handle_event()
        self.player.audio_volume = int((self.slide_x - self.x) / self.width * 100)

        radius = self.height
        pygame.draw.rect(self.surface, self.color_ext, [self.x - 1, self.y + 1, self.width + 2, self.thin + 2])

        pygame.draw.rect(self.surface, (139, 0, 255), [self.x, self.y + (self.height - self.thin) // 2,
                                                       self.slide_x - self.x, self.thin])
        pygame.draw.rect(self.surface, (128, 128, 128), [self.slide_x, self.y + (self.height - self.thin) // 2,
                                                         self.width - (self.slide_x - self.x), self.thin])

        pygame.gfxdraw.aacircle(self.surface, int(self.slide_x), int(self.slide_y), radius + 1, self.color_ext)
        pygame.gfxdraw.filled_circle(self.surface, int(self.slide_x), int(self.slide_y), radius + 1, self.color_ext)
        pygame.gfxdraw.aacircle(self.surface, int(self.slide_x), int(self.slide_y), radius, self.color)
        pygame.gfxdraw.filled_circle(self.surface, int(self.slide_x), int(self.slide_y), radius, self.color)

    def handle_event(self):
        """
        Обработчик событий слайдера
        """
        if pygame.mouse.get_pressed()[0] == 1 and self.rect.collidepoint(pygame.mouse.get_pos()):
            self.slide_x = pygame.mouse.get_pos()[0]
            if self.slide_x < self.x:
                self.slide_x = self.x
            if self.slide_x > self.x + self.width:
                self.slide_x = self.x + self.width


if __name__ == '__main__':
    print('This module is not for direct run!')
