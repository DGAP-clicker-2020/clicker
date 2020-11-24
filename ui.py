import pygame
from button import Button
from settings import *


pygame.init()

large_font = pygame.font.Font('terminator.ttf', 30)
lower_font = pygame.font.Font('terminator.ttf', 15)


def draw_back_picture(name, surface):
    """рисует задний фон
    type name(названия файла): string"""
    surface.blit(pygame.image.load(name), (0, 0, window_width, window_height))


def change_player(screen):
    """
    Функия обрабатывает ввод имени игрока
    :param screen: экран
    :return: имя нового игрока, и флаг, показывающий осымысленность данных
    """
    hello_text = large_font.render("TYPE YOUR NAME", False, (0, 180, 0))
    pygame.display.update()
    clock = pygame.time.Clock()
    new_data = False

    cancel_btn = Button(
        screen,
        10,
        150,
        text='Cancel',
        color=(200, 200, 200),
        hover_color=(235, 146, 37),
        clicked_color=(213, 23, 23),
        border_radius=5,
        border_width=2
    )

    finished = False

    new_name = ''
    while not finished:
        new_data = True
        clock.tick(FPS)
        screen.fill(BLACK)
        screen.blit(hello_text, (10, 10))
        cancel_btn.draw()
        for event in pygame.event.get():
            cancel_btn.handle_event(event)
            if cancel_btn.clicked:
                finished = True
                new_data = False
            if event.type == pygame.QUIT:
                finished = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    finished = True
                    new_data = True
                    break
                elif event.key == 8:
                    new_name = new_name[:-1]
                else:
                    new_name += event.unicode
        current_name_text = large_font.render(new_name, False, (200, 0, 0))
        screen.blit(current_name_text, (10, 70))
        pygame.display.update()
    return new_data, new_name


def create_change_name_btn(screen):
    """
    Функция создаёт кнопочку
    :param screen: экран
    :return: экземпляр класс Button
    """
    return Button(
            screen,
            10,
            130,
            text='Change player',
            color=(200, 200, 200),
            hover_color=(235, 146, 37),
            clicked_color=(213, 23, 23),
            border_radius=5,
            border_width=2
        )


if __name__ == '__main__':
    print('This module is not for direct run!')
