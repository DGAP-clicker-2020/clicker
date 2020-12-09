import ui
import slider
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
    :param current_player: текущий игрок
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

    volume_slider = slider.Slider(
        ui.screen,
        x=50,
        y=150,
        width=WINDOW_WIDTH - 100,
        height=10,
        thin=5,
        color=RED,
        color_ext=BLACK,
        player=current_player
    )

    hello_text = ui.render_outline("MENU", ui.pygame.font.Font(TERMINATOR_FONT_PATH, 45), ORANGE, BLACK, 3)
    audio_text = ui.render_outline("AUDIO VOLUME", ui.pygame.font.Font(SONICBT_FONT_PATH, 35), WHITE, BLACK, 2)
    clock = ui.pygame.time.Clock()
    back_pict = BACK_PICTURES[current_player.player_back_pict]  # выбирает задний фон
    finished = False

    while not finished:
        clock.tick(FPS)
        ui.screen.fill(BLACK)
        ui.draw_back_picture(back_pict, ui.screen)
        ui.screen.blit(hello_text, ((WINDOW_WIDTH - hello_text.get_width()) / 2, WINDOW_WIDTH / 30))
        ui.screen.blit(audio_text, ((WINDOW_WIDTH - audio_text.get_width()) / 2, 150 - audio_text.get_height()))
        return_btn.draw()
        volume_slider.draw()
        music.set_all_volume(music.all_sounds, current_player.audio_volume)
        for event in ui.pygame.event.get():
            return_btn.handle_event(event)
            if return_btn.clicked:
                music.pick_snd.play()
                finished = True
            if event.type == ui.pygame.QUIT:
                finished = True

        current_player.draw_stats()

        ui.pygame.display.update()
