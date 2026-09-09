# region--------------------IMPORTS-----------------------
from turtledemo.clock import jump

import consts
import random

import screen
from consts import BOARD_ROWS, BOARD_COLS, MINE_ROWS, MINE_COLS, MINES_COUNT


# endregion-----------------------------------------------


def create():

    game_field = [["FREE" for col in range(consts.BOARD_COLS)] for row in range(consts.BOARD_ROWS)]
    add_soldier_to_matrix(game_field)
    add_flag_to_matrix(game_field)
    # add_random_mines(game_field)
    return game_field

''' add soldier to the left top in the matrix'''
def add_soldier_to_matrix(game_field):
    # add soldier body
    for i in range(consts.SOLDIER_BODY_ROWS):
        for j in range(consts.SOLDIER_COLS):
            game_field[i][j] = "SOLDIER_BODY"
    # add soldier feet
    for i in range(consts.SOLDIER_BODY_ROWS, consts.SOLDIER_BODY_ROWS + consts.SOLDIER_FEET_ROWS):
        for j in range(consts.SOLDIER_COLS):
            game_field[i][j] = "SOLDIER_FEET"

''' add fleg to the right bottom in the matrix'''
def add_flag_to_matrix(game_field):
    for i in range(consts.BOARD_ROWS - consts.FLAG_ROWS, consts.BOARD_ROWS):
        for j in range(consts.BOARD_COLS - consts.FLAG_COLS, consts.BOARD_COLS):
            game_field[i][j] = "FLAG"

''' add mines in random locations to the matrix'''
def add_random_mines(game_field):
    mines_locations = []

    for i in range(consts.MINES_COUNT):
        mine_row = get_random_matrix_location(0, consts.BOARD_ROWS,
                                              consts.MINE_ROWS)
        mine_col = get_random_matrix_location(0, consts.BOARD_COLS,
                                              consts.MINE_COLS)

        while not check_free(game_field, mine_row, mine_col):
            mine_row = get_random_matrix_location(0, consts.BOARD_ROWS,
                                                  consts.MINE_ROWS)
            mine_col = get_random_matrix_location(0, consts.BOARD_COLS,
                                                  consts.MINE_COLS)

        mines_locations.append((mine_row, mine_col))
        add_mines_to_loc(game_field, mine_row, mine_col)

    return mines_locations


''''''
def add_mines_to_loc(game_field ,row , col):
    for i in range(row, row + MINE_ROWS):
        for j in range(col,col + MINE_COLS):
            game_field[i][j] = "MINE"

def check_free(game_field, row, col):
    for i in range(row, row + consts.MINE_ROWS):
        for j in range(col, col + consts.MINE_COLS):
            if game_field[i][j] != "FREE":
                return False
    return True

def get_random_matrix_location(start, range, jumps):
    random_in_range = random.randrange(start, range, jumps)
    while random_in_range + jumps > range:
        random_in_range = random.randrange(start, range, jumps)
    return random_in_range


