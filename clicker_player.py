from clicker_settings import *

from random import randint
import json


def read_players_from_file():
    file = open('players.json', 'r')
    new_dict = json.load(file)
    players = []
    for val in new_dict.values():
        val = json.loads(val)
        players.append(Player(name=val['name'],
                              id_num=int(val['id_num']),
                              hand_power=int(val['hand_power']),
                              last_player=bool(val['last_player']),
                              targets_killed=int(val['targets_killed']),
                              afk_power=float(val['afk_power'])))
    return players


def define_current_player(players):
    for pl in players:
        if pl.last_player:
            return pl


def write_players_to_file(players):
    with open('players.json', 'w') as file:
        dic = {}
        for i, pl in enumerate(players):
            dic[i] = pl.to_json()
        json.dump(dic, file)


class Player:

    def __init__(self,
                 name='Arseniy',
                 id_num=randint(1, 1000),
                 hand_power=1,
                 last_player=True,
                 targets_killed=0,
                 afk_power=0.0):
        self.name = name
        self.id_num = id_num
        self.hand_power = hand_power
        self.afk_power = afk_power
        self.last_player = last_player
        self.targets_killed = targets_killed

    def to_json(self):
        return json.dumps(self.__dict__)


if __name__ == '__main__':
    print('This module is not for direct run!')
