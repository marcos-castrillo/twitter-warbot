#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models.match_type import Match_type

# General
MENTION_USERS = True
MATCH_TYPE = Match_type.rumble
USE_FLAGS = False
MIN_ITEMS = 0
MAX_ITEMS = 50
MAX_ATRACTED_PLAYERS = 0
DEFAULT_SLEEP_MESSAGE = u''
SLEEP_ACTION_NUMBER_LIMIT = 60
REDISTRIBUTE_TRIBUTES = True

# Probabilities
ATRACT_RANGE_LIST = [0]
PROBAB_SUICIDE = [0]
PROBAB_TRAP = [0]
PROBAB_INFECT = [0]
PROBAB_DESTROY = [0]
PROBAB_ATRACT = [0]
PROBAB_MONSTER = [0]
PROBAB_MONSTER = [0]
PROBAB_MOVE = [0]
PROBAB_REVIVE = [1]
PROBAB_STEAL = [5]
PROBAB_ITEM = [5]
PROBAB_TIE = 3
PROBAB_NEUTRAL = 25

THRESHOLD_LIST = []
TREASONS_ENABLED_LIST =  [True]

# Map
MAP_AVATAR_SIZE = 150
MAP_PLAYERS_IN_SINGLE_LINE = False
MAP_MAX_PLAYERS_IN_LINE = 5
MAP_WIDTH_BETWEEN_PLAYERS = 155
MAP_HEIGHT_BETWEEN_PLAYERS = 155
MAP_WATERMARK_COORDINATES = None
MAP_LIMIT_SMALL_AVATARS = 0
MAP_CIRCLE_SIZE = 1000
MAP_SHOW_CIRCLE = False

# Ranking
RANKING_AVATAR_SIZE = 70
BG_COLOR = '#dcdeff'
RANKING_IMGS_PER_ROW = 8
RANKING_PADDING = 20
RANKING_DISTRICT_NAME_HEIGHT = 0
