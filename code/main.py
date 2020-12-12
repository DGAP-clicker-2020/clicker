import time
import pygame as pg

import auxiliary_functions
import player
import target
import ui
import menu
import shop
import music
from settings import *


def draw_objects(current_player, current_target, change_name_btn, menu_open_btn, shop_open_btn):
    """
    Функция прорисовывает переданные ей объекты
    """
    ui.draw_back_picture(BACK_PICTURES[current_player.player_back_pict], ui.screen)
    current_target.draw(ui.screen)
    change_name_btn.draw()
    menu_open_btn.draw()
    shop_open_btn.draw()


def main():
    """
    Главная функция. Делает всё(почти).
    """
    clock = pg.time.Clock()
    change_name_btn = ui.create_change_name_btn()
    menu_open_btn = menu.create_menu_btn()
    shop_open_btn = shop.create_shop_btn()

    players = player.read_players_from_file()
    current_player = player.define_current_player(players)

    current_target = target.Target(hp=auxiliary_functions.calculate_hp(current_player.current_target))

    finished = False

    while not finished:
        clock.tick(FPS)

        draw_objects(current_player, current_target, change_name_btn, menu_open_btn, shop_open_btn)

        ui.show_money(current_player.money, SONICBT_FONT_PATH, 40, GOLD, BLACK, WINDOW_WIDTH, 145)
        music.set_all_volume(music.all_sounds, current_player.audio_volume)

        for event in pg.event.get():

            change_name_btn.handle_event(event)
            menu_open_btn.handle_event(event)
            shop_open_btn.handle_event(event)

            if change_name_btn.left_clicked:
                music.pick_snd.play()
                new_data, new_name = ui.change_player()
                change_name_btn.left_clicked = False
                if new_data:
                    players, current_player = player.handle_new_data(new_name, players, current_player)
                    current_target = target.Target(hp=auxiliary_functions.calculate_hp(current_player.current_target))

            if menu_open_btn.left_clicked:
                music.pick_snd.play()
                menu_open_btn.left_clicked = False
                menu.menu_window(current_player)

            if shop_open_btn.left_clicked:
                music.pick_snd.play()
                shop_open_btn.left_clicked = False
                shop.shop_window(current_player)

            if event.type == pg.QUIT:
                finished = True

            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                if current_target.check_click(event):
                    current_target.hurt(current_player.hand_power, current_player.critical_chance,
                                        current_player.critical_multiplier)
                    current_player.total_clicks += 1
                    current_player.total_damage += current_player.hand_power

            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                current_target.hurt(current_player.hand_power, current_player.critical_chance,
                                    current_player.critical_multiplier)
                current_target.hit_snd.play()

        current_target.afk_hurt(current_player.afk_power / FPS)
        current_player.total_damage += current_player.afk_power / FPS

        if current_target.died:
            current_player.power_up()
            current_target = target.Target(hp=auxiliary_functions.calculate_hp(current_player.current_target))

        pg.display.update()

    current_player.last_player = True
    current_player.last_login = int(time.time())
    player.write_players_to_file(players)


if __name__ == '__main__':
    try:
        main()
    finally:
        pg.quit()
