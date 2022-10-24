import pygame
import screen
import constans
import soldier
import random
# import Screen
import numpy as np

location_mines_in_matrix = []
location_mines_in_pixl = []
default = 'Clear'
mine_field = np.tile(default, (constans.MINE_FIELD_ROWS, constans.MINE_FIELD_COLS))


def convert_location_to_pixl(location_matrix):  # only if they fill the same squares -mine, not soldier!!
    location_pixl = (int(location_matrix[1] * constans.SQUARE_WIDTH),
                     int(location_matrix[0] * constans.SQUARE_HEIGHT))
    return location_pixl


def set_flag_matrix_in_field():
    global mine_field
    for row in range(constans.MINE_FIELD_ROWS - constans.FLAG_ROWS - 1, constans.MINE_FIELD_ROWS - 1):
        for col in range(constans.MINE_FIELD_COLS - constans.FLAG_COLS, constans.MINE_FIELD_COLS):
            mine_field[row][col] = "FLAG"


def update_soldier_matrix_in_field():
    global mine_field
    location = soldier.soldier["location_matrix"]
    for row in range(location[0], location[0] + constans.SOLDIER_ROWS_MATRIX):
        for col in range(location[1], location[1] + constans.SOLDIER_COLS_MATRIX):
            mine_field[row][col] = "SOLDIER"


def clear_soldier_from_field():
    global mine_field
    for row in range(len(mine_field)):
        for col in range(len(mine_field[0])):
            if mine_field[row][col] == "SOLDIER":
                mine_field[row][col] = "Clear"


def add_mines_random():
    for i in range(constans.MINES_NUMBER):
        mine_location = random_mine_location()
        while not check_add_mine_possible(mine_location):
            mine_location = random_mine_location()
        add_a_mine(mine_location)


def random_mine_location():
    mine_row = random.randint(0, constans.MINE_FIELD_ROWS - constans.MINE_ROWS)
    mine_col = random.randint(0, constans.MINE_FIELD_COLS - constans.MINE_COLS)
    mine_matrix_location = (mine_row, mine_col)
    return mine_matrix_location


def add_a_mine(mine_location):
    global location_mines_in_pixl
    for i in range(constans.MINE_COLS):
        mine_field[mine_location[0]][mine_location[1] + i] = "MINE"
        location_mines_in_matrix.append((mine_location[0], mine_location[1] + i))
    location_mines_in_pixl.append(convert_location_to_pixl(mine_location))


def set_boom():
    boom_location = convert_location_to_pixl(soldier.get_legs_loc_in_field()[0])
    boom_image = constans.EXPLOTION_IMG
    screen.display_image(boom_image, constans.MINE_SIZE, boom_location)


def check_add_mine_possible(location):
    for i in range(constans.MINE_COLS):
        if mine_field[location[0]][location[1] + i] != 'Clear':
            return False
    return True


def check_soldier_on_mine():
    legs = soldier.get_legs_loc_in_field()
    if any(location in legs for location in location_mines_in_matrix):
        return True  # soldier will touch mine
    return False  # soldier will -not- touch mine


def check_soldier_on_flag():
    upper_body = soldier.get_body_loc_in_field()
    if any(location in upper_body for location in constans.FLAG_LOC_MATRIX_LIST):
        return True  # soldier will touch flag
    return False  # soldier will -not- touch flag
