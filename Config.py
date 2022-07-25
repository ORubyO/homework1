import pygame as pg

"""
Constant
"""
SCREEN_WIDTH = 650
SCREEN_HEIGHT = 700
BACKGROUND_COLOR = (0, 0, 0)  # rgb for black

TEXT_COLOR = (255, 255, 255)
SCORE_POS = (10, 0)
HP_POS = (SCREEN_WIDTH - 50, 0)

SCORE = 100

PLAYER_SPEED = 5
PLAYER_HP = 3

P_BULLET_COLOR = (255, 255, 255)
E_BULLET_COLOR = (255, 0, 0)
BULLET_SPEED = 9
BULLET_SIZE = (3, 12)

ENEMY_X_COUNT = 6
ENEMY_Y_COUNT = 3
ENEMY_SPEED = 5
ENEMY_MOVEMENT_SET = [(1,0)] * 35 + [(0, 3)] + [(-1, 0)] * 35 + [(0, 3)]
ENEMY_MOVE_TIME_MAX = 750
ENEMY_MOVE_TIME_MIN = 50

ENEMY_SHOOT_TIME = 1000
ENEMY_SHOOT_PROBABILITY = 0.2

ENEMYSHOOT_EVENT = pg.USEREVENT + 1  # custom event
ENEMYMOVE_EVENT = ENEMYSHOOT_EVENT + 1