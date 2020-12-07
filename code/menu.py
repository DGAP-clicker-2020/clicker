import ui
from settings import *
import music


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
        color=DEFAULT_BUTTON_COLOR,
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
        color=DEFAULT_BUTTON_COLOR,
        hover_color=(235, 146, 37),
        clicked_color=(213, 23, 23),
        border_radius=5,
        border_width=2
    )

    hello_text = ui.pygame.font.Font(TERMINATOR_FONT_PATH, 45).render("MENU", True, ORANGE)
    clock = ui.pygame.time.Clock()
    back_pict = BACK_PICTURES[current_player.player_back_pict]  # выбирает задний фон
    finished = False

    while not finished:
        clock.tick(FPS)
        ui.screen.fill(BLACK)
        ui.draw_back_picture(back_pict, ui.screen)
        ui.screen.blit(hello_text, ((WINDOW_WIDTH - hello_text.get_width()) / 2, WINDOW_WIDTH / 30))
        return_btn.draw()
        for event in ui.pygame.event.get():
            return_btn.handle_event(event)
            if return_btn.clicked:
                music.pick_snd.play()
                finished = True
            if event.type == ui.pygame.QUIT:
                finished = True

        current_player.draw_stats()

        ui.pygame.display.update()
