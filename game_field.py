# region--------------------IMPORTS-----------------------
import consts

# endregion-----------------------------------------------

game_field = []

def create():
    row_list = []
    for i in range(consts.BOARD_ROWS):
        for j in range(consts.BOARD_COLS):
            row_list.append("FREE")
        game_field.append(row_list)


def add_soldier_to_matrix():
    for i in range(consts.SOLDIER_BODY_ROWS):
        for j in range(consts.SOLDIER_COLS):
            game_field[i][j] = "SOLDIER_BODY"

    for i in range(consts.SOLDIER_FEET_ROWS):
        for j in range(consts.SOLDIER_COLS):
            game_field[i][j] = "SOLDIER_FEET"

