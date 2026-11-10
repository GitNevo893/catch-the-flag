#מגישים- נבו ברוך וברק ברמן
import pygame

state = {
    "is_window_open": True,
    "state": consts.RUNNING_STATE
}

def main():

    #TODO
    pass


def handle_user_events():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_window_open"] = False
            return
        elif state["state"] != consts.RUNNING_STATE:
            continue

        if event.type == pygame.K_UP:
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
