from typing import Tuple, Callable

import pygame

from settings import TERMINATOR_FONT_PATH


def _round_rect(surface, rect, color, radius=None):
    if not radius:
        pygame.gfxdraw.rect(surface, color, rect)
        return

    radius = min(radius, rect.width / 2, rect.height / 2)

    r = rect.inflate(-radius * 2, -radius * 2)
    for corn in (r.topleft, r.topright, r.bottomleft, r.bottomright):
        pygame.gfxdraw.aacircle(surface, corn[0], corn[1], radius, color)
        pygame.gfxdraw.filled_circle(surface, corn[0], corn[1], radius, color)
    pygame.gfxdraw.aapolygon(surface, [r.inflate(radius * 2, 0).topleft, r.inflate(radius * 2, 0).topright,
                                       r.inflate(radius * 2, 0).bottomright, r.inflate(radius * 2, 0).bottomleft],
                             color)
    pygame.gfxdraw.aapolygon(surface, [r.inflate(0, radius * 2).topleft, r.inflate(0, radius * 2).topright,
                                       r.inflate(0, radius * 2).bottomright, r.inflate(0, radius * 2).bottomleft],
                             color)
    pygame.gfxdraw.filled_polygon(surface, [r.inflate(radius * 2, 0).topleft, r.inflate(radius * 2, 0).topright,
                                            r.inflate(radius * 2, 0).bottomright, r.inflate(radius * 2, 0).bottomleft],
                                  color)
    pygame.gfxdraw.filled_polygon(surface, [r.inflate(0, radius * 2).topleft, r.inflate(0, radius * 2).topright,
                                            r.inflate(0, radius * 2).bottomright, r.inflate(0, radius * 2).bottomleft],
                                  color)


class Button:
    """
    Button class
    Contructor params:
    surface: surface to display button
    x, y: top-left coordinates
    click_handler: function that is called when the button is clicked,
        default is lambda, doing nothing
    text: text to display on button
    width, height: button size. If not provided, calculated by size of text
    color: button color, default is (224, 224, 224)
    hover_color: button color when hovered, if None (default), no effect
    clicked_color: button color when clicked, if None (default), no effect
    border_color, border_width, border_radius - border params
    font: text font, pygame.font.Font instance, default is Courier New 20
    font_color: default is black
    Methods defined:
    draw(): draws the button on given surface
    handle_event(event): handles mouse events (hover and click). Must be called in
        main loop.
    handle_events(event_list): handles all events in event_list
    To check if given point is inside the button, use 'in' operator:
        if (120, 50) in button: ...
    """

    def __init__(
            self,
            surface: pygame.surface.Surface,
            x: int,
            y: int,
            click_handler: Callable = lambda: None,
            text="",
            width=0,
            height=0,
            color: Tuple[int] = None,
            border_width=0,
            hover_color=None,
            clicked_color=None,
            border_radius=0,
            border_color=None,
            font: pygame.font.Font = None,
            font_color=None
    ):

        self.surface = surface
        self.x = x
        self.y = y
        self.click_handler = click_handler
        self.color = color or (224, 224, 224)
        self.border_width = border_width
        self.hover_color = hover_color
        self.clicked_color = clicked_color
        self.border_radius = border_radius
        self.text = text

        if font is None:
            self.font = pygame.font.Font(TERMINATOR_FONT_PATH, 15)

        text_size = self.font.size(text)
        self.width = width or text_size[0] + self.border_width + 2
        self.height = height or text_size[1] + self.border_width + 2
        self.font_color = font_color or (0, 0, 0)

        self.hovered = False
        self.left_clicked = False
        self.right_clicked = False
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def __repr__(self):
        return f'<Button "{self.text}" at ({self.x}, {self.y})>'

    def __contains__(self, point: Tuple[int]):
        return self.rect.collidepoint(point)

    def draw(self):
        color = self.color
        if self.left_clicked and self.clicked_color:
            color = self.clicked_color
        elif self.hovered and self.hover_color:
            color = self.hover_color

        if not self.border_width:
            _round_rect(self.surface, self.rect, color, self.border_radius)
        else:
            _round_rect(self.surface, self.rect, (0, 0, 0), self.border_radius)
            _round_rect(
                self.surface,
                self.rect.inflate(-self.border_width, -self.border_width),
                color,
                self.border_radius
            )
        text = self.font.render(self.text, True, self.font_color)
        place = text.get_rect(center=self.rect.center)
        self.surface.blit(text, place)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hovered = event.pos in self
        elif event.type == pygame.MOUSEBUTTONDOWN and event.pos in self:
            if event.button == 1:
                self.left_clicked = True
            if event.button == 3:
                self.right_clicked = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.left_clicked = False
            if event.button == 3:
                self.right_clicked = False

    def handle_events(self, event_list):
        for event in event_list:
            self.handle_event(event)


if __name__ == '__main__':
    print('This module is not for direct run!')
