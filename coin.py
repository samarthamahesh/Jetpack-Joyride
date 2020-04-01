import random
from base import DIMENSION, COLOR
from colorama import Fore, Style

class Coins:

    def __init__(self, xcoord, ycoord, dim):
        self.__xcoord = xcoord
        self.__ycoord = ycoord
        self.__dim = dim
        self.__coins_left = self.__dim['x'] * self.__dim['y']
        self.__coin_shape = COLOR['coin'] + '$' + Style.RESET_ALL
        self.__shape = [[self.__coin_shape for _ in range(self.__dim['y'])] for _ in range(self.__dim['x'])]

    def place_coins(self, grid):
        for i in range(self.__dim['x']):
            for j in range(self.__dim['y']):
                grid[self.__xcoord+i][self.__ycoord+j] = self.__shape[i][j]

    def remove_coin(self, coord):
        self.__shape[coord[0]][coord[1]] = ' '
        self.__coins_left -= 1

    def get_xcoord(self):
        return self.__xcoord

    def get_ycoord(self):
        return self.__ycoord

    def get_dim(self):
        return self.__dim

    def get_coins_left(self):
        return self.__coins_left

    def get_coin_shape(self):
        return self.__coin_shape

    def get_shape(self):
        return self.__shape

def create_coins():

    x = DIMENSION['sky_height'] + random.randint(1, 3)
    y = random.randint(50, 100)
    obj_list = []

    while y < DIMENSION['width'] - DIMENSION['frame_width']:
        dim = {}
        dim['x'] = random.randint(1, 5)
        dim['y'] = random.randint(1, 5)
        coins = Coins(x, y, dim)
        obj_list.append(coins)
        x = DIMENSION['sky_height'] + random.randint(2, 10)
        y += random.randint(30, 50)

    return obj_list

def place_coins(obj_list, grid, xdis):
    
    for coins in obj_list:
        if coins.get_ycoord() > xdis + DIMENSION['frame_width']:
            break
        elif coins.get_ycoord() < xdis - coins.get_dim()['y']:
            obj_list.remove(coins)
        elif coins.get_coins_left() == 0:
            obj_list.remove(coins)
        else:
            coins.place_coins(grid)