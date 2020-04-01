import random
from colorama import Fore, Style
from base import DIMENSION, COLOR

class PowerUp:

    def __init__(self, xcoord, ycoord):
        self._xcoord = xcoord
        self._ycoord = ycoord
        self._dim = {}
        self._dim['x'] = 1
        self._dim['y'] = 2
        self._shape = COLOR['powerup'] + '>' + Style.RESET_ALL
        
    def place(self, grid):
        for i in range(self._dim['x']):
            for j in range(self._dim['y']):
                grid[self._xcoord+i][self._ycoord+j] = self._shape

    def get_xcoord(self):
        return self._xcoord

    def get_ycoord(self):
        return self._ycoord

    def get_dim(self):
        return self._dim

    def get_shape(self):
        return self._shape

def create_powerups():
    x = DIMENSION['sky_height'] + random.randint(5, 15)
    y = random.randint(100, 120)
    obj_list = []

    while y < 3 * DIMENSION['width'] // 4:
        powerup = PowerUp(x, y)
        obj_list.append(powerup)
        x = DIMENSION['sky_height'] + random.randint(5, 15)
        y += random.randint(100, 300)

    return obj_list

def place_powerups(obj_list, grid, xdis):
    for powerup in obj_list:
        if powerup.get_ycoord() > xdis + DIMENSION['frame_width']:
            break
        elif powerup.get_ycoord() < xdis - powerup.get_dim()['y']:
            obj_list.remove(powerup)
        else:
            powerup.place(grid)

class Dragon_Power(PowerUp):

    def __init__(self, xcoord, ycoord):
        PowerUp.__init__(self, xcoord, ycoord)
        self._shape = COLOR['dragon_powerup'] + 'D' + Style.RESET_ALL

    def remove(self, grid):
        for i in range(self._dim['x']):
            for j in range(self._dim['y']):
                grid[self._xcoord+i][self._ycoord+j] = ' '

def create_dragon_powerup():
    x = DIMENSION['length'] - 2*DIMENSION['ground_height']
    y = random.randint(DIMENSION['width'] // 3, 2 * DIMENSION['width'] // 3)
    dragon_powerup = Dragon_Power(x, y)
    return dragon_powerup

def place_dragon_powerup(dragon_powerup, grid):
    dragon_powerup.place(grid)