import json
import math
import time
import zlib
from random import randint

from settings import *
import ui
import music
from auxiliary_functions import calculate_hp


def handle_new_data(new_name, players, current_player):
    """
    Функция обрабатывает новое введённое имя после нажатия на кнопку change name
    :param new_name: имя нового игрока
    :param players: список игроков
    :param current_player: текущий игрок
    :return: возвращает изменённый список игроков и текущего игрока
    """
    current_player.bg_snd.stop()

    current_player.last_login = int(time.time())
    current_player.last_player = False
    really_new_player = True

    for pl in players:
        if new_name.lower() == pl.name.lower():
            current_player = pl
            current_player.last_player = True
            current_player.calculate_offline_money()
            really_new_player = False

    if really_new_player:
        if new_name == '':
            current_player = Player
        else:
            current_player = Player(name=new_name, last_player=True)
        players.append(current_player)

    current_player.bg_snd.play(-1, 0, 3000)
    return players, current_player


def read_players_from_file():
    """
    Функция считывает игроков из базы данных
    :rtype: list
    :return: список игроков
    """
    players = []

    try:
        if DEBUG_FLAG:
            file = open('players.json', 'r')
            new_dict = json.load(file)
            file.close()
        else:
            with open(os.path.join('..', 'data', 'players'), 'rb') as f:
                data = f.read()
            data = zlib.decompress(data)
            data = data.decode('utf-8')
            new_dict = json.loads(data)
        for val in new_dict.values():
            players.append(Player(name=val['name'], id_num=val['id_num'], hand_power=val['hand_power'],
                                  critical_multiplier=val['critical_multiplier'],
                                  critical_chance=val['critical_chance'],
                                  last_player=val['last_player'], current_target=val['current_target'],
                                  current_target_level=val['current_target_level'],
                                  afk_power=val['afk_power'], money=val['money'], last_login=val['last_login'],
                                  player_back_pict=val['player_back_pict'], total_clicks=val['total_clicks'],
                                  total_damage=val['total_damage'], hold_products=val['hold_products'],
                                  back_snd=val['back_snd']))
    except (json.JSONDecodeError, FileNotFoundError, zlib.error, KeyError):
        pass

    if not players:
        new_data, new_name = ui.change_player()
        if not new_data:
            players.append(Player(name='Sample Name', last_player=True))
        else:
            players.append(Player(name=new_name, last_player=True))

    return players


def define_current_player(players):
    """
    Функция определяет текущего игрока
    :param players: список игроков
    :return: возвращает текущего игрока
    """
    for pl in players:
        if pl.last_player:
            return pl


def write_players_to_file(players):
    """
    Функция записывает информацию об игроках в файл
    :param players: список игроков
    """
    for pl in players:
        pl.bg_snd = None

    dic = {}

    for count, pl in enumerate(players):
        dic[count] = pl.__dict__

    if not DEBUG_FLAG:
        dic = json.dumps(dic, indent='    ')
        dic = zlib.compress(dic.encode('utf-8'))
        with open(os.path.join('..', 'data', 'players'), 'wb') as file:
            file.write(dic)
    else:
        with open('players.json', 'w') as file:
            dic = {}
            for count, pl in enumerate(players):
                dic[count] = pl.__dict__
            json.dump(dic, file)


class Player:

    def __init__(self,
                 name='Sample Name',
                 id_num=randint(1, 1000),
                 hand_power=1,
                 last_player=False,
                 current_target=0,
                 current_target_level=1,
                 critical_multiplier=2,
                 critical_chance=0,
                 afk_power=0,
                 money=0,
                 last_login=int(time.time()),
                 new_login=int(time.time()),
                 player_back_pict='kpm_1.jpg',
                 total_clicks=0,
                 total_damage=0,
                 audio_volume=50,
                 hold_products=None,
                 back_snd=5
                 ):
        """
        Сборщик экземпляра класса Player
        :param critical_multiplier: множитель критического урона
        :param critical_chance: шанс критического урона
        :param total_clicks: общее коллическтво кликов
        :param total_damage: общее колличество урона
        :param audio_volume: громкость звуков
        :param hold_products: список купленных товаров
        :param back_snd: музыка на заднем фоне
        :param current_target: колличество убитых целей
        :param last_login: последнее время захода в игру, обновляется после выхода из игры
        :param new_login: время, обновляющееся после захода игру
        :param player_back_pict: задний фон игрока
        :param name: имя
        :param id_num: идентификационный номер
        :param hand_power: сила клика
        :param last_player: флаг-статус последнего игрока
        :param current_target: текущий уровень цели
        :param afk_power: урон каждую секунду
        :param money: колличество денег
        """
        if hold_products is None:
            hold_products = [5, 9]
        self.name = name
        self.id_num = id_num
        self.hand_power = hand_power
        self.afk_power = afk_power
        self.critical_multiplier = critical_multiplier
        self.critical_chance = critical_chance
        self.last_player = last_player
        self.current_target = current_target
        self.current_target_level = current_target_level
        self.money = money
        self.last_login = last_login
        self.new_login = new_login
        self.player_back_pict = player_back_pict
        self.total_clicks = total_clicks
        self.total_damage = total_damage
        self.audio_volume = audio_volume
        self.hold_products = hold_products
        self.back_snd = back_snd
        self.bg_snd = music.all_music[self.back_snd]

        if self.last_player:
            self.bg_snd.play(-1, 0, 3000)

        self.calculate_offline_money()

    def power_up(self):
        """
        Улучшение игрока после уничтожения цели
        """
        self.money += int(0.5 * math.exp(self.current_target_level))
        if self.current_target_level >= 5:
            self.current_target_level = 0
        self.current_target += 1
        self.current_target_level += 1

    def draw_stats(self):
        """
        Метод выводит статистику игрока на экран
        """
        dic = self.__dict__
        count = 0
        for key in [
            'name',
            'afk_power',
            'hand_power',
            'critical_multiplier',
            'critical_chance',
            'current_target',
            'money',
            'total_clicks',
            'total_damage',
            'audio_volume'
        ]:
            if key == 'total_damage':
                text = ui.render_outline(str(key) + ': ' + str(format(dic[key], '.2e')), ui.lower_font, CYAN, BLACK, 1)
            else:
                text = ui.render_outline(str(key) + ': ' + str(dic[key]), ui.lower_font, CYAN, BLACK, 1)

            ui.screen.blit(text, (10, 200 + count * 25))
            count += 1

    def calculate_offline_money(self):
        """
        Метод начисляет игроку деньги за время, проведённое вне игры
        """
        self.new_login = int(time.time())
        initial_money = self.money
        offline_time = self.new_login - self.last_login
        damage = offline_time * self.afk_power
        self.total_damage += damage

        while True:
            hp = calculate_hp(self.current_target)
            if damage > hp:
                self.money += int(0.5 * math.exp(self.current_target_level))
                if self.current_target_level >= 5:
                    self.current_target_level = 0
                self.current_target_level += 1
                self.current_target += 1
                damage -= hp
            else:
                if self.last_player and self.afk_power != 0:
                    money_earned = self.money - initial_money
                    ui.show_offline_income(money_earned, offline_time)
                break


if __name__ == '__main__':
    print('This module is not for direct run!')
