#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Tweet(object):
    type = None
    place = None
    place_2 = None
    player = None
    player_2 = None
    player_list = []
    player_list_2 = []

    action_number = None
    double = False
    factor = None
    inverse = False
    there_was_infection = False
    infected_or_was_infected_by = False
    item = None
    new_item = None
    old_item = None
    unfriend = False
    is_event = False

    def __init__(self):
        return
