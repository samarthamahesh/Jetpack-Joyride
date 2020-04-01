from colorama import init, Fore, Back, Style
from board import Board
from background import Background
from characters import Mandalorian, Slave_Enemy, Boss_Enemy
from coin import Coins, place_coins, create_coins
from powerup import PowerUp, place_powerups, create_powerups, place_dragon_powerup, create_dragon_powerup
from obstacles import FireBeam, create_firebeams, create_magnets, place_obstacles
from topbar import Topbar
from getch import user_input
from os import system
import time, random, signal
from base import DIMENSION, COLOR, INIT_PLACE, PATH, IDENTIFIER, TOPBAR, MANDO_MOVES_WITH_FRAME, MANDO_MOVES_FASTER_SPEED
from functions import *
import shutil

columns = shutil.get_terminal_size().columns

init(autoreset=True)

topbar = Topbar()
board = Board()

background = Background()
background.create_ground(board.get_matrix())
background.create_sky(board.get_matrix())
background.create_clouds_coord()
background.create_mountain_coord()
background.create_tree_coord()

coins_obj_list = create_coins()
powerup_obj_list = create_powerups()

firebeam_obj_list = create_firebeams()
magnet_obj_list = create_magnets()

dragon_powerup = create_dragon_powerup()
dragon_collected = False

mando = Mandalorian(INIT_PLACE['Mandalorian'], DIMENSION['Mandalorian'], DIMENSION['dragon_dim'], PATH['Mandalorian'], PATH['dragon'])
mando.reappear(board.get_matrix(), COLOR['Mandalorian_normal'])

slave_enemy_obj_list = []

i = 100
while(i < DIMENSION['width'] - 3 * DIMENSION['frame_width']):
    INIT_PLACE['slave_enemy']['y'] = i
    slave_enemy = Slave_Enemy(INIT_PLACE['slave_enemy'], DIMENSION['slave_enemy'], PATH['slave_enemy'])
    slave_enemy.reappear(board.get_matrix(), COLOR['slave_enemy'])
    i = i + random.randint(50, 100)
    slave_enemy_obj_list.append(slave_enemy)

boss_enemy = Boss_Enemy(INIT_PLACE['boss_enemy'], DIMENSION['boss_enemy'], PATH['boss_enemy-1'], PATH['boss_enemy-2'])
boss_enemy.reappear(board.get_matrix(), COLOR['boss_enemy'])

xdis = 0
system('clear')
x = time.time()
y = x

speedtime = 0
for _ in range(15):
    print()
print("Game guide!!!".center(columns))
print()
print("a -> Move left".center(columns))
print("d -> Move right".center(columns))
print("w -> Activate jet".center(columns))
print("s -> Move down (If dragon is activated)".center(columns))
print("b -> Fire bullets".center(columns))
print("<spacebar> -> Activate shield (if available)".center(columns))
print()
print("Game starts in 5 seconds".center(columns))
print("GET READY!!!".center(columns))

time.sleep(5)

system('clear')

while True:
    ret = check_powerup(mando, powerup_obj_list)
    if ret == True:
        speedtime = 10
    
    if speedtime > 0:
        if MANDO_MOVES_FASTER_SPEED == True:
            mando.set_speed(True)
        passtime = 0.1
        inc = 2
    else:
        if MANDO_MOVES_FASTER_SPEED == True:
            mando.set_speed(False)
        passtime = 0.3
        inc = 1

    if dragon_collected == True:
        passtime = 0.1

    if xdis >= DIMENSION['width'] - DIMENSION['frame_width'] - DIMENSION['boss_enemy']['y']:
        boss_enemy_shoot = True
    else:
        boss_enemy_shoot = False
    
    if(time.time() - x >= passtime):
        x = time.time()
        xdis += inc
        mando.set_xdis(xdis)

        if xdis > DIMENSION['width']-DIMENSION['frame_width']:
            xdis = DIMENSION['width']-DIMENSION['frame_width']
        else:
            if MANDO_MOVES_WITH_FRAME == True:
                mando.increment_ycoord(inc, board.get_matrix())
            else:
                pass

        if boss_enemy_shoot == True:
            boss_enemy.throw_iceballs(mando)

    
    if(time.time() - y >= 1):
        y = time.time()
        topbar.update_time()

        if topbar.get_shield() == IDENTIFIER['shield']['unavailable']:
            topbar.decrement_activation_time()
            if topbar.get_activation_time() == 0:
                topbar.set_shield(IDENTIFIER['shield']['available'])
        elif topbar.get_shield() == IDENTIFIER['shield']['in_use']:
            topbar.decrement_remaining_time()
            if topbar.get_remaining_time() == 0:
                mando.deactivate_shield()
                topbar.set_shield(IDENTIFIER['shield']['unavailable'])
                mando.shield = False

        if speedtime > 0:
            speedtime -= 1

    if topbar.get_game_time() == 0:
        system('clear')
        with open(PATH['time_up']) as obj:
            for line in obj:
                print(line.strip('\n'))
        print()
        print("You scored", topbar.get_score(), "points")
        break

    print("\033[0;0H")
    
    background.place_clouds(board.get_matrix(), xdis)
    background.place_mountain(board.get_matrix(), xdis)
    background.place_trees(board.get_matrix(), xdis)

    place_coins(coins_obj_list, board.get_matrix(), xdis)
    place_powerups(powerup_obj_list, board.get_matrix(), xdis)

    place_obstacles(board.get_matrix(), firebeam_obj_list, xdis, False)
    place_obstacles(board.get_matrix(), magnet_obj_list, xdis, True)

    if dragon_collected == False:
        place_dragon_powerup(dragon_powerup, board.get_matrix())

    obj = check_magnet_range(mando, board.get_matrix(), magnet_obj_list)

    ch = user_input()
    if ch != 'w' and mando.get_magnet() == False:
        mando.gravity(board.get_matrix(), True, obj)
    if mando.get_magnet() == True:
        mando.gravity(board.get_matrix(), False, obj)

    ret = mando.move(board.get_matrix(), ch, topbar)
    if ret == 0:
        system('clear')
        print("Game quitted!!!")
        break

    mando.check_outofrange(board.get_matrix(), xdis)

    mando.move_bullet(board.get_matrix(), xdis)
    boss_enemy.move_iceballs(board.get_matrix(), xdis)
    
    check_coins(mando, coins_obj_list, topbar, xdis)

    for slave in slave_enemy_obj_list:
        slave.move(board.get_matrix())
    
    if xdis > boss_enemy.get_ycoord() - DIMENSION['frame_width']:
        boss_enemy.move(mando, board.get_matrix())
    
    check_enemy_collision(mando, slave_enemy_obj_list, topbar, board.get_matrix(), xdis)
    check_iceball_collision(mando, boss_enemy, board.get_matrix(), topbar)
    check_boss_enemy_collision(mando, boss_enemy, topbar, board.get_matrix())
    check_slave_enemy_bullet_collision(mando.get_bullet_list(), slave_enemy_obj_list, board.get_matrix(), topbar)
    check_iceball_bullet_collision(mando.get_bullet_list(), boss_enemy.get_ice_balls(), board.get_matrix())

    if check_boss_enemy_bullet_collision(mando.get_bullet_list(), boss_enemy, board.get_matrix(), topbar):
        system('clear')
        with open(PATH['congrats']) as obj:
            for line in obj:
                print(line.strip('\n'))
        print()
        print("You killed Viserion(the Dragon) and saved Baby Yoda!!!")
        print("You scored", topbar.get_score(), "points")
        break

    check_obstacle_bullet_collision(mando.get_bullet_list(), firebeam_obj_list, board.get_matrix())
    check_obstacle_bullet_collision(mando.get_bullet_list(), magnet_obj_list, board.get_matrix())
    check_firebeam_collision(mando, board.get_matrix(), firebeam_obj_list, topbar)
    check_magnet_collision(mando, board.get_matrix(), magnet_obj_list)

    ret = check_dragon_powerup(mando, board.get_matrix(), dragon_powerup)
    if ret == True:
        dragon_collected = True

    if topbar.get_lives() == 0:
        system('clear')
        with open(PATH['game_over']) as obj:
            for line in obj:
                print(line.strip('\n'))
        print()
        print("You scored", topbar.get_score(), "points")
        break
    
    topbar.print_topbar()
    board.printBoard(xdis)