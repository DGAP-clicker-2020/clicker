# main module
from clicker_target import *
from clicker_settings import *


def main():
    screen = pygame.display.set_mode((window_width, window_height))
    screen.fill((0, 0, 0))
    pygame.display.update()
    clock = pygame.time.Clock()
    power = 5

    target = Target()

    finished = False
    while not finished:
        clock.tick(FPS)
        screen.fill((0, 0, 0))
        target.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if target.check_click(event):
                    target.hurt(power)

                if target.died:
                    target = Target()

        pygame.display.update()




if __name__ == '__main__':
    main()
    pygame.quit()
