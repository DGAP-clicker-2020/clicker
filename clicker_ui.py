import pygame
from button import Button
from clicker_settings import *


def cancel_name_enter(*args):
    return True, False


def change_player(screen):
    f2 = pygame.font.SysFont('serif', 60)
    f1 = pygame.font.SysFont('serif', 60)
    text2 = f1.render("Введите ваше имя", 0, (0, 180, 0))
    pygame.display.update()
    clock = pygame.time.Clock()
    new_data = False

    cancel_btn = Button(
        screen,
        10,
        130,
        cancel_name_enter,
        text='Cancel',
        color=(200, 200, 200),
        hover_color=(235, 146, 37),
        clicked_color=(213, 23, 23),
        border_radius=5,
        border_width=2
    )

    f = True
    finished = False

    string = ''
    while not finished:
        while f:
            clock.tick(FPS)
            screen.fill(BLACK)
            screen.blit(text2, (10, 10))
            cancel_btn.draw()
            for event in pygame.event.get():
                finished, f = cancel_btn.handle_event(event, screen)
                if event.type == pygame.QUIT:
                    finished = True
                    f = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        f = False
                        finished = True
                        new_data = True
                        break
                    elif event.key == 8:
                        string = string[:-1]
                    else:
                        string += event.unicode
            text3 = f2.render(string, 0, (200, 0, 0))
            screen.blit(text3, (10, 70))
            pygame.display.update()
    return new_data, string


def create_change_name_btn(screen):
    return Button(
            screen,
            10,
            130,
            change_player,
            text='Change player',
            color=(200, 200, 200),
            hover_color=(235, 146, 37),
            clicked_color=(213, 23, 23),
            border_radius=5,
            border_width=2
        )


if __name__ == '__main__':
    print('This module is not for direct run!')
