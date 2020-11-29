from button import Button
import player
from settings import *
from ui import *

players = player.read_players_from_file()
current_player = player.define_current_player(players)
back_pict = back_pictures[current_player.player_back_pict]  # выбирает задний фон


def create_menu_btn():
    """
    Функция создаёт кнопочку
    :return: экземпляр класс Button
    """
    return Button(
        screen,
        10,
        170,
        text='Menu',
        color=(51, 153, 255),
        hover_color=(235, 146, 37),
        clicked_color=(213, 23, 23),
        border_radius=5,
        border_width=2
    )


def menu_window():
    """
    Функция для вывода меню
    """
    return_btn = Button(
        screen,
        10,
        170,
        text='return',
        color=(51, 153, 255),
        hover_color=(235, 146, 37),
        clicked_color=(213, 23, 23),
        border_radius=5,
        border_width=2
    )

    hello_text = pygame.font.Font('terminator.ttf', 45).render("MENU", True, (0, 180, 0))
    clock = pygame.time.Clock()
    finished = False

    while not finished:
        new_data = True
        clock.tick(FPS)
        screen.fill(BLACK)
        draw_back_picture(back_pict, screen)
        screen.blit(hello_text, ((window_width - hello_text.get_width()) / 2, window_width / 30))
        return_btn.draw()
        for event in pygame.event.get():
            return_btn.handle_event(event)
            if return_btn.clicked:
                finished = True
                new_data = False
            if event.type == pygame.QUIT:
                finished = True

        current_money_text = large_font.render('money: ' + str(current_player.money) + '$',
                                               True, (255, 215, 0))
        screen.blit(current_money_text, (10, 70))
        pygame.display.update()
