# main module

import target
import player
import ui
from settings import *

import pygame as pg
from random import choice


def main():
    """
    Главная функция. Делает всё(почти).
    """
    screen = pg.display.set_mode((window_width, window_height))
    screen.fill(BLACK)
    pg.display.update()

    clock = pg.time.Clock()

    change_name_btn = ui.create_change_name_btn(screen)

    players = player.read_players_from_file(screen)
    current_player = player.define_current_player(players)

    current_target = target.Target(hp=INITIAL_TARGET_HP + current_player.targets_killed * TARGET_HP_MULTIPLIER)

    back_pict = choice(back_pictures)  # выбирает начальный фон

    finished = False

    while not finished:
        clock.tick(FPS)
        screen.fill(BLACK)
        ui.draw_back_picture(back_pict, screen)
        current_target.draw(screen)
        change_name_btn.draw()
        current_player.draw_stats(screen)

        for event in pg.event.get():

            change_name_btn.handle_event(event)

            if change_name_btn.clicked:
                new_data, new_name = ui.change_player(screen)
                change_name_btn.clicked = False
                if new_data:
                    players, current_player = player.handle_new_data(new_name, players, current_player)
                    current_target = target.Target(hp=target.calculate_hp(current_player.targets_killed))

            if event.type == pg.QUIT:
                finished = True

            if event.type == pg.MOUSEBUTTONDOWN:
                if current_target.check_click(event):
                    current_target.hurt(current_player.hand_power)

        current_target.hurt(current_player.afk_power / FPS)

        if current_target.died:
            current_player.power_up()
            current_target = target.Target(hp=target.calculate_hp(current_player.targets_killed))
        pg.display.update()

    current_player.last_player = True
    player.write_players_to_file(players)


if __name__ == '__main__':
    main()
    pg.quit()
