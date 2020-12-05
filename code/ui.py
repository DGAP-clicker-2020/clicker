import pygame

from button import Button
from settings import *

pygame.init()

large_font = pygame.font.Font('terminator.ttf', 30)
lower_font = pygame.font.Font('terminator.ttf', 15)

screen = pygame.display.set_mode((window_width, window_height))
screen.fill(BLACK)
pygame.display.update()


def draw_back_picture(name, surface):
    """рисует задний фон
    type name(названия файла): string"""
    surface.blit(pygame.image.load(name), (0, 0, window_width, window_height))


def show_offline_income(money_earned, offline_time):
    cancel_btn = Button(
        screen,
        5,
        100,
        text='OK',
        color=(51, 153, 255),
        hover_color=(235, 146, 37),
        clicked_color=(213, 23, 23),
        border_radius=5,
        border_width=2
    )
    finished = False
    clock = pygame.time.Clock()
    date = {'d': offline_time // 86400, 'h': (offline_time % 86400) // 3600,
            'min': ((offline_time % 86400) % 3600) // 60, 'sec': ((offline_time % 86400) % 3600) % 60}
    date_str = ''
    for k, v in date.items():
        if v != 0:
            date_str += f'{v}{k} '
    text1 = large_font.render('You were offline', True, RED)
    text2 = large_font.render(date_str, True, RED)
    text3 = large_font.render('and earned ' + str(format(money_earned, '.0f')), True, RED)
    while not finished:
        clock.tick(FPS)
        screen.fill(BLACK)
        draw_back_picture(back_pictures['mipt_logo.jpg'], screen)
        screen.blit(text1, (5, 0))
        screen.blit(text2, (5, 30))
        screen.blit(text3, (5, 60))
        cancel_btn.draw()
        for event in pygame.event.get():
            cancel_btn.handle_event(event)
            if cancel_btn.clicked:
                finished = True
            if event.type == pygame.QUIT:
                finished = True
        screen.blit(screen, (0, 0))
        pygame.display.update()


def change_player():
    """
    Функия обрабатывает ввод имени игрока
    :return: имя нового игрока, и флаг, показывающий осымысленность данных
    """
    hello_text = large_font.render("TYPE YOUR NAME", True, (0, 180, 0))
    pygame.display.update()
    clock = pygame.time.Clock()
    new_data = False

    cancel_btn = Button(
        screen,
        10,
        130,
        text='Cancel',
        color=(51, 153, 255),
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
        draw_back_picture(back_pictures['mipt_logo.jpg'], screen)
        screen.blit(hello_text, (10, 10))
        cancel_btn.draw()
        for event in pygame.event.get():
            cancel_btn.handle_event(event)
            if cancel_btn.clicked:
                finished = True
                new_data = False
            if event.type == pygame.QUIT:
                finished = True
                new_data = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    finished = True
                    new_data = True
                    break
                elif event.key == 8:
                    new_name = new_name[:-1]
                else:
                    new_name += event.unicode
        current_name_text = large_font.render(new_name, True, (200, 0, 0))
        screen.blit(current_name_text, (10, 70))
        pygame.display.update()
    return new_data, new_name


def create_change_name_btn():
    """
    Функция создаёт кнопочку
    :return: экземпляр класс Button
    """
    return Button(
        screen,
        10,
        130,
        text='Change player',
        color=(51, 153, 255),
        hover_color=(235, 146, 37),
        clicked_color=(213, 23, 23),
        border_radius=5,
        border_width=2
    )


if __name__ == '__main__':
    print('This module is not for direct run!')
