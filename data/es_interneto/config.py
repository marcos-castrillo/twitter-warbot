#!/usr/bin/env python
# -*- coding: utf-8 -*-

# General
MENTION_USERS = True
USE_DISTRICTS = False
MIN_ITEMS = 1
MAX_ITEMS = 5
DEFAULT_SLEEP_MESSAGE = u'[Visto en https://www.reddit.com/r/Yointerneto]'
SLEEP_ACTION_NUMBER_LIMIT = 100
REDISTRIBUTE_TRIBUTES = True

# Probabilities
ATRACT_RANGE_LIST =  [1, 1, 1, 1, 1, 2, 2, 2]
THRESHOLD_LIST = [20, 50, 75, 100, 150, 175, 200, 250]
TREASONS_ENABLED_LIST =  [False, False, False, True, True, True, True, True]
PROBAB_DESTROY = [0,  0,  0,  0,  0,  1,  1,  1]
PROBAB_TRAP =    [0,  0,  1,  0,  1,  0,  1,  1]
PROBAB_BATTLE =  [50, 50, 50, 49, 49, 49, 49, 49]

# Map
WIDTH_MAP = 1496
PLAYERS_IN_SINGLE_LINE = False
AVATAR_WIDTH = 48
WIDTH_BETWEEN_PLAYERS = 48
HEIGHT_BETWEEN_PLAYERS = 48

# Ranking
BG_COLOR = '#e2a8fa'
RANKING_IMG_SIZE = AVATAR_WIDTH + 2
RANKING_IMGS_PER_ROW = 10
RANKING_PADDING = 20
RANKING_SPACE_BETWEEN_ROWS = RANKING_IMG_SIZE * 2 + RANKING_PADDING
RANKING_SPACE_BETWEEN_COLS = RANKING_PADDING

# Calculations
RANKING_FIRST_COLUMN_X = RANKING_PADDING
RANKING_FIRST_ROW_Y = RANKING_IMG_SIZE + RANKING_PADDING
RANKING_WIDTH = RANKING_IMGS_PER_ROW * RANKING_IMG_SIZE + (RANKING_IMGS_PER_ROW - 1) * RANKING_SPACE_BETWEEN_COLS + RANKING_PADDING * 2