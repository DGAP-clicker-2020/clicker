import ui
from settings import *
import music


class Product:
    def __init__(self, btn_x_coord, btn_y_coord, content_of_text, money_cost):
        self.button = ui.Button(
            ui.screen,
            btn_x_coord,
            btn_y_coord,
            text='buy',
            color=DEFAULT_BUTTON_COLOR,
            hover_color=(235, 146, 37),
            clicked_color=(213, 23, 23),
            border_radius=5,
            border_width=2
        )
        self.content_of_text = content_of_text
        self.money_cost = money_cost
        self.text = ui.pygame.font.Font(TERMINATOR_FONT_PATH, 25).render(content_of_text, True, BLACK)
        self.cost_text = ui.pygame.font.Font(TERMINATOR_FONT_PATH, 25).render("-- " + str(self.money_cost) + "$",
                                                                              True, BLACK)

    def draw(self):
        ui.screen.blit(self.text, (10, self.button.y - 5))
        ui.screen.blit(self.cost_text, (300, self.button.y - 5))
        self.button.draw()

    def manage_event(self, event, current_player):
        if current_player.money >= self.money_cost:
            self.button.color = ENOUGH_MONEY_COLOR
            self.button.handle_event(event)
            if self.button.clicked:
                music.purchase_snd.play()
                self.button.clicked = False
                if self.content_of_text == 'afk power':
                    current_player.afk_power += 1
                elif self.content_of_text == 'hand power':
                    current_player.hand_power += 1
                current_player.money -= self.money_cost
        else:
            self.button.hovered = False
            self.button.color = NOT_ENOUGH_MONEY_COLOR


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

    afk_power = Product(440, 255, 'afk power', AFK_POWER_COST)
    hand_power = Product(440, 295, 'hand power', HAND_POWER_COST)

    products = [afk_power, hand_power]

    finished = False
    clock = ui.pygame.time.Clock()

    back_pict = BACK_PICTURES[current_player.player_back_pict]  # выбирает задний фон

    hello_text = ui.pygame.font.Font(TERMINATOR_FONT_PATH, 45).render("SHOP", True, ORANGE)

    while not finished:
        clock.tick(FPS)

        ui.draw_back_picture(back_pict, ui.screen)
        ui.screen.blit(hello_text, ((WINDOW_WIDTH - hello_text.get_width()) / 2, WINDOW_WIDTH / 30))

        for product in products:
            product.draw()
        return_btn.draw()

        for event in ui.pygame.event.get():
            return_btn.handle_event(event)

            for product in products:
                product.manage_event(event, current_player)

            if return_btn.clicked:
                music.pick_snd.play()
                finished = True

            if event.type == ui.pygame.QUIT:
                finished = True

        current_money_text = ui.render_outline('money: ' + str(current_player.money),
                                               ui.pygame.font.Font(SONICBT_FONT_PATH, 50), GOLD, BLACK, 2)
        ui.screen.blit(current_money_text, (10, 70))
        ui.pygame.display.update()
