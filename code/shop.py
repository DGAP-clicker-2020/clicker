import ui
from settings import *
from music import *

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
        color=(51, 153, 255),
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
        color=(51, 153, 255),
        hover_color=(235, 146, 37),
        clicked_color=(213, 23, 23),
        border_radius=5,
        border_width=2
    )

    buy_afk_power_btn = ui.Button(
        ui.screen,
        440,
        255,
        text='buy',
        color=(51, 153, 255),
        hover_color=(235, 146, 37),
        clicked_color=(213, 23, 23),
        border_radius=5,
        border_width=2
    )

    buy_hand_power_btn = ui.Button(
        ui.screen,
        440,
        295,
        text='buy',
        color=(51, 153, 255),
        hover_color=(235, 146, 37),
        clicked_color=(213, 23, 23),
        border_radius=5,
        border_width=2
    )

    finished = False
    clock = ui.pygame.time.Clock()

    back_pict = back_pictures[current_player.player_back_pict]  # выбирает задний фон

    hello_text = ui.pygame.font.Font('terminator.ttf', 45).render("SHOP", True, ORANGE)
    afk_power_text = ui.pygame.font.Font('terminator.ttf', 25).render("AFK POWER", True, BLACK)
    hand_power_text = ui.pygame.font.Font('terminator.ttf', 25).render("HAND POWER", True, BLACK)
    afk_power_cost_text = ui.pygame.font.Font('terminator.ttf', 25).render("-- " + str(AFK_POWER_COST) + "$",
                                                                           True, BLACK)
    hand_power_cost_text = ui.pygame.font.Font('terminator.ttf', 25).render("-- " + str(HAND_POWER_COST) + "$",
                                                                            True, BLACK)

    while not finished:
        clock.tick(FPS)

        ui.draw_back_picture(back_pict, ui.screen)
        ui.screen.blit(hello_text, ((window_width - hello_text.get_width()) / 2, window_width / 30))
        ui.screen.blit(afk_power_text, (10, 250))
        ui.screen.blit(hand_power_text, (10, 260 + hand_power_text.get_height()))
        ui.screen.blit(afk_power_cost_text, (300, 250))
        ui.screen.blit(hand_power_cost_text, (300, 260 + hand_power_text.get_height()))

        buy_afk_power_btn.draw()
        buy_hand_power_btn.draw()

        return_btn.draw()
        for event in ui.pygame.event.get():
            return_btn.handle_event(event)

            if current_player.money >= AFK_POWER_COST:
                buy_afk_power_btn.color = (51, 153, 255)
                buy_afk_power_btn.handle_event(event)
                if buy_afk_power_btn.clicked:
                    purchase_snd.play()
                    buy_afk_power_btn.clicked = False
                    current_player.afk_power += 1
                    current_player.money -= AFK_POWER_COST
            else:
                buy_afk_power_btn.hovered = False
                buy_afk_power_btn.color = (128, 128, 128)

            if current_player.money >= HAND_POWER_COST:
                buy_hand_power_btn.color = (51, 153, 255)
                buy_hand_power_btn.handle_event(event)
                if buy_hand_power_btn.clicked:
                    purchase_snd.play()
                    buy_hand_power_btn.clicked = False
                    current_player.hand_power += 1
                    current_player.money -= HAND_POWER_COST
            else:
                buy_hand_power_btn.hovered = False
                buy_hand_power_btn.color = (128, 128, 128)

            if return_btn.clicked:
                pick_snd.play()
                finished = True
            if event.type == ui.pygame.QUIT:
                finished = True

        current_money_text = ui.render_outline('money: ' + str(current_player.money),
                                               ui.pygame.font.Font('SonicBT.otf', 50), GOLD, BLACK, 2)
        ui.screen.blit(current_money_text, (10, 70))
        ui.pygame.display.update()
