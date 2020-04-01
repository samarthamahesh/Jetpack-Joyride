from base import DIMENSION, IDENTIFIER, TOPBAR

class Topbar:
    
    def __init__(self):
        self.__time = TOPBAR['game_time']
        self.__score = 0
        self.__lives = TOPBAR['mando_lives']
        self.__dragon_lives = TOPBAR['viserion_lives']
        self.__coins = 0
        self.__shield = 0
        self.__activation_time = TOPBAR['shield_activation_time']
        self.__remaining_time = TOPBAR['shield_remaining_time']
        self.__kills = 0
    
    def update_time(self):
        self.__time -= 1

    def increment_score(self, inc):
        self.__score += inc

    def increment_coins(self):
        self.__coins += 1

    def decrement_lives(self):
        self.__lives -= 1

    def decrement_dragon_lives(self):
        self.__dragon_lives -= 1

    def get_game_time(self):
        return self.__time

    def get_score(self):
        return self.__score

    def get_lives(self):
        return self.__lives

    def get_dragon_lives(self):
        return self.__dragon_lives

    def get_shield(self):
        return self.__shield

    def set_shield(self, val):
        self.__shield = val
        if val == IDENTIFIER['shield']['unavailable']:
            self.__remaining_time = 10
        elif val == IDENTIFIER['shield']['available']:
            self.__activation_time = 60

    def get_activation_time(self):
        return self.__activation_time

    def get_remaining_time(self):
        return self.__remaining_time

    def decrement_activation_time(self):
        self.__activation_time -= 1

    def decrement_remaining_time(self):
        self.__remaining_time -= 1

    def increment_kills(self):
        self.__kills += 1

    def print_topbar(self):
        x = ''
        for _ in range(DIMENSION['frame_width']):
            x += ' '
        print(x)
        x = ''
        print("\033[0;0H")
        x += "Time remaining :" + str(self.__time) + "s\tCoins :" + str(self.__coins) + "\tKills :" + str(self.__kills) + "\tScore :" + str(self.__score) + "\tLives :" + str(self.__lives) + "\tViseron lives :" + str(self.__dragon_lives)
        if self.__shield == 0:
            x += "\tShield activation time :" + str(self.__activation_time)
        elif self.__shield == 1:
            x += "\tShield is ready"
        elif self.__shield == 2:
            x += "\tShield remaining time :" + str(self.__remaining_time)
        print(x)