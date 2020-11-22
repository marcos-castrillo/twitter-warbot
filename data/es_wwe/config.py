#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models.match_type import Match_type

# General
config.general.mention_users = True
config.general.match_type = Match_type.rumble
config.general.use_flags = False
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
config.battle.probabilities.tie = 3
config.battle.probabilities.neutral = 25

THRESHOLD_LIST = []
TREASONS_ENABLED_LIST = [True]

# Map
config.map.avatar_size = 150
config.map.players_in_single_line = False
config.map.max_players_in_line = 5
config.map.width_between_players = 155
config.map.height_between_players = 155
config.map.watermark_coordinates = None
config.map.limit_small_avatars = 0
config.map.circle_size = 1000
config.map.show_circle = False

# Ranking
config.ranking.avatar_size = 70
config.ranking.bg_color = '#dcdeff'
config.ranking.images_per_row = 8
config.ranking.padding = 20
config.ranking.district_name_height = 0
