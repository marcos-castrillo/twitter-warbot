#!/usr/bin/env python
# -*- coding: utf-8 -*-

# General
MENTION_USERS = True
USE_DISTRICTS = True
USE_FLAGS = False
MIN_ITEMS = 0
MAX_ITEMS = 2
MAX_ATRACTED_PLAYERS = 5
DEFAULT_SLEEP_MESSAGE = u''
SLEEP_ACTION_NUMBER_LIMIT = 60
REDISTRIBUTE_TRIBUTES = False

# If USE_DISTRICTS
MAX_TRIBUTES_PER_DISTRICT = 0

# Probabilities
ATRACT_RANGE_LIST =  [1, 1, 1, 1, 2, 2, 2, 3]
PROBAB_MOVE =    [25,  8,  9,  10,  12, 14, 15, 16]
PROBAB_ITEM =    [24, 38, 32, 29, 23, 18, 15, 15]
THRESHOLD_LIST = [50, 100, 150, 200, 250, 300, 400, 500]
TREASONS_ENABLED_LIST =  [False, False, False, True, True, True, True, True]

# Map
WIDTH_MAP = 1496
PLAYERS_IN_SINGLE_LINE = False
AVATAR_WIDTH = 48
WIDTH_BETWEEN_PLAYERS = 24
HEIGHT_BETWEEN_PLAYERS = 36

# Ranking
BG_COLOR = '#eceae4'
RANKING_IMG_SIZE = AVATAR_WIDTH + 2
RANKING_IMGS_PER_ROW = 16
RANKING_PADDING = 20
RANKING_SPACE_BETWEEN_COLS = RANKING_PADDING
RANKING_SPACE_BETWEEN_DISTRICTS = RANKING_PADDING / 2
RANKING_DISTRICT_NAME_HEIGHT = 25
RANKING_SPACE_BETWEEN_ROWS = RANKING_IMG_SIZE * 2 + RANKING_PADDING + int(RANKING_SPACE_BETWEEN_DISTRICTS/2) + RANKING_DISTRICT_NAME_HEIGHT

# Calculations
RANKING_FIRST_COLUMN_X = RANKING_PADDING
RANKING_FIRST_ROW_Y = RANKING_IMG_SIZE + RANKING_PADDING + RANKING_DISTRICT_NAME_HEIGHT
RANKING_WIDTH = RANKING_IMGS_PER_ROW * RANKING_IMG_SIZE + (RANKING_IMGS_PER_ROW - 1) * RANKING_SPACE_BETWEEN_COLS + RANKING_PADDING * 2
RANKING_DELTA_X = RANKING_IMG_SIZE + RANKING_SPACE_BETWEEN_COLS
