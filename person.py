from colorama import Fore, Style

class Person:

    def __init__(self, coord, dim, path):
        self._xcoord = coord['x']
        self._ycoord = coord['y']
        self._height = dim['x']
        self._width = dim['y']
        self._shape = []
        self._dir = True
        with open(path) as obj:
            for line in obj:
                self._shape.append(line.strip('\n'))
    
    def disappear(self, grid):
        for i in range(self._height):
            for j in range(self._width):
                grid[self._xcoord + i][self._ycoord + j] = ' '

    def reappear(self, grid, color):
        for i in range(self._height):
            for j in range(self._width):
                grid[self._xcoord + i][self._ycoord + j] = color + self._shape[i][j] + Style.RESET_ALL

    def get_xcoord(self):
        return self._xcoord

    def get_ycoord(self):
        return self._ycoord

    def get_height(self):
        return self._height

    def get_width(self):
        return self._width

    def get_dir(self):
        return self._dir