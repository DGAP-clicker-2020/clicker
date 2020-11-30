import ui


def create_menu_btn():
    """
    Функция создаёт кнопочку
    :return: экземпляр класс Button
    """
    return ui.Button(
        ui.screen,
        10,
        170,
        text='Menu',
        color=(51, 153, 255),
        hover_color=(235, 146, 37),
        clicked_color=(213, 23, 23),
        border_radius=5,
        border_width=2
    )


def menu_window(current_player):
    """
    Функция для вывода меню
    """
    return_btn = ui.Button(
        ui.screen,
        10,
        170,
        text='return',
        color=(51, 153, 255),
        hover_color=(235, 146, 37),
        clicked_color=(213, 23, 23),
        border_radius=5,
        border_width=2
    )

    hello_text = ui.pygame.font.Font('terminator.ttf', 45).render("MENU", True, ui.ORANGE)
    clock = ui.pygame.time.Clock()
    finished = False
    '''initial_money = player.get_init_money(current_player)'''
    # fixme сделать, чтобы при входе в меню, обновлялись деньги в меню

    while not finished:
        clock.tick(ui.FPS)
        ui.screen.fill(ui.BLACK)
        ui.draw_back_picture(ui.back_pict, ui.screen)
        ui.screen.blit(hello_text, ((ui.window_width - hello_text.get_width()) / 2, ui.window_width / 30))
        return_btn.draw()
        for event in ui.pygame.event.get():
            return_btn.handle_event(event)
            if return_btn.clicked:
                finished = True
            if event.type == ui.pygame.QUIT:
                finished = True

        current_money_text = ui.large_font.render('money: ' + str(current_player.money),
                                                  True, ui.BLACK)
        ui.screen.blit(current_money_text, (10, 70))
        ui.pygame.display.update()
