from colorama import Fore, Style
import random
from base import DIMENSION, PATH, COLOR

HORIZONTAL = 0
VERTICAL = 1
RIGHTTILT = 2
LEFTTILT = 3

class Obstacle:

    def __init__(self, xcoord, ycoord, dim, shape, path):
        self._xcoord = xcoord
        self._ycoord = ycoord
        self._height = dim['x']
        self._width = dim['y']
        self._each_shape = shape
        self._lives = 3
        self._shape = []
        with open(path) as obj:
            for line in obj:
                self._shape.append(line.strip('\n'))

    def get_xcoord(self):
        return self._xcoord

    def get_ycoord(self):
        return self._ycoord

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def get_each_shape(self):
        return self._each_shape

    def decrement_lives(self):
        self._lives -= 1

    def get_lives(self):
        return self._lives

    def get_shape(self):
        return self._shape

class FireBeam(Obstacle):

    def place(self, grid):
        for i in range(self._height):
            for j in range(self._width):
                if self._shape[i][j] == self._each_shape:
                    grid[self._xcoord+i][self._ycoord+j] = COLOR['fire_beam'] + self._shape[i][j] + Style.RESET_ALL

    def remove(self, grid):
        for i in range(self._height):
            for j in range(self._width):
                if self._shape[i][j] == self._each_shape:
                    grid[self._xcoord+i][self._ycoord+j] = ' '

def create_firebeams():
    obj = []

    x = DIMENSION['sky_height'] + random.randint(5, 10)
    y = random.randint(50, 150)

    while y < DIMENSION['width'] - DIMENSION['frame_width']:
        ch = random.randint(1, 4)
        fire_beam = FireBeam(x, y, DIMENSION['fire_beam-' + str(ch)], '*', PATH['fire_beam-' + str(ch)])
        obj.append(fire_beam)
        y += random.randint(30, 50)

    return obj

class Magnet(Obstacle):

    def __init__(self, xcoord, ycoord, dim, shape, path):
        Obstacle.__init__(self, xcoord, ycoord, dim, shape, path)
        self.__x_range = 20
    
    def place(self, grid):
        for i in range(self._height):
            for j in range(self._width):
                if j >= self._width // 2:
                    grid[self._xcoord+i][self._ycoord+j] = COLOR['magnet-2'] + self._shape[i][j] + Style.RESET_ALL
                else:
                    grid[self._xcoord+i][self._ycoord+j] = COLOR['magnet-1'] + self._shape[i][j] + Style.RESET_ALL
    def remove(self, grid):
        for i in range(self._height):
            for j in range(self._width):
                    grid[self._xcoord+i][self._ycoord+j] = ' '

    def get_x_range(self):
        return self.__x_range

def create_magnets():
    obj = []
    
    x = DIMENSION['sky_height'] + 1
    y = random.randint(150, 200)

    while y < DIMENSION['width'] - DIMENSION['frame_width']:
        magnet = Magnet(x, y, DIMENSION['magnet'], '@', PATH['magnet'])
        obj.append(magnet)
        y += random.randint(150, 200)

    return obj

def place_obstacles(grid, obj_list, xdis, is_magnet):
    for obj in obj_list:
        if obj.get_ycoord() > xdis + DIMENSION['frame_width']:
            break
        elif obj.get_ycoord() < xdis - obj.get_width():
            if is_magnet == False:
                obj_list.remove(obj)
            else:
                if obj.get_ycoord() < xdis - obj.get_width() - obj.get_x_range():
                    obj_list.remove(obj)
        else:
            obj.place(grid)