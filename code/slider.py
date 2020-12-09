import pygame
from typing import Tuple


def slider_draw(surface, x, y, width, height, color, color_ext, slide_x, slide_y, thin):

    radius = height
    pygame.draw.rect(surface, color_ext, [x - 1, y + 1, width + 2, thin + 2])
    pygame.draw.rect(surface, (139, 0, 255), [x, y + (height - thin) // 2, slide_x - x, thin])
    pygame.draw.rect(surface, (128, 128, 128), [slide_x, y + (height - thin) // 2,  width - (slide_x - x), thin])

    pygame.gfxdraw.aacircle(surface, int(slide_x), int(slide_y), radius + 1, color_ext)
    pygame.gfxdraw.filled_circle(surface, int(slide_x), int(slide_y), radius + 1, color_ext)
    pygame.gfxdraw.aacircle(surface, int(slide_x), int(slide_y), radius, color)
    pygame.gfxdraw.filled_circle(surface, int(slide_x), int(slide_y), radius, color)


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
        self.handle_event()
        self.player.audio_volume = int((self.slide_x - self.x) / self.width * 100)
        slider_draw(self.surface, self.x, self.y,  self.width, self.height, self.color, self.color_ext, self.slide_x,
                    self.slide_y, self.thin)

    def handle_event(self):
        if pygame.mouse.get_pressed()[0] == 1 and self.rect.collidepoint(pygame.mouse.get_pos()):
            self.slide_x = pygame.mouse.get_pos()[0]
            if self.slide_x < self.x:
                self.slide_x = self.x
            if self.slide_x > self.x + self.width:
                self.slide_x = self.x + self.width


if __name__ == '__main__':
    print('This module is not for direct run!')
