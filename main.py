#מגישים- נבו ברוך וברק ברמן
import pygame
import screen
import consts
import game_field
import grass_field
import time

state = {
    "is_window_open": True
}

def main():
    pygame.init()
    game_field.create()
    grass_field.create_grass_field()

    while state["is_window_open"]:
        handle_user_events()

        if not state["is_window_open"]:
            break
        elif is_lose():
            screen.draw_game_lose()
            time.sleep(3)
            break
        elif is_win():
            screen.draw_game_win()
            time.sleep(3)
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
                time.sleep(1)

def step_right():
    game_field.move_soldier(0, 1)
def step_left():
    game_field.move_soldier(0, -1)
def step_up():
    game_field.move_soldier(-1, 0)
def step_down():
    game_field.move_soldier(1, 0)

def show_mines():
    game_field.mine_glimpse()

def is_lose():
    upper_cells, lower_cells = game_field.get_soldier_cells()

    for row, col in lower_cells:
        for mine_row, mine_col in game_field.mines_positions:
            if (mine_row <= row < mine_row + consts.MINE_ROWS and mine_col <= col < mine_col + consts.MINE_COLS):
                return True
    return False

def is_win():
    upper_cells, lower_cells = game_field.get_soldier_cells()
    flag_cells = game_field.get_flag_cells()

    for soldier_cell in upper_cells:
        if soldier_cell in flag_cells:
            return True
    return False


main()
