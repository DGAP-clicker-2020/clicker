import pygame

from typing import Tuple


def slider_draw(surface, rect, color, slide_x, slide_y, thin):

    radius = rect.height // 2

    pygame.gfxdraw.aacircle(surface, int(slide_x), int(slide_y), radius, color)
    pygame.gfxdraw.filled_circle(surface, int(slide_x), int(slide_y), radius, color)
    pygame.draw.rect(surface, color, ((rect.bottomleft[1] - rect.topleft[1]) // 2 - thin, rect.bottomleft[0],
                                      (rect.bottomright[1] - rect.topright[1]) // 2 + thin, rect.bottomright[0]))




class Slider:

    def __init__(
            self,
            surface: pygame.surface.Surface,
            x: int,
            y: int,
            slide_x: int,
            slide_y: int,
            width=0,
            height=0,
            thin=0,
            color: Tuple[int] = None,
            player
    ):

        self.surface = surface
        self.x = x
        self.y = y
        self.thin = thin
        self.slide_x = slide_x
        self.slide_y = slide_y
        self.width = width
        self.height = height
        self.color = color or (224, 224, 224)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.player = player

    def draw(self):
        self.handle_event()
        self.player.s
        slider_draw(self.surface, self.rect, self.color, self.slide_x, self.slide_y, self.thin)

    def handle_event(self):
        '''if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and event.pos in self:
            self.slide_x, self.slide_y = pygame.mouse.get_pos()'''
        if pygame.mouse.get_pressed()[0] != 0:
            # collision detection also needed here
            self.slide_x = pygame.mouse.get_pos()[0]
            if self.slide_x < 0:
                self.slide_x = 0


if __name__ == '__main__':
    print('This module is not for direct run!')
