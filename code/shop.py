import ui
import product
from settings import *
import music


def create_shop_btn():
    """
    Функция создаёт кнопочку
    :return: экземпляр класс Button
    """
    return ui.Button(
        ui.screen,
        420,
        170,
        text='shop',
        color=DEFAULT_BUTTON_COLOR,
        hover_color=(235, 146, 37),
        clicked_color=(213, 23, 23),
        border_radius=5,
        border_width=2
    )


def shop_window(current_player):
    """
    Функция для вывода меню
    """
    return_btn = ui.Button(
        ui.screen,
        390,
        170,
        text='return',
        color=DEFAULT_BUTTON_COLOR,
        hover_color=(235, 146, 37),
        clicked_color=(213, 23, 23),
        border_radius=5,
        border_width=2
    )

    finished = False
    clock = ui.pygame.time.Clock()

    hello_text = ui.render_outline("SHOP", ui.pygame.font.Font(TERMINATOR_FONT_PATH, 45), ORANGE, BLACK, 3)

    while not finished:
        clock.tick(FPS)

        back_pict = BACK_PICTURES[current_player.player_back_pict]  # обновляет задний фон
        ui.draw_back_picture(back_pict, ui.screen)
        ui.screen.blit(hello_text, ((WINDOW_WIDTH - hello_text.get_width()) / 2, WINDOW_WIDTH / 30))

        for prod in product.products:
            prod.check_hold(current_player)
            prod.draw()
        return_btn.draw()

        for event in ui.pygame.event.get():
            return_btn.handle_event(event)

            for prod in product.products:
                prod.manage_event(event, current_player)

            if return_btn.left_clicked:
                music.pick_snd.play()
                finished = True

            if event.type == ui.pygame.QUIT:
                finished = True

        guide_text1 = ui.render_outline('LEFT CLICK - BUY x1', ui.pygame.font.Font(TERMINATOR_FONT_PATH, 13), WHITE, BLACK, 1)
        guide_text2 = ui.render_outline('RIGHT CLICK - BUY x10', ui.pygame.font.Font(TERMINATOR_FONT_PATH, 13), WHITE, BLACK, 1)
        current_money_text = ui.render_outline('money: ' + str(current_player.money) + ' $',
                                               ui.pygame.font.Font(SONICBT_FONT_PATH, 50), GOLD, BLACK, 2)
        ui.screen.blit(current_money_text, (10, 70))
        ui.screen.blit(guide_text1, (250, 715))
        ui.screen.blit(guide_text2, (250, 730))
        ui.pygame.display.update()
