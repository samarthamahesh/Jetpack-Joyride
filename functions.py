from colorama import Style
from base import DIMENSION, COLOR

def check_enemy_collision(mando, enemy_obj, bar, grid, xdis):
    if mando.get_shield() == False:
        for enemy in enemy_obj:
            if enemy.get_ycoord() > xdis + DIMENSION['frame_width']:
                break
            if enemy.get_ycoord() > mando.get_ycoord() + mando.get_width() or enemy.get_ycoord() < mando.get_ycoord() - enemy.get_width():
                continue
            else:
                if mando.get_dragon() == False:
                    if enemy.get_xcoord() == mando.get_xcoord() + mando.get_height() - 1 and abs(mando.get_ycoord() - enemy.get_ycoord()) < mando.get_width():
                        enemy.die(enemy_obj, grid)
                        bar.increment_score(50)
                        bar.increment_kills()
                    elif (abs(enemy.get_ycoord() - mando.get_ycoord()) < mando.get_width()) and mando.get_xcoord() + mando.get_height() > enemy.get_xcoord():
                        mando.spawn(grid)
                        bar.decrement_lives()
                else:
                    array = mando.get_array()
                    for i in range(mando.get_width()):
                        for j in range(mando.get_height()):
                            temp1 = [array[i]+j, xdis+i]
                            for x in range(enemy.get_height()):
                                for y in range(enemy.get_width()):
                                    temp2 = [enemy.get_xcoord()+x, enemy.get_ycoord()+y]
                                    if temp1 == temp2:
                                        mando.set_dragon(False, grid)
    
def check_boss_enemy_collision(mando, obj, bar, grid):
    if mando.get_shield() == False:
        if mando.get_dragon() == False:
            if obj.get_xcoord() - mando.get_xcoord() <= mando.get_height() or mando.get_xcoord() - obj.get_xcoord() <= obj.get_height():
                if mando.get_ycoord() + mando.get_width() >= obj.get_ycoord():
                    bar.decrement_lives()
                    mando.spawn(grid)
        else:
            array = mando.get_array()
            for i in range(mando.get_width()):
                for j in range(mando.get_height()):
                    temp1 = [array[i]+j, mando.get_xdis()+i]
                    for x in range(obj.get_height()):
                        for y in range(obj.get_width()):
                            temp2 = [obj.get_xcoord()+x, obj.get_ycoord()+y]
                            if temp1 == temp2:
                                mando.set_dragon(False, grid)

def check_slave_enemy_bullet_collision(bullet_list, slave_enemy_list, grid, bar):
    for bullet in bullet_list:
        for enemy in slave_enemy_list:
            sub = enemy.get_ycoord() - bullet.get_ycoord()
            if bullet.get_xcoord() >= enemy.get_xcoord() and sub < 1 and -sub < enemy.get_width():
                enemy.die(slave_enemy_list, grid)
                bullet.die(grid)
                bullet_list.remove(bullet)
                bar.increment_score(50)
                bar.increment_kills()
                break

def check_boss_enemy_bullet_collision(bullet_list, boss_enemy, grid, bar):
    for bullet in bullet_list:
        if bullet.get_xcoord() >= boss_enemy.get_xcoord() and bullet.get_xcoord() < boss_enemy.get_xcoord()+boss_enemy.get_height() and boss_enemy.get_ycoord() - bullet.get_ycoord() < 1:
            bullet.die(grid)
            bullet_list.remove(bullet)
            bar.increment_score(100)
            bar.decrement_dragon_lives()
            if bar.get_dragon_lives() == 0:
                return True
            else:
                return False

def check_obstacle_bullet_collision(bullet_list, obj_list, grid):
    for bullet in bullet_list:
        for obj in obj_list:
            collide = False
            for k in range(bullet.get_inc()):
                for i in range(obj.get_height()):
                    for j in range(obj.get_width()):
                        if ((bullet.get_dir() == True and bullet.get_xcoord() == obj.get_xcoord()+i and obj.get_ycoord()+j == bullet.get_ycoord()-k) \
                            or (bullet.get_dir() == False and bullet.get_xcoord() == obj.get_xcoord()+i and obj.get_ycoord()+j == bullet.get_ycoord()+k)) and\
                                obj.get_shape()[i][j] == obj.get_each_shape():
                                            collide = True
                                            break
                    if collide == True:
                        break
                if collide == True:
                    break
            if collide == True:
                bullet.die(grid)
                bullet_list.remove(bullet)
                obj.decrement_lives()
                if obj.get_lives() == 0:
                    obj.remove(grid)
                    obj_list.remove(obj)
 
def check_iceball_collision(mando, boss_enemy, grid, bar):
    if mando.get_shield() == False:
        for iceball in boss_enemy.get_ice_balls():
            if mando.get_dragon() == False:
                for i in range(mando.get_height()):
                    if iceball.get_xcoord() == mando.get_xcoord()+i and iceball.get_ycoord() < mando.get_ycoord() + mando.get_width() and iceball.get_ycoord() >= mando.get_ycoord():
                        bar.decrement_lives()
                        iceball.die(grid)
                        boss_enemy.get_ice_balls().remove(iceball)
                        mando.spawn(grid)
                        break
            else:
                array = mando.get_array()
                for i in range(mando.get_width()):
                    for j in range(mando.get_height()):
                        temp1 = [array[i]+j, mando.get_xdis()+i]
                        temp2 = [iceball.get_xcoord(), iceball.get_ycoord()]
                        if temp1 == temp2:
                            mando.set_dragon(False, grid)

def check_iceball_bullet_collision(bullet_list, iceball_list, grid):
    for bullet in bullet_list:
        for iceball in iceball_list:
            if bullet.get_xcoord() == iceball.get_xcoord() and abs(bullet.get_ycoord() - iceball.get_ycoord()) <= 1:
                bullet_list.remove(bullet)
                iceball_list.remove(iceball)
                bullet.die(grid)
                iceball.die(grid)

def check_firebeam_collision(mando, grid, obj_list, bar):
    if mando.get_shield() == False:
        if mando.get_dragon() == False:
            for i in range(mando.get_height()):
                for j in range(mando.get_width()):
                    temp1 = [mando.get_xcoord()+i, mando.get_ycoord()+j]
                    for obj in obj_list:
                        for x in range(obj.get_height()):
                            for y in range(obj.get_width()):
                                temp2 = [obj.get_xcoord() + x, obj.get_ycoord() + y]
                                if temp1 == temp2:
                                    bar.decrement_lives()
                                    mando.spawn(grid)
                                    return
        else:
            array = mando.get_array()
            for i in range(mando.get_width()):
                for j in range(mando.get_height()):
                    temp1 = [array[i]+j, mando.get_xdis()+i]
                    for obj in obj_list:
                        for x in range(obj.get_height()):
                            for y in range(obj.get_width()):
                                temp2 = [obj.get_xcoord() + x, obj.get_ycoord() + y]
                                if temp1 == temp2:
                                    mando.set_dragon(False, grid)
                                    return            

def check_coins(mando, coins_obj_list, bar, xdis):
    for coins in coins_obj_list:
        if coins.get_ycoord() > xdis + DIMENSION['frame_width']:
            break
        else:
            for x in range(coins.get_dim()['x']):
                for y in range(coins.get_dim()['y']):
                    temp1 = [coins.get_xcoord()+x, coins.get_ycoord()+y]
                    if mando.get_dragon() == False:
                        for i in range(mando.get_height()):
                            for j in range(mando.get_width()):
                                temp2 = [mando.get_xcoord()+i, mando.get_ycoord()+j]
                                if temp1 == temp2 and coins.get_shape()[x][y] == coins.get_coin_shape():
                                    bar.increment_score(5)
                                    bar.increment_coins()
                                    coins.remove_coin([x, y])

                    else:
                        array = mando.get_array()
                        for i in range(mando.get_width()):
                            for j in range(mando.get_height()):
                                temp2 = [array[i]+j, xdis+i]
                                if temp1 == temp2 and coins.get_shape()[x][y] == coins.get_coin_shape():
                                    bar.increment_score(5)
                                    bar.increment_coins()
                                    coins.remove_coin([x, y])


def check_powerup(mando, obj_list):
    for i in range(mando.get_height()):
        for j in range(mando.get_width()):
            temp1 = [mando.get_xcoord()+i, mando.get_ycoord()+j]
            for obj in obj_list:
                for i in range(obj.get_dim()['x']):
                    for j in range(obj.get_dim()['y']):
                        temp2 = [obj.get_xcoord()+i, obj.get_ycoord()+j]
                        if temp1 == temp2:
                            return True
    return False

def check_magnet_range(mando, grid, obj_list):
    for obj in obj_list:
        x = mando.get_ycoord() - obj.get_ycoord()
        if (x < obj.get_width() + obj.get_x_range() and x >= 0) or (-x < mando.get_width()+obj.get_x_range() and -x >=0):
            mando.set_magnet(True)
            return obj
    mando.set_magnet(False)
    return None

def check_dragon_powerup(mando, grid, dragon_powerup):
    for i in range(mando.get_height()):
        for j in range(mando.get_width()):
            temp1 = [mando.get_xcoord()+i, mando.get_ycoord()+j]
            for x in range(dragon_powerup.get_dim()['x']):
                for y in range(dragon_powerup.get_dim()['y']):
                    temp2 = [dragon_powerup.get_xcoord()+x, dragon_powerup.get_ycoord()+y]
                    if temp1 == temp2:
                        mando.set_dragon(True, grid)
                        dragon_powerup.remove(grid)
                        return True
    return False

def check_magnet_collision(mando, grid, obj_list):
    if mando.get_dragon() == True:
        array = mando.get_array()
        for i in range(mando.get_width()):
            for j in range(mando.get_height()):
                temp1 = [array[i]+j, mando.get_xdis()+i]
                for obj in obj_list:
                    for x in range(obj.get_height()):
                        for y in range(obj.get_width()):
                            temp2 = [obj.get_xcoord() + x, obj.get_ycoord() + y]
                            if temp1 == temp2:
                                mando.set_dragon(False, grid)
                                return 