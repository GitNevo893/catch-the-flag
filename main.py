#מגישים- נבו ברוך וברק ברמן
import pygame
import screen
import consts

state = {
    "is_window_open": True,
    "flag_pic": screen.create_flag(consts.FLAG_IMG),
    "grass_pic": screen.create_grass(consts.GRASS_IMG),
    "soldier_pic": screen.create_grass(consts.SOLDIER_IMG),
    "mine_pic": screen.create_mine(consts.MINE_IMG)
}

def main():
    pygame.init()

    while state["is_window_open"]:

        handle_user_events()

        if not state["is_window_open"]:
            break

        screen.draw_game(state)



def handle_user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["is_window_open"] = False
            return
        elif event.type == pygame.K_UP:
            print("pressed UP arrow")
            step_up()
        elif event.type == pygame.K_DOWN:
            print("pressed DOWN arrow")
            step_down()
        elif event.type == pygame.K_RIGHT:
            print("pressed RIGHT arrow")
            step_right()
        elif event.type == pygame.K_LEFT:
            print("pressed LEFT arrow")
            step_left()
        elif event.type == pygame.K_RETURN:
            print("pressed ENTER")
            show_mines()

def step_right():

    #TODO
    pass

def step_left():

    #TODO
    pass

def step_up():

    #TODO
    pass

def step_down():

    #TODO
    pass

def show_mines():

    #TODO
    pass

main()
