import ui
import music
from settings import *


class Product:
    def __init__(self, x_coord, y_coord, content_of_text, money_cost, type, flag):
        """
        Сборщик класса Товар
        :param x_coord: координата x
        :param y_coord: координата y
        :param content_of_text: описание товара
        :param money_cost: стоимость улучшения
        :type вид товара
        """
        self.type = type
        self.hold = False
        self.flag = flag
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.content_of_text = content_of_text
        self.money_cost = money_cost
        self.text = ui.pygame.font.Font(TERMINATOR_FONT_PATH, 25).render(content_of_text + "-" + str(self.money_cost)
                                                                         + "$", True, BLACK)

        self.button = ui.Button(
            ui.screen,
            self.x_coord + self.text.get_width(),
            self.y_coord,
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
        if self.flag in current_player.hold_products:
            self.hold = True
        else:
            self.hold = False
        if self.hold and self.type != 'boost':
            self.button.color = YELLOW

    def manage_event(self, event, current_player):
        """
        Обработчик событий
        :param event: событие
        :param current_player: текущий игрок
        """
        self.check_hold(current_player)
        if current_player.money >= self.money_cost:
            self.button.color = ENOUGH_MONEY_COLOR
            self.button.handle_event(event)
            if self.button.clicked:
                music.purchase_snd.play()
                self.button.clicked = False
                if self.content_of_text == 'afk power':
                    current_player.afk_power += 1
                    current_player.money -= self.money_cost
                elif self.content_of_text == 'hand power':
                    current_player.hand_power += 1
                    current_player.money -= self.money_cost
                elif self.type == 'music' and not self.hold:
                    current_player.hold_products.append(self.flag)
                    self.hold = True
                    current_player.bg_snd.stop()
                    current_player.bg_snd = music.all_music[self.flag]
                    current_player.bg_snd.play(-1, 0, 3000)
                    current_player.money -= self.money_cost
        else:
            self.button.hovered = False
            self.button.color = NOT_ENOUGH_MONEY_COLOR
        if self.type == 'music' and self.hold:
            self.button.handle_event(event)
            if self.button.clicked:
                self.button.clicked = False
                music.purchase_snd.play()
                current_player.bg_snd.stop()
                current_player.bg_snd = music.all_music[self.flag]
                current_player.bg_snd.play(-1, 0, 3000)


afk_power = Product(0, 230, 'afk power', 20, 'boost', 1)
hand_power = Product(0, 270, 'hand power', 30, 'boost', 2)
bg_snd = Product(0, 310, 'def_sound', 0, 'music', 3)
minecraft_1_snd = Product(0, 350, 'minecraft_1', 100, 'music', 4)
minecraft_2_snd = Product(0, 390, 'minecraft_2', 200, 'music', 5)
matreshka_snd = Product(0, 430, 'matreshka', 9999, 'music', 6)

products = [afk_power, hand_power, bg_snd, minecraft_1_snd, minecraft_2_snd, matreshka_snd]