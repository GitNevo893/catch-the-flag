#מגישים- נבו ברוך וברק ברמן
import pygame
import screen
import consts
import game_field
import grass_field

# flag_pic = screen.create_flag(consts.FLAG_IMG)
# grass_pic = screen.create_grass(consts.GRASS_IMG)
# soldier_pic = screen.create_grass(consts.SOLDIER_IMG)
# mine_pic = screen.create_mine(consts.MINE_IMG)
state = {
    "is_window_open": True,
    # "flag_pic": flag_pic,
    # "grass_pic": grass_pic,
    # "soldier_pic": soldier_pic,
    # "mine_pic": mine_pic
}

def main():
    pygame.init()
    game_field.create()

    grass_field.create_grass_field()
    grass_field.draw_grass_field()

    while state["is_window_open"]:
        handle_user_events()

        if not state["is_window_open"]:
            break

        screen.draw_game()

def handle_user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["is_window_open"] = False
            return

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("pressed UP arrow")
                step_up()
            elif event.key == pygame.K_DOWN:
                print("pressed DOWN arrow")
                step_down()
            elif event.key == pygame.K_RIGHT:
                print("pressed RIGHT arrow")
                step_right()
            elif event.key == pygame.K_LEFT:
                print("pressed LEFT arrow")
                step_left()
            elif event.key == pygame.K_RETURN:
                print("pressed ENTER")
                show_mines()

def step_right():
    game_field.move_soldier(0, 1)

def step_left():
    game_field.move_soldier(0, -1)

def step_up():
    game_field.move_soldier(-1, 0)

def step_down():
    game_field.move_soldier(1, 0)

def show_mines():

    #TODO
    pass

main()
