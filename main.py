# ----------------------IMPORTS------------------------
import pygame
import sys
# import Soldier
import consts
import game_field
import screen
import soldier
from game_field import add_mines_to_loc, add_random_mines

# endregion--------------------------------------------


state = {"is_window_open":True,
         "state": False}






def handle_user_events(row, col, list_of_grass_locations):

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_window_open"] = False

        # elif state["state"] != consts.RUNNING_STATE:
        #     continue
        new_row = row
        new_col = col
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                new_col += 1

            elif event.key == pygame.K_LEFT:
                new_col -= 1

            elif event.key == pygame.K_UP:
                new_row += 1

            elif event.key == pygame.K_DOWN:
                new_row += 1

            elif event.key == pygame.K_RETURN:
                screen.show_the_matrix_for_one_sec(list_of_grass_locations)
        soldier.is_valid_move(new_row, new_col)




def main():
    running = True
    game_field_matrix = game_field.create()
    mines_locations_list = game_field.add_random_mines(game_field_matrix)

    # list_of_grass_locations= screen.get_grass_location()
    # screen.open_screen(list_of_grass_locations)
    # screen.print_mines(mines_locations_list)


    for row in game_field_matrix:
        print(row)

    while running:
        soldier_loc = soldier.find_solider(game_field_matrix)

        soldier_row = soldier_loc[0]
        soldier_col = soldier_loc[1]
        # handle_user_events(soldier_row, soldier_col, list_of_grass_locations)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                state["is_window_open"] = False

            # elif state["state"] != consts.RUNNING_STATE:
            #     continue
            new_row = soldier_row
            new_col = soldier_col
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    new_col += 1

                elif event.key == pygame.K_LEFT:
                    new_col -= 1

                elif event.key == pygame.K_UP:
                    new_row += 1

                elif event.key == pygame.K_DOWN:
                    new_row += 1

                # elif event.key == pygame.K_RETURN:
                #     screen.show_the_matrix_for_one_sec(list_of_grass_locations)
                soldier.is_valid_move(new_row, new_col)
                if soldier.check_mine_collision(game_field_matrix, new_row, new_col):
                    screen.draw_lose_message()
            #         סגירת משחק
                if soldier.check_flag_collision(game_field_matrix,new_row, new_col):
                    screen.draw_win_message()
            #       סגירת משחק
                soldier.remove_old_soldier_location(game_field_matrix, soldier_row, soldier_col)

                soldier.add_new_soldier_location(game_field_matrix, new_row, new_col)
                for row in game_field_matrix:
                    print(row)
                    running = False

if __name__ == '__main__':
    main()