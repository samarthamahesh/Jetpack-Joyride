from colorama import Fore, Style
from base import DIMENSION
import time

class Firing:

    def __init__(self, xcoord, ycoord, color, shape, dir, inc):
        self._xcoord = xcoord
        self._ycoord = ycoord
        self._shape = color + shape + Style.RESET_ALL
        self._dir = dir
        self._inc = inc

    def die(self, grid):
        grid[self._xcoord][self._ycoord] = ' '

    def move(self, grid, xdis):
        grid[self._xcoord][self._ycoord] = ' '
        if self._dir == True:
            self._ycoord += self._inc
            if self._ycoord >= xdis + DIMENSION['frame_width'] or self._ycoord >= DIMENSION['width']:
                self._ycoord -= self._inc
                self.die(grid)
                return 1
        else:
            self._ycoord -= self._inc
            if self._ycoord < xdis:
                self._ycoord += self._inc
                self.die(grid)
                return 1
        grid[self._xcoord][self._ycoord] = self._shape

    def get_xcoord(self):
        return self._xcoord

    def get_ycoord(self):
        return self._ycoord

    def get_dir(self):
        return self._dir

    def set_inc(self, inc):
        self._inc = inc
    
    def get_inc(self):
        return self._inc

class Bullet(Firing):
    pass

class Iceball(Firing):
    
    def __init__(self, xcoord, ycoord, color, shape, dis, inc):
        Firing.__init__(self, xcoord, ycoord, color, shape, True, inc)
        self.__mando_dis = dis
        self.__moved = 0
        self.__cycle_time = 1
        self.__cycle_count = 0
        self.__last_count = 0
        self.__iter = 0

    def move(self, grid, xdis):
        if self._xcoord >= DIMENSION['sky_height']:
            grid[self._xcoord][self._ycoord] = ' '

        if self._dir == True:
            self.__cycle_count += 1
            self.__last_count += 1
            if self.__cycle_count == self.__cycle_time:
                self._xcoord -= 1
                self.__cycle_time += 1
                self.__cycle_count = 0
                self.__last_count = 0
        else:
            self.__cycle_count += 1
            if self.__iter == 1:
                if self.__cycle_count >= self.__last_count:
                    self._xcoord += 1
                    self.__cycle_time -= 1
                    self.__cycle_count = 0
                    self.__iter += 1
                    if self.__cycle_time == 0:
                        self.__cycle_time = 1
            else:
                if self.__cycle_count == self.__cycle_time:
                    self._xcoord += 1
                    self.__cycle_time -= 1
                    self.__cycle_count = 0
                    if self.__cycle_time == 0:
                        self.__cycle_time = 1
        self._ycoord -= 1
        self.__moved += 1
        if self.__moved >= self.__mando_dis // 2:
            self._dir = False
            if self.__iter == 0:
                self.__cycle_count = 0
                self.__iter += 1
        
        if self._xcoord >= DIMENSION['length'] - DIMENSION['ground_height']:
            return True
        elif self._ycoord < xdis:
            return True
        elif self._xcoord >= DIMENSION['sky_height']:
            grid[self._xcoord][self._ycoord] = self._shape
        
        return False