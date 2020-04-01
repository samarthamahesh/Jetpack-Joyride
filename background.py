import random
from colorama import init, Fore, Back, Style
from base import DIMENSION, PATH, COLOR

init(autoreset=True)

class Background:

    def __init__(self):
        self.__ground = Back.RED + ' '
        self.__sky = Back.CYAN + ' '
        self.__cloud = []
        self.__mountain = []
        self.__tree = []
        self.__cloud_dim = DIMENSION['cloud']
        self.__mountain_dim = DIMENSION['mountain']
        self.__tree_dim = DIMENSION['tree']
        self.__cloud_coord = []
        self.__mountain_coord = []
        self.__tree_coord = []

    def create_ground(self, grid):
        for i in range(DIMENSION['length']-DIMENSION['ground_height'], DIMENSION['length']):
            for j in range(DIMENSION['width']):
                grid[i][j] = self.__ground

    def create_sky(self, grid):
        for i in range(DIMENSION['sky_height']):
            for j in range(DIMENSION['width']):
                grid[i][j] = self.__sky

    def create_clouds_coord(self):
        with open(PATH['clouds']) as obj:
            for line in obj:
                self.__cloud.append(line.strip('\n'))

        f = DIMENSION['sky_height'] + random.randint(1, 3)
        x = f
        y = random.randint(10, 30)
        while y < DIMENSION['width'] - DIMENSION['frame_width']:
            temp = [x, y]
            self.__cloud_coord.append(temp)
            x = f + random.randint(0, 4)
            y += random.randint(30, 70)

    def place_clouds(self, grid, xdis):
        for k in self.__cloud_coord:
            if k[1] > xdis + DIMENSION['frame_width']:
                break
            elif k[1] < xdis - DIMENSION['cloud']['y']:
                self.__cloud_coord.remove(k)
            else:
                for i in range(self.__cloud_dim['x']):
                    for j in range(self.__cloud_dim['y']):
                        grid[k[0]+i][k[1]+j] = COLOR['cloud'] + self.__cloud[i][j] + Style.RESET_ALL

    def create_tree_coord(self):
        with open(PATH['tree']) as obj:
            for line in obj:
                self.__tree.append(line.strip('\n'))

        x = DIMENSION['length'] - DIMENSION['ground_height'] - self.__tree_dim['x']
        y = random.randint(50, 100)
        while y < DIMENSION['width'] - DIMENSION['frame_width']:
            temp = [x, y]
            self.__tree_coord.append(temp)
            y += random.randint(100, 200)

    def place_trees(self, grid, xdis):
        for k in self.__tree_coord:
            if k[1] > xdis + DIMENSION['frame_width']:
                break
            elif k[1] < xdis - DIMENSION['tree']['y']:
                self.__tree_coord.remove(k)
            else:
                for i in range(self.__tree_dim['x']):
                    for j in range(self.__tree_dim['y']):
                        grid[k[0]+i][k[1]+j] = COLOR['tree'] + self.__tree[i][j] + Style.RESET_ALL

    def create_mountain_coord(self):
        with open(PATH['mountain']) as obj:
            for line in obj:
                self.__mountain.append(line.strip('\n'))

        x = DIMENSION['sky_height'] + random.randint(3, 6)
        y = random.randint(100, 300)

        while y < DIMENSION['width'] - DIMENSION['frame_width']:
            temp = [x, y]
            self.__mountain_coord.append(temp)
            y += DIMENSION['mountain']['y'] + random.randint(200, 300)

    def place_mountain(self, grid, xdis):
        for k in self.__mountain_coord:
            if k[1] > xdis + DIMENSION['frame_width']:
                break
            elif k[1] < xdis - DIMENSION['mountain']['y']:
                self.__mountain_coord.remove(k)
            else:
                for i in range(self.__mountain_dim['x']):
                    for j in range(self.__mountain_dim['y']):
                        grid[k[0]+i][k[1]+j] = COLOR['mountain'] + self.__mountain[i][j] + Style.RESET_ALL