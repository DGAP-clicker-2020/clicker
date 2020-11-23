from clicker_ui import *

from random import randint
import json


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
            really_new_player = False
    if really_new_player:
        current_player = Player(name=new_name)
        players.append(current_player)
    return players, current_player


def read_players_from_file(screen):
    """
    Функция считывает игроков из базы данных
    :rtype: list
    :param screen: экран
    :return: список игроков
    """
    players = []
    try:
        file = open('players.json', 'r')
        new_dict = json.load(file)
        file.close()
        for val in new_dict.values():
            players.append(Player(name=val['name'],
                                  id_num=val['id_num'],
                                  hand_power=val['hand_power'],
                                  last_player=val['last_player'],
                                  targets_killed=val['targets_killed'],
                                  afk_power=val['afk_power']))
    except (json.JSONDecodeError, FileNotFoundError):
        pass
    if not players:
        new_data, new_name = change_player(screen)
        if not new_data:
            players.append(Player(name='Sample Name',
                                  last_player=True))
        else:
            players.append(Player(name=new_name,
                                  last_player=True))
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
        for i, pl in enumerate(players):
            dic[i] = pl.__dict__
        json.dump(dic, file)


class Player:

    def __init__(self,
                 name='Sample Name',
                 id_num=randint(1, 1000),
                 hand_power=1,
                 last_player=False,
                 targets_killed=0,
                 afk_power=0.0):
        """
        Сборщик экземпляра класса Player
        :param name: имя
        :param id_num: идентификационный номер
        :param hand_power: сила клика
        :param last_player: Флаг-статус последнего игрока
        :param targets_killed: Колличество убитых целей
        :param afk_power: Урон каждую секунду
        """
        self.name = name
        self.id_num = id_num
        self.hand_power = hand_power
        self.afk_power = afk_power
        self.last_player = last_player
        self.targets_killed = targets_killed

    def power_up(self):
        """
        Улучшение игрока после уничтожения цели
        """
        self.hand_power += HAND_POWER_BONUS
        self.afk_power += AFK_POWER_BONUS
        self.targets_killed += 1

    def draw_stats(self, screen):
        for i, key_n_val in enumerate(self.__dict__.items()):
            key, val = key_n_val
            text = lower_font.render(str(key)+': '+str(val), 0, (0, 160, 255))
            screen.blit(text, (250, 100 + 30 * i))


if __name__ == '__main__':
    print('This module is not for direct run!')
