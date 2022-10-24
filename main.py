import pygame
import screen
import constans
import soldier
import mine_field

state = {
    "is_window_open": True,
    "state": constans.RUNNING_STATE,  # 1
    "soldier_to": "",
    "enter_pressed": False,
    "on_mine": False,
    "on_flag": False,
    "win": False,
    "lose": False,

}


def main():
    pygame.init()
    soldier.create()
    generate_permanents()
    screen.draw_game()
    while state["is_window_open"]:

        handle_user_events()

        if state["enter_pressed"]:
            screen.draw_k_enter()
            pygame.time.delay(1 * 1000)
            soldier.update_image(constans.SOLDIER_IMG)
            screen.draw_game()
            state["enter_pressed"] = False

        if state["soldier_to"]:
            soldier.move_to(state["soldier_to"])
            screen.draw_game()
            if mine_field.check_soldier_on_flag():
                state["win"] = True
            elif mine_field.check_soldier_on_mine():
                state["lose"] = True
        state["soldier_to"] = ""

        if state["win"]:
            win()

        if state["lose"]:
            lose()

    screen.draw_game()


def handle_user_events():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_window_open"] = False

        elif state["state"] != constans.RUNNING_STATE:
            continue
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                state["soldier_to"] = "UP"

            elif event.key == pygame.K_DOWN:
                state["soldier_to"] = "DOWN"

            elif event.key == pygame.K_LEFT:
                state["soldier_to"] = "LEFT"

            elif event.key == pygame.K_RIGHT:
                state["soldier_to"] = "RIGHT"

            elif event.key == pygame.K_RETURN:
                state["enter_pressed"] = True


def win():
    screen.draw_message("you win", (int(constans.WINDOW_WIDTH/2), int(constans.WINDOW_HEIGHT/2)))
    state["state"] = constans.WIN_STATE
    state["is_window_open"] = False


def lose():
    screen.set_screen()
    screen.display_grass()
    mine_field.set_boom()
    soldier.update_image(constans.INJURY_IMG)
    screen.display_soldier()
    screen.draw_message("you lose", (int(constans.WINDOW_WIDTH/2), int(constans.WINDOW_HEIGHT/2)))
    state["state"] = constans.LOSE_STATE
    state["is_window_open"] = False


def generate_permanents():
    screen.grass_locations()
    mine_field.clear_soldier_from_field()
    mine_field.update_soldier_matrix_in_field()
    mine_field.set_flag_matrix_in_field()
    mine_field.add_mines_random()


if __name__ == '__main__':
    main()
