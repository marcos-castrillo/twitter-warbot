#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models.match_type import Match_type

# General
config.general.mention_users = True
config.general.match_type = Match_type.standard
MIN_ITEMS = 1
MAX_ITEMS = 5
DEFAULT_SLEEP_MESSAGE = u'[Visto en https://www.reddit.com/r/Yointerneto]'
SLEEP_ACTION_NUMBER_LIMIT = 100
REDISTRIBUTE_TRIBUTES = True

# Probabilities
ATRACT_RANGE_LIST = [1, 1, 1, 1, 1, 2, 2, 2]
THRESHOLD_LIST = [20, 50, 75, 100, 150, 175, 200, 250]
TREASONS_ENABLED_LIST = [False, False, False, True, True, True, True, True]
PROBAB_DESTROY = [0, 0, 0, 0, 0, 1, 1, 1]
PROBAB_TRAP = [0, 0, 1, 0, 1, 0, 1, 1]

# Map
config.map.players_in_single_line = False
config.map.avatar_size = 48
config.map.width_between_players = 48
config.map.height_between_players = 48
config.map.watermark_coordinates = [125, 1275]

# Ranking
config.ranking.avatar_size = 48
config.ranking.bg_color = '#e2a8fa'
config.ranking.images_per_row = 10
config.ranking.padding = 20
config.ranking.district_name_height = 25
