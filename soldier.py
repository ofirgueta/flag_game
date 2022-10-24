import constans
import pygame
import mine_field

soldier = {}


def create():
    global soldier
    soldier = {"image": constans.SOLDIER_IMG,
               "location_matrix": constans.SOLDIER_START_LOCATION_MATRIX,  # top left index
               "location_pixel": constans.SOLDIER_START_LOCATION_PIXL  # top left index
               }


def update_location_matrix(location_matrix):
    global soldier
    soldier["location_matrix"] = location_matrix


def update_location_pixel(location_pixel):
    global soldier
    soldier["location_pixel"] = location_pixel


def update_image(image):
    global soldier
    soldier["image"] = image


def move_to(key):
    if key == "RIGHT":
        if check_right_border():
            move_to_right()
    elif key == "LEFT":
        if check_left_border():
            move_to_left()
    elif key == "UP":
        if check_up_border():
            move_up()
    elif key == "DOWN":
        if check_down_border():
            move_down()


def check_left_border():
    top_left = soldier["location_pixel"]
    if top_left[0] - constans.SQUARE_WIDTH < 0:
        return False
    return True


def check_up_border():
    top_left = soldier["location_pixel"]
    if top_left[1] - constans.SQUARE_HEIGHT < 0:
        return False
    return True


def check_right_border():
    top_left = soldier["location_pixel"]
    bottem_right = (top_left[0] + (4 * constans.SQUARE_WIDTH), top_left[1] + (4 * constans.SQUARE_HEIGHT))
    if bottem_right[0] + constans.SQUARE_WIDTH > constans.WINDOW_WIDTH:
        return False
    return True


def check_down_border():
    top_left = soldier["location_pixel"]
    bottem_right = (top_left[0] + (4 * constans.SQUARE_WIDTH), top_left[1] + (4 * constans.SQUARE_HEIGHT))
    if bottem_right[1] + constans.SQUARE_HEIGHT > constans.WINDOW_HEIGHT:
        return False
    return True


def move_to_right():
    location_matrix = soldier["location_matrix"]
    location_pixel = soldier["location_pixel"]
    update_location_matrix((location_matrix[0], location_matrix[1] + constans.STEP))
    update_location_pixel((location_pixel[0] + constans.SQUARE_WIDTH, location_pixel[1]))
    print(soldier["location_pixel"])
    print(soldier["location_matrix"])


def move_to_left():
    location_matrix = soldier["location_matrix"]
    location_pixel = soldier["location_pixel"]
    update_location_matrix((location_matrix[0], location_matrix[1] - constans.STEP))
    update_location_pixel((location_pixel[0] - constans.SQUARE_WIDTH, location_pixel[1]))
    print(soldier["location_pixel"])
    print(soldier["location_matrix"])


def move_up():
    location_matrix = soldier["location_matrix"]
    location_pixel = soldier["location_pixel"]
    update_location_matrix((location_matrix[0] - constans.STEP, location_matrix[1]))
    update_location_pixel((location_pixel[0], location_pixel[1] - constans.SQUARE_HEIGHT))
    print(soldier["location_pixel"])
    print(soldier["location_matrix"])


def move_down():
    location_matrix = soldier["location_matrix"]
    location_pixel = soldier["location_pixel"]
    update_location_matrix((location_matrix[0] + constans.STEP, location_matrix[1]))
    update_location_pixel((location_pixel[0], location_pixel[1] + constans.SQUARE_HEIGHT))
    print(soldier["location_pixel"])
    print(soldier["location_matrix"])


def get_legs_loc_in_field():
    legs_loc_list = []
    top_left = soldier["location_matrix"]  # top left(x,y)
    bottem_left = (top_left[0] + 3, top_left[1])
    for row in range(1):
        for col in range(2):
            legs_loc_list.append((bottem_left[0], bottem_left[1] + col))
    return legs_loc_list


def get_body_loc_in_field():
    body_loc_list = []
    top_left = soldier["location_matrix"]
    for row in range(3):
        for col in range(2):
            body_loc_list.append((top_left[0] + row, top_left[1] + col))
    return body_loc_list
