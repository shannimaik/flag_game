# region--------------------IMPORTS-----------------------
import consts

# endregion-----------------------------------------------


def create():

    game_field = [["FREE" for col in range(consts.BOARD_COLS)] for row in range(consts.BOARD_ROWS)]
    add_soldier_to_matrix(game_field)
    add_flag_to_matrix(game_field)
    return game_field

def add_soldier_to_matrix(game_field):
    for i in range(consts.SOLDIER_BODY_ROWS):
        for j in range(consts.SOLDIER_COLS):
            game_field[i][j] = "SOLDIER_BODY"

    for i in range(consts.SOLDIER_BODY_ROWS, consts.SOLDIER_BODY_ROWS + consts.SOLDIER_FEET_ROWS):
        for j in range(consts.SOLDIER_COLS):
            game_field[i][j] = "SOLDIER_FEET"

def add_flag_to_matrix(game_field):
    for i in range(consts.BOARD_ROWS - consts.FLAG_ROWS, consts.BOARD_ROWS):
        for j in range(consts.BOARD_COLS - consts.FLAG_COLS, consts.BOARD_COLS):
            game_field[i][j] = "FLAG"

matrix = create()
for row in matrix:
    print(row)