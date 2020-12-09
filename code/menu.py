import ui
import slider
from settings import *


def create_menu_btn():
    """
    Функция создаёт кнопочку
    :return: экземпляр класс Button
    """
    return ui.Button(
        ui.screen,
        10,
        170,
        text='Menu',
        color=(51, 153, 255),
        hover_color=(235, 146, 37),
        clicked_color=(213, 23, 23),
        border_radius=5,
        border_width=2
    )


def menu_window(current_player):
    """
    Функция для вывода меню
    """
    return_btn = ui.Button(
        ui.screen,
        10,
        170,
        text='return',
        color=(51, 153, 255),
        hover_color=(235, 146, 37),
        clicked_color=(213, 23, 23),
        border_radius=5,
        border_width=2
    )

    volume_slider = slider.Slider(
        ui.screen,
        x=window_width // 2 - (window_width - 20 * 2) // 2,
        y=window_height // 10 - 25,
        slide_x=window_width // 2,
        slide_y=window_height // 10,
        width=window_width - 20 * 2,
        height=50,
        thin=5,
        color=RED,
        player=current_player
    )

    hello_text = ui.pygame.font.Font('terminator.ttf', 45).render("MENU", True, ORANGE)
    clock = ui.pygame.time.Clock()
    back_pict = back_pictures[current_player.player_back_pict]  # выбирает задний фон
    finished = False

    while not finished:
        clock.tick(ui.FPS)
        ui.screen.fill(ui.BLACK)
        ui.draw_back_picture(back_pict, ui.screen)
        ui.screen.blit(hello_text, ((ui.window_width - hello_text.get_width()) / 2, ui.window_width / 30))
        return_btn.draw()
        volume_slider.draw()
        for event in ui.pygame.event.get():
            return_btn.handle_event(event)
            if return_btn.clicked:
                finished = True
            if event.type == ui.pygame.QUIT:
                finished = True

        current_player.draw_stats()

        ui.pygame.display.update()
