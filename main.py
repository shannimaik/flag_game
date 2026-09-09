# ----------------------IMPORTS------------------------
import pygame
import sys
# import Soldier
import consts
import game_field
import screen
from game_field import add_mines_to_loc, add_random_mines

# endregion--------------------------------------------


state = {"is_window_open":True,
         "state": False}






def handle_user_events(list_of_grass_locations):

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_window_open"] = False

        # elif state["state"] != consts.RUNNING_STATE:
        #     continue

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                pass

            elif event.key == pygame.K_LEFT:
                pass

            elif event.key == pygame.K_UP:
                pass

            elif event.key == pygame.K_DOWN:
                pass
            elif event.key == pygame.K_RETURN:
                screen.show_the_matrix_for_one_sec(list_of_grass_locations)



def main():
    running = True
    game_field_matrix = game_field.create()
    mines_locations_list = game_field.add_random_mines(game_field_matrix)
    print(mines_locations_list)
    list_of_grass_locations= screen.get_grass_location()
    screen.open_screen(list_of_grass_locations)
    screen.print_mines(mines_locations_list)
    for row in game_field_matrix:
        print(row)
    while running:
        handle_user_events(list_of_grass_locations)


if __name__ == '__main__':
    main()