#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models.match_type import Match_type

# General
config.general.mention_users = True
config.general.match_type = Match_type.standard
config.general.use_flags = True
MIN_ITEMS = 0
MAX_ITEMS = 1
MAX_ATRACTED_PLAYERS = 5
DEFAULT_SLEEP_MESSAGE = u''
SLEEP_ACTION_NUMBER_LIMIT = 60
REDISTRIBUTE_TRIBUTES = True

# Probabilities
ATRACT_RANGE_LIST = [1, 1, 2, 2, 2, 3, 3, 3]
PROBAB_DESTROY = [0, 1, 1, 1, 1, 2, 2, 3]
PROBAB_ITEM = [42, 37, 32, 29, 23, 17, 14, 14]

THRESHOLD_LIST = [25, 50, 75, 100, 125, 150, 175, 200]
TREASONS_ENABLED_LIST = [False, False, False, True, True, True, True, True]

# Map
config.map.avatar_size = 70
config.map.players_in_single_line = False
config.map.max_players_in_line = 3
config.map.width_between_players = 44
config.map.height_between_players = 48
config.map.watermark_coordinates = [1549, 1462]
config.map.limit_small_avatars = 0
config.map.circle_size = 150
config.map.show_circle = True

# Ranking
config.ranking.avatar_size = 70
config.ranking.bg_color = '#dcdeff'
config.ranking.images_per_row = 8
config.ranking.padding = 20
config.ranking.district_name_height = 0
