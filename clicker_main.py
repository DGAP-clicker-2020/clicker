# main module

from clicker_target import *
from clicker_player import *
from clicker_ui import *


def main():
    """
    Главная функция. Делает всё(почти).
    """
    screen = pygame.display.set_mode((window_width, window_height))
    screen.fill(BLACK)
    pygame.display.update()

    clock = pygame.time.Clock()

    change_name_btn = create_change_name_btn(screen)

    players = read_players_from_file(screen)
    current_player = define_current_player(players)

    target = Target(hp=INITIAL_TARGET_HP + current_player.targets_killed * TARGET_HP_MULTIPLIER)

    finished = False

    while not finished:
        clock.tick(FPS)
        screen.fill(BLACK)
        draw_back_picture('kpm_1.jpg', screen)
        target.draw(screen)
        change_name_btn.draw()
        current_player.draw_stats(screen)

        for event in pygame.event.get():
            new_data = False
            new_name = None
            try:
                new_data, new_name = change_name_btn.handle_event(event, screen)
            except TypeError:
                pass
            if new_data:
                players, current_player = handle_new_data(new_name, players, current_player)
                target = Target(hp=INITIAL_TARGET_HP + current_player.targets_killed * TARGET_HP_MULTIPLIER)

            if event.type == pygame.QUIT:
                finished = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if target.check_click(event):
                    target.hurt(current_player.hand_power)

        target.hurt(current_player.afk_power/FPS)

        if target.died:
            current_player.power_up()
            target = Target(hp=INITIAL_TARGET_HP + current_player.targets_killed * TARGET_HP_MULTIPLIER)
        pygame.display.update()

    current_player.last_player = True
    write_players_to_file(players)


if __name__ == '__main__':
    main()
    pygame.quit()
