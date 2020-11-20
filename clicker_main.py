# main module

from clicker_target import *
from clicker_player import *
from button import Button


def change_player(screen):
    f2 = pygame.font.SysFont('serif', 60)
    f1 = pygame.font.SysFont('serif', 60)
    text2 = f1.render("Введите ваше имя", 0, (0, 180, 0))
    pygame.display.update()
    clock = pygame.time.Clock()

    f = True
    finished = False

    string = ''
    while not finished:
        while f:
            clock.tick(FPS)
            screen.fill(BLACK)
            screen.blit(text2, (10, 10))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                    f = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        f = False
                        finished = True
                        break
                    elif event.key == 8:
                        string = string[:-1]
                    else:
                        string += event.unicode
            text3 = f2.render(string, 0, (200, 0, 0))
            screen.blit(text3, (10, 70))
            pygame.display.update()


def main():
    pygame.init()
    screen = pygame.display.set_mode((window_width, window_height))
    screen.fill(BLACK)
    pygame.display.update()
    clock = pygame.time.Clock()

    btn = Button(
        screen,
        10,
        130,
        change_player,
        text='Change player',
        color=(200, 200, 200),
        hover_color=(235, 146, 37),
        clicked_color=(213, 23, 23),
        border_radius=5,
        border_width=2
    )

    players = read_players_from_file()
    current_player = define_current_player(players)

    target = Target(hp=10 + current_player.targets_killed*3)

    finished = False

    while not finished:
        clock.tick(FPS)
        screen.fill(BLACK)
        target.draw(screen)
        btn.draw()

        for event in pygame.event.get():
            btn.handle_event(event, screen)
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
