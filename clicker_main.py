# main module

from clicker_target import *
from clicker_player import *
from clicker_ui import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((window_width, window_height))
    screen.fill(BLACK)
    pygame.display.update()
    clock = pygame.time.Clock()
    change_name_btn = create_change_name_btn(screen)


    players = read_players_from_file(screen)
    current_player = define_current_player(players)

    target = Target(hp=10 + current_player.targets_killed*3)

    finished = False

    while not finished:
        clock.tick(FPS)
        screen.fill(BLACK)
        target.draw(screen)
        change_name_btn.draw()

        for event in pygame.event.get():
            new_data, new_name = change_name_btn.handle_event(event, screen)
            if new_data:
                players, current_player = handle_new_data(new_name, players, current_player)
                target = Target(hp=30 + current_player.targets_killed * 3)


            if event.type == pygame.QUIT:
                finished = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if target.check_click(event):
                    target.click_hurt(current_player.hand_power)

        target.afk_hurt(current_player.afk_power/FPS)

        if target.died:
            current_player.hand_power += 1
            current_player.afk_power += 0.5
            current_player.targets_killed += 1
            target = Target(hp=30 + current_player.targets_killed * 3)

        pygame.display.update()

    current_player.last_player = True
    write_players_to_file(players)



if __name__ == '__main__':
    main()
    pygame.quit()
