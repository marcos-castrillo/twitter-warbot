#!/usr/bin/env python
# -*- coding: utf-8 -*-

from services.config import config
from models.enums import ItemType


class Item(object):
    type = None
    name = ""
    power = 0
    special = None
    thrown_away_by = None

    def __init__(self):
        return

    def get_rarity(self):
        if self.type == ItemType.special:
            return 3

        if self.power <= config.items.max_value_rarity_1:
            return 1
        elif self.power <= config.items.max_value_rarity_2:
            return 2
        else:
            return 3
