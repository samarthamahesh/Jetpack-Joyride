from person import Person
from getch import user_input
from colorama import Fore, Style
from base import DIMENSION, COLOR, IDENTIFIER
from firing import Bullet, Iceball

class Mandalorian(Person):

    def __init__(self, coord, dim, dragon_dim, path, dragon_path):
        Person.__init__(self, coord, dim, path)
        self.__shield = False
        self.__bullet_list = []
        self.__cycle_time = 3
        self.__cur_cycle = 0
        self.__cycle_iter_times = 2
        self.__double = False
        self.__magnet = False
        self.__speed = False
        self.__dragon = False
        self.__dragon_shape = []
        self.__extra_shape = []
        self.__dragon_dim = dragon_dim
        self.__extra_dim = dim
        self.__xdis = 0
        with open(dragon_path) as obj:
            for line in obj:
                self.__dragon_shape.append(line.strip('\n'))
        with open(path) as obj:
            for line in obj:
                self.__extra_shape.append(line.strip('\n'))
        self.__dragon_array = [DIMENSION['sky_height'] for i in range(self.__dragon_dim['y'])]

    def reappear(self, grid, color):
        if self.__dragon == False:
            for i in range(self._height):
                for j in range(self._width):
                    grid[self._xcoord + i][self._ycoord + j] = color + self._shape[i][j] + Style.RESET_ALL
        else:
            for i in range(self._width):
                for j in range(self._height):
                    grid[self.__dragon_array[i]+j][self.__xdis+i] = self._shape[j][i]

    def disappear(self, grid):
        if self.__dragon == False:
            for i in range(self._height):
                for j in range(self._width):
                    grid[self._xcoord + i][self._ycoord + j] = ' '
        else:
            for i in range(self._width):
                for j in range(self._height):
                    grid[self.__dragon_array[i]+j][self.__xdis+i] = ' '

    def move(self, grid, ch, bar):
        if ch == 'q':
            return 0

        if self.__dragon == False:
            self.disappear(grid)

            if ch == 'd':
                if self.__magnet == True:
                    self._ycoord += 2
                else:
                    if self.__speed == True:
                        self._ycoord += 2
                    else:
                        self._ycoord += 1
                self._dir = True
            elif ch == 'a':
                if self.__magnet == True:
                    self._ycoord -= 2
                else:
                    if self.__speed == True:
                        self._ycoord -= 2
                    else:
                        self._ycoord -= 1
                self._dir = False
            elif ch == 'w':
                self.__cycle_time = 3
                self.__cur_cycle = 0
                self.__cycle_iter_times = 2
                self.__double = False
                self._xcoord -= 1
                self.__velocity = 0
            elif ch == ' ':
                if bar.get_shield() == 1:
                    self.__shield = True
                    bar.set_shield(IDENTIFIER['shield']['in_use'])
            elif ch == 'b':
                self.shoot_bullet(grid)

            if self.__shield == False:
                self.reappear(grid, COLOR['Mandalorian_normal'])
            else:
                self.reappear(grid, COLOR['Mandalorian_shield'])

        else:
            self.disappear(grid)
            width = self.__dragon_dim['y']
            self.shoot_bullet(grid)
            for i in range(width):
                if i >= width - 7:
                    if ch == 'w':
                        if self.__dragon_array[i] > DIMENSION['sky_height']:
                            self.__dragon_array[i] -= 1
                    elif ch == 's':
                        if self.__dragon_array[i] < DIMENSION['length'] - DIMENSION['ground_height'] - self._height:
                            self.__dragon_array[i] += 1
                else:
                    if self.__dragon_array[i] < self.__dragon_array[i+1]:
                        self.__dragon_array[i] += 1
                    elif self.__dragon_array[i] > self.__dragon_array[i+1]:
                        self.__dragon_array[i] -= 1
                    if self.__dragon_array[i] < self.__dragon_array[i+1]:
                        self.__dragon_array[i] += 1
                    elif self.__dragon_array[i] > self.__dragon_array[i+1]:
                        self.__dragon_array[i] -= 1
            self.reappear(grid, COLOR['Mandalorian_normal'])

    def check_outofrange(self, grid, xdis):
        self.disappear(grid)

        if self._ycoord < xdis:
            self._ycoord = xdis
        elif self._ycoord > xdis + DIMENSION['frame_width'] - self._width:
            self._ycoord = xdis + DIMENSION['frame_width'] - self._width

        if self._xcoord <= DIMENSION['sky_height']:
            self._xcoord = DIMENSION['sky_height'] + 1
        elif self._xcoord > DIMENSION['length'] - DIMENSION['ground_height'] - self._height:
            self._xcoord = DIMENSION['length'] - DIMENSION['ground_height'] -self._height

        if self.__shield == False:
            self.reappear(grid, COLOR['Mandalorian_normal'])
        else:
            self.reappear(grid, COLOR['Mandalorian_shield'])

    def gravity(self, grid, ch, obj):
        if self.__dragon == False:
            self.disappear(grid)
    
            if ch == True and self._xcoord <= DIMENSION['length']-DIMENSION['ground_height']-1-self._height:
                self.__cur_cycle += 1
                if self.__cur_cycle == self.__cycle_time:
                    self.__cur_cycle = 0
                    self.__cycle_iter_times -= 1
                    if self.__cycle_iter_times == 0:
                        self.__cycle_time -= 1
                        self.__cycle_iter_times = 2
                    if self.__cycle_time == 0:
                        self.__cycle_time = 1
                        self.__double = True
                    if self.__double == True:
                        self._xcoord += 2
                        if self._xcoord > DIMENSION['length'] - DIMENSION['ground_height'] - self._height:
                            self._xcoord -= 1
                    else:
                        self._xcoord += 1
            elif ch == False and self._xcoord > DIMENSION['sky_height']:
                if self._ycoord > obj.get_ycoord()+obj.get_width()//2:
                    self._ycoord -= 1
                elif self._ycoord < obj.get_ycoord()+obj.get_width()//2-self._width:
                    self._ycoord += 1
                self._xcoord -= 1
                if self._xcoord <= obj.get_xcoord() + obj.get_height() and self._ycoord > obj.get_ycoord()-self._width and self._ycoord < obj.get_ycoord()+obj.get_width():
                    self._xcoord = obj.get_xcoord() + obj.get_height()
            
            if self.__shield == False:
                self.reappear(grid, COLOR['Mandalorian_normal'])
            else:
                self.reappear(grid, COLOR['Mandalorian_shield'])

    def spawn(self, grid):
        self.disappear(grid)
        self._xcoord = DIMENSION['sky_height']
        self._ycoord -= 100
        if self.__shield == False:
            self.reappear(grid, COLOR['Mandalorian_normal'])
        else:
            self.reappear(grid, COLOR['Mandalorian_shield'])

    def shoot_bullet(self, grid):
        if self.__dragon == False:
            if self.__speed == True:
                bullet = Bullet(self._xcoord + 1, self._ycoord, COLOR['bullet'], '-', self._dir, 3)
            else:
                bullet = Bullet(self._xcoord + 1, self._ycoord, COLOR['bullet'], '-', self._dir, 2)
        else:
            bullet = Bullet(self.__dragon_array[self._width-1] + self._height//2, self.__xdis+self._width, COLOR['fire'], '*', True, 3)
        self.__bullet_list.append(bullet)

    def move_bullet(self, grid, xdis):
        for bullet in self.__bullet_list:
            ret = bullet.move(grid, xdis)
            if ret == 1:
                self.__bullet_list.remove(bullet)

    def activate_shield(self):
        self.__shield = True

    def deactivate_shield(self):
        self.__shield = False

    def get_magnet(self):
        return self.__magnet
    
    def set_magnet(self, val):
        self.__magnet = val

    def get_shield(self):
        return self.__shield

    def get_bullet_list(self):
        return self.__bullet_list

    def set_speed(self, val):
        self.__speed = val

    def set_xdis(self, val):
        self.__xdis = val

    def get_xdis(self):
        return self.__xdis

    def increment_ycoord(self, inc, grid):
        self.disappear(grid)
        self._ycoord += inc
        if self.__shield == False:
            self.reappear(grid, COLOR['Mandalorian_normal'])
        else:
            self.reappear(grid, COLOR['Mandalorian_shield'])

    def set_dragon(self, val, grid):
        self.disappear(grid)
        self.__dragon = val
        if val == True:
            self._shape = self.__dragon_shape
            self._height = self.__dragon_dim['x']
            self._width = self.__dragon_dim['y']
            self._ycoord -= DIMENSION['frame_width']
            self._xcoord = DIMENSION['sky_height']
            self.__shield = False
        else:
            self._shape = self.__extra_shape
            self._height = self.__extra_dim['x']
            self._width = self.__extra_dim['y']
            self._ycoord -= DIMENSION['frame_width']
            self._xcoord = DIMENSION['sky_height']
        self.reappear(grid, COLOR['Mandalorian_normal'])
    
    def get_dragon(self):
        return self.__dragon

    def get_array(self):
        return self.__dragon_array

class Slave_Enemy(Person):
    
    def __init__(self, coord, dim, path):
        Person.__init__(self, coord, dim, path)
        self.__maxsteps = 50
        self.__steps = 0

    def move(self, grid):
        self.disappear(grid)
        if self._dir == True:
            self._ycoord += 1
        else:
            self._ycoord -= 1
        self.__steps += 1
        if self.__steps >= self.__maxsteps:
            self._dir = not self._dir
            self.__steps = 0
        self.reappear(grid, COLOR['slave_enemy'])
    
    def die(self, obj_list, grid):
        self.disappear(grid)
        obj_list.remove(self)
        
class Boss_Enemy(Person):

    def __init__(self, coord, dim, path1, path2):
        Person.__init__(self, coord, dim, path1)
        self.__shape2 = []
        self.__curshape = True
        self.__iceballs_list = []
        with open(path2) as obj:
            for line in obj:
                self.__shape2.append(line.strip('\n'))

    def reappear(self, grid, color):
        for i in range(self._height):
            for j in range(self._width):
                if self.__curshape == True:
                    grid[self._xcoord + i][self._ycoord + j] = color + self._shape[i][j] + Style.RESET_ALL
                else:
                    grid[self._xcoord + i][self._ycoord + j] = color + self.__shape2[i][j] + Style.RESET_ALL
        self.__curshape = not self.__curshape

    def move(self, mando, grid):
        self.disappear(grid)
        if mando.get_dragon() == False:
            if mando.get_xcoord() > self._xcoord and self._xcoord < DIMENSION['length'] - DIMENSION['ground_height'] - self._height:
                self._xcoord += 1
            elif mando.get_xcoord() < self._xcoord and self._xcoord > DIMENSION['sky_height']:
                self._xcoord -= 1
        else:
            if self._xcoord > mando.get_array()[mando.get_width()//2] and self._xcoord > DIMENSION['sky_height']:
                self._xcoord -=1
            elif self._xcoord < mando.get_array()[mando.get_width()//2] and self._xcoord < DIMENSION['length'] - DIMENSION['ground_height'] - self._height:
                self._xcoord += 1
        self.reappear(grid, COLOR['boss_enemy'])

    def throw_iceballs(self, mando):
        dis = self._ycoord - mando.get_ycoord()
        iceball = Iceball(self._xcoord+DIMENSION['boss_enemy']['mouth']+1, self._ycoord-1, COLOR['iceball'], '*', dis, 2)
        self.__iceballs_list.append(iceball)

    def move_iceballs(self, grid, xdis):
        for i in self.__iceballs_list:
            ret = i.move(grid, xdis)
            if ret == True:
                self.__iceballs_list.remove(i)

    def get_ice_balls(self):
        return self.__iceballs_list