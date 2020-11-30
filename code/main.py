# main module

import time
import pygame as pg
import player
import target
import ui
import menu
from settings import *


def main():
    """
    Главная функция. Делает всё(почти).
    """
    clock = pg.time.Clock()

    change_name_btn = ui.create_change_name_btn()
    menu_open_btn = menu.create_menu_btn()

    players = player.read_players_from_file()
    current_player = player.define_current_player(players)

    current_target = target.Target(hp=INITIAL_TARGET_HP + current_player.current_target * TARGET_HP_MULTIPLIER)

    back_pict = back_pictures[current_player.player_back_pict]  # выбирает задний фон

    finished = False

    while not finished:
        clock.tick(FPS)
        ui.screen.fill(BLACK)
        ui.draw_back_picture(back_pict, ui.screen)
        current_target.draw(ui.screen)
        change_name_btn.draw()
        menu_open_btn.draw()
        current_player.draw_stats(ui.screen)

        for event in pg.event.get():

            change_name_btn.handle_event(event)
            menu_open_btn.handle_event(event)

            if change_name_btn.clicked:
                player.write_players_to_file(players)
                new_data, new_name = ui.change_player()
                change_name_btn.clicked = False
                if new_data:
                    players, current_player = player.handle_new_data(new_name, players, current_player)
                    current_target = target.Target(hp=target.calculate_hp(current_player.current_target))

            if menu_open_btn.clicked:
                menu.menu_window(current_player)

            if event.type == pg.QUIT:
                finished = True

            if event.type == pg.MOUSEBUTTONDOWN:
                if current_target.check_click(event):
                    current_target.hurt(current_player.hand_power)

        current_target.hurt(current_player.afk_power / FPS)

        if current_target.died:
            current_player.power_up()
            current_target = target.Target(hp=target.calculate_hp(current_player.current_target))
        pg.display.update()

    current_player.last_player = True
    current_player.last_login = int(time.time())
    player.write_players_to_file(players)


if __name__ == '__main__':
    main()
    pg.quit()
