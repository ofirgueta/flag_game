from random import randrange
import soldier
import pygame
import pygame as pygame
import mine_field

import constans
import math
import sys
import os
from pygame.locals import *

global grass_list
grass_list = []
screen = pygame.display.set_mode(
    (constans.WINDOW_WIDTH, constans.WINDOW_HEIGHT))


def set_screen():
    pygame.display.set_caption('FLAG GAME')
    screen.fill(constans.BACKGROUND_COLOR)


def display_image(image_path, size, location):
    image = pygame.image.load(image_path)
    sized_image = pygame.transform.scale(image, size)
    screen.blit(sized_image, location)


def display_grass():
    for location in grass_list:
        display_image(constans.GRASS_IMG, constans.GRASS_SIZE, location)


def grass_locations():
    global grass_list
    for i in range(20):
        grass_list.append(((randrange(constans.WINDOW_WIDTH - constans.GRASS_SIZE[0]),
                            randrange(constans.WINDOW_HEIGHT - constans.GRASS_SIZE[1]))))


def display_mines():
    for location in mine_field.location_mines_in_pixl:
        display_image(constans.MINE_IMG, constans.MINE_SIZE, location)


def display_flag():
    display_image(constans.FLAG_IMG, constans.FlAG_SIZE, constans.FLAG_LOCATION_PIXL)


def draw_message(text, location):
    WHITE = (200, 200, 200)
    font = pygame.font.SysFont(None, 24)
    img = font.render(text, True, WHITE)
    screen.blit(img, location)
    pygame.display.update()
    pygame.time.delay(2 * 1000)


def draw_grid():
    blockSizeX = int(constans.SQUARE_WIDTH)
    blockSizeY = int(constans.SQUARE_HEIGHT)  # Set the size of the grid block
    for x in range(0, constans.WINDOW_WIDTH, blockSizeX):
        for y in range(0, constans.WINDOW_HEIGHT, blockSizeY):
            rect = pygame.Rect(x, y, blockSizeX, blockSizeY)
            pygame.draw.rect(screen, constans.BRIGHT_GREEN, rect, 1)
    pygame.display.update()


def draw_k_enter():
    screen.fill(constans.BLACK)
    soldier.update_image(constans.SOLDIER_NIGHT_IMG)
    display_soldier()
    draw_grid()
    display_mines()
    pygame.display.update()


def display_soldier():
    location = soldier.soldier["location_pixel"]
    image = soldier.soldier["image"]
    display_image(image, constans.SOLDIER_SIZE, location)


def draw_game():
    set_screen()
    display_grass()
    display_flag()
    mine_field.update_soldier_matrix_in_field()
    display_soldier()
    pygame.display.update()
