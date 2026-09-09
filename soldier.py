import pygame

from consts import BOARD_ROWS, BOARD_COLS, SOLDIER_ROWS, SOLDIER_COLS, \
    SOLDIER_BODY_ROWS, SOLDIER_FEET_ROWS

'''create a new solider'''
def create_solider():
    return {"img": pygame.image.load('soldier.png'),
            "list_of_body_position":[(0,0),(1,0),(0,1),(1,1),(0,2),(1,2)] ,
            "list_of_legs_position":[(0,3),(1,3)],

    }
'''find left corner of the soldier'''
def find_solider(game_field):
    for i in range(BOARD_ROWS):
        for j in range(BOARD_COLS):
            if game_field[i][j]=="SOLDIER_BODY":
                return (i,j)

'''checks if soldier stays in the matrix'''
def is_valid_move(row,col):
    if row<0 or row+SOLDIER_ROWS>BOARD_ROWS:
        return False
    if col<0 or col+SOLDIER_COLS>BOARD_COLS:
        return False
    return True

'''checks if the soldier legs touches the mine'''
def check_mine_collision(game_field,row,col):
    feet_row=row+SOLDIER_BODY_ROWS
    for i in range (col,col+SOLDIER_COLS):
        if game_field[feet_row][i]=="MINE":
            return True
    return False

'''DELETE THE SOLIDER FROM OLD LOCATION'''
def remove_old_soldier_location(game_field,row,col):
    for i in range(row,row+SOLDIER_ROWS):
        for j in range(col,col + SOLDIER_COLS):
            game_field[i][j]="FREE"

'''add solider to new location'''
def add_new_soldier_location(game_field,row,col):
    for i in range(row,row+SOLDIER_BODY_ROWS):
        for j in range(col,col+SOLDIER_COLS):
            game_field[i][j]=="SOLDIER_BODY"
    for i in range(col, col+SOLDIER_COLS):
        game_field[row+SOLDIER_BODY_ROWS][i]="SOLDIER_FEET"

def check_flag_collision(game_field, row, col):
    for i in range(row, row+ SOLDIER_BODY_ROWS):
        for j in range(col, col + SOLDIER_COLS):
            if game_field[i][j] == "FLAG":
                return True
    return False


