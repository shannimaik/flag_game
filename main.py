# ----------------------IMPORTS------------------------
import pygame
import sys
# import Soldier
import consts
import screen
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
    list_of_grass_locations= screen.get_grass_location()
    screen.open_screen(list_of_grass_locations)
    while running:
        handle_user_events(list_of_grass_locations)


if __name__ == '__main__':
    main()