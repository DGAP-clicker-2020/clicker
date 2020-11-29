import json
import math
import time
from random import randint

import ui
from settings import *


def handle_new_data(new_name, players, current_player):
    """
    Функция обрабатывает новое введённое имя после нажатия на кнопку change name
    :param new_name: имя нового игрока
    :param players: список игроков
    :param current_player: текущий игрок
    :return: возвращает изменённый список игроков и текущего игрока
    """
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
    return players, current_player


def read_players_from_file():
    """
    Функция считывает игроков из базы данных
    :rtype: list
    :return: список игроков
    """
    players = []
    try:
        file = open('players.json', 'r')
        new_dict = json.load(file)
        file.close()
        for val in new_dict.values():
            players.append(Player(name=val['name'], id_num=val['id_num'], hand_power=val['hand_power'],
                                  last_player=val['last_player'], current_target=val['current_target'],
                                  current_target_level=val['current_target_level'],
                                  afk_power=val['afk_power'], money=val['money'], last_login=val['last_login'],
                                  player_back_pict=val['player_back_pict']))
    except (json.JSONDecodeError, FileNotFoundError):
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
    Функция записывает информацию об игроках в json-файл
    :param players: список игроков
    """
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
                 afk_power=0.0,
                 money=0.0,
                 last_login=int(time.time()),
                 new_login=int(time.time()),
                 player_back_pict='kpm_1.jpg'
                 ):
        """
        Сборщик экземпляра класса Player
        :param name: имя
        :param id_num: идентификационный номер
        :param hand_power: сила клика
        :param last_player: Флаг-статус последнего игрока
        :param current_target_level: Колличество убитых целей
        :param afk_power: Урон каждую секунду
        :param money: колличество денег
        """
        self.name = name
        self.id_num = id_num
        self.hand_power = hand_power
        self.afk_power = afk_power
        self.last_player = last_player
        self.current_target = current_target
        self.current_target_level = current_target_level
        self.money = money
        self.last_login = last_login
        self.new_login = new_login
        self.player_back_pict  = player_back_pict
        self.calculate_offline_money()

    def power_up(self):
        """
        Улучшение игрока после уничтожения цели
        """
        self.money += int(math.exp(0.1 * self.current_target_level))
        self.hand_power += HAND_POWER_BONUS
        self.afk_power += AFK_POWER_BONUS
        if self.current_target_level >= 5:
            self.current_target_level = 0
        self.current_target += 1
        self.current_target_level += 1

    def draw_stats(self, screen):
        for count, key_n_val in enumerate(self.__dict__.items()):
            key, val = key_n_val
            if key == 'money':
                text = ui.lower_font.render(str(key) + ': ' + str(format(val, '.0f')), True, BLACK)
            elif key == 'current_target_level':
                text = ui.lower_font.render('target_level' + ': ' + str(val), True, BLACK)
            else:
                text = ui.lower_font.render(str(key) + ': ' + str(val), True, BLACK)
            screen.blit(text, (10, 200 + 20 * count))

    def calculate_offline_money(self):
        offline_time = self.new_login - self.last_login
        while True:
            if self.last_player:
                money_earned = int(offline_time / 60 * afk_money)
                self.money += money_earned
                ui.show_offline_income(money_earned, offline_time)
            break


if __name__ == '__main__':
    print('This module is not for direct run!')
