#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models.match_type import Match_type

# General
MENTION_USERS = True
MATCH_TYPE = Match_type.standard
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

# Map
MAP_PLAYERS_IN_SINGLE_LINE = False
MAP_AVATAR_SIZE = 48
MAP_WIDTH_BETWEEN_PLAYERS = 48
MAP_HEIGHT_BETWEEN_PLAYERS = 48
MAP_WATERMARK_COORDINATES = [125, 1275]

# Ranking
RANKING_AVATAR_SIZE = 48
BG_COLOR = '#e2a8fa'
RANKING_IMGS_PER_ROW = 10
RANKING_PADDING = 20
RANKING_DISTRICT_NAME_HEIGHT = 25
