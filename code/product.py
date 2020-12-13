import ui
import music
from settings import *


class Product:
    def __init__(self, content_of_text, money_cost, type, flag):
        """
        Сборщик класса Товар
        :param content_of_text: описание товара
        :param money_cost: стоимость улучшения
        :param type: тип товара
        :param flag: номер товара
        """
        self.type = type
        self.hold = False
        self.flag = flag
        self.x_coord = 5
        self.y_coord = 230 + 40 * (self.flag - 1)
        self.content_of_text = content_of_text
        self.money_cost = money_cost

        self.text = ui.render_outline(content_of_text + "-" + str(self.money_cost) + "$",
                                      ui.pygame.font.Font(TERMINATOR_FONT_PATH, 25), WHITE, BLACK, 2)

        self.button = ui.Button(
            ui.screen,
            self.x_coord + self.text.get_width() + 5,
            self.y_coord + 7,
            text='buy',
            color=DEFAULT_BUTTON_COLOR,
            hover_color=(235, 146, 37),
            clicked_color=(213, 23, 23),
            border_radius=5,
            border_width=2
        )

    def draw(self):
        """
        Метод, отвечающий за прорисовку товара.
        """
        ui.screen.blit(self.text, (self.x_coord, self.y_coord))
        self.button.draw()


    def check_hold(self, current_player):
        if self.hold and self.type != 'boost':
            self.button.color = YELLOW
            self.button.text = 'use'
        if self.hold and self.type == 'music' and current_player.bg_snd == music.all_music[self.flag]:
            self.button.color = WHITE
        if self.hold and self.type == 'background' and current_player.player_back_pict == SHOP_BACK_PICTURES[self.flag]:
            self.button.color = WHITE
        if self.flag in current_player.hold_products:
            self.hold = True

    def manage_event(self, event, current_player):
        """
        Обработчик событий
        :param event: событие
        :param current_player: текущий игрок
        """
        if current_player.money >= self.money_cost or self.hold:

            self.button.color = ENOUGH_MONEY_COLOR
            self.button.handle_event(event)

            if self.button.right_clicked and current_player.money >= 10 * self.money_cost:
                music.purchase_snd.play()
                self.button.right_clicked = False

                if self.content_of_text == 'afk power':
                    current_player.afk_power += 10
                    current_player.money -= 10 * self.money_cost

                elif self.content_of_text == 'hand power':
                    current_player.hand_power += 10
                    current_player.money -= 10 * self.money_cost

                elif self.content_of_text == 'crit chance':
                    current_player.critical_chance += 10
                    current_player.money -= 10 * self.money_cost

                elif self.content_of_text == 'crit multi':
                    current_player.critical_multiplier += 10
                    current_player.money -= 10 * self.money_cost

            if self.button.left_clicked:
                music.purchase_snd.play()
                self.button.left_clicked = False

                if self.content_of_text == 'afk power':
                    current_player.afk_power += 1
                    current_player.money -= self.money_cost

                elif self.content_of_text == 'hand power':
                    current_player.hand_power += 1
                    current_player.money -= self.money_cost

                elif self.content_of_text == 'crit chance':
                    current_player.critical_chance += 1
                    current_player.money -= self.money_cost

                elif self.content_of_text == 'crit multi':
                    current_player.critical_multiplier += 0.5
                    current_player.money -= self.money_cost

                elif self.type == 'music' and not self.hold:
                    current_player.hold_products.append(self.flag)
                    self.hold = True
                    current_player.bg_snd.stop()
                    current_player.back_snd = self.flag
                    current_player.bg_snd = music.all_music[current_player.back_snd]
                    current_player.bg_snd.play(-1, 0, 3000)
                    current_player.money -= self.money_cost

                elif self.type == 'music' and self.hold:
                    current_player.bg_snd.stop()
                    current_player.back_snd = self.flag
                    current_player.bg_snd = music.all_music[current_player.back_snd]
                    current_player.bg_snd.play(-1, 0, 3000)

                elif self.type == 'background' and not self.hold:
                    current_player.hold_products.append(self.flag)
                    self.hold = True
                    current_player.player_back_pict = SHOP_BACK_PICTURES[self.flag]
                    current_player.money -= self.money_cost

                elif self.type == 'background' and self.hold:
                    current_player.player_back_pict = SHOP_BACK_PICTURES[self.flag]

        else:
            self.button.hovered = False
            self.button.color = NOT_ENOUGH_MONEY_COLOR


afk_power = Product('afk power', 20, 'boost', 1)
hand_power = Product('hand power', 30, 'boost', 2)
critical_chance = Product('crit chance', 1500, 'boost', 10)
critical_multiplier = Product('crit multi', 1500, 'boost', 11)
def_snd = Product('def_sound', 0, 'music', 3)
minecraft_1_snd = Product('minecraft_1', 100, 'music', 4)
minecraft_2_snd = Product('minecraft_2', 200, 'music', 5)
matreshka_snd = Product('matreshka', 9999, 'music', 6)
kpm_background = Product('kpm_picture', 0, 'background', 7)
bio_background = Product('bio_picture', 300, 'background', 8)
nk_background = Product('nk_picture', 5000, 'background', 9)

products = [
    afk_power,
    hand_power,
    critical_chance,
    critical_multiplier,
    def_snd,
    minecraft_1_snd,
    minecraft_2_snd,
    matreshka_snd,
    kpm_background,
    bio_background,
    nk_background,
]
