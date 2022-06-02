#!/usr/bin/env python
# -*- coding: utf-8 -*-

from data.config import config


class Player(object):
    avatar_dir = None
    district = None
    friend_list = []
    friendship_boost = False
    gender = None
    infected = False
    infection_immunity = False
    injure_immunity = False
    injury_list = []
    is_alive = True
    is_zombie = False
    item_list = []
    kills = 0
    location = None
    monster_immunity = False
    movement_boost = False
    name = ""
    power = 0
    powerup_list = []
    previous_power = None
    username = ""
    zombie_immunity = False

    # Constructor
    def __init__(self):
        self.item_list = []
        self.injury_list = []
        self.friend_list = []
        self.powerup_list = []
        return

    def get_power(self):
        if self.previous_power is not None:
            return self.previous_power
        power = self.power
        for item in self.item_list:
            power = power + item.power
        for injury in self.injury_list:
            power = power + injury.power
        for powerup in self.powerup_list:
            power = power + powerup.power
        return power

    def get_best_item(self):
        if len(self.item_list) == 0:
            return None
        elif len(self.item_list) == 1:
            return self.item_list[0]
        else:
            if self.item_list[0].power >= self.item_list[1].power:
                return self.item_list[0]
            else:
                return self.item_list[1]

    def get_worst_item(self):
        if len(self.item_list) == 0:
            return None
        elif len(self.item_list) == 1:
            return self.item_list[0]
        else:
            if self.item_list[0].power < self.item_list[1].power:
                return self.item_list[0]
            else:
                return self.item_list[1]

    def get_name(self):
        if self.username != "" and config.general.mention_users:
            return self.name + u'(@' + self.username + u')'
        else:
            return self.name
