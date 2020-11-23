#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ItemType(object):
    weapon = 1
    powerup = 2
    special = 3
    injury = 4

    def __init__(self):
        pass

    def __getattr__(self, attr):
        return self[attr]


class MatchType(object):
    standard = 1
    districts = 2
    rumble = 3

    def __init__(self):
        pass

    def __getattr__(self, attr):
        return self[attr]


class SpecialType(object):
    infection_immunity = 1
    monster_immunity = 2
    injure_immunity = 3

    def __init__(self):
        pass

    def __getattr__(self, attr):
        return self[attr]


class TweetType(object):
    start = 1
    winner_districts = 2
    hour_threshold = 3
    next_entrance = 4
    winner = 5
    nobody_won = 6
    somebody_stole = 7
    somebody_stole_and_replaced = 8
    somebody_stole_and_threw = 9
    somebody_got_special = 10
    soft_attack = 11
    somebody_found_item = 12
    somebody_replaced_item = 13
    introduce_players = 14
    somebody_tied_and_became_friend = 15
    somebody_tied_and_was_friend = 16
    somebody_escaped = 17
    somebody_killed = 18
    somebody_revived = 19
    somebody_suicided = 20
    somebody_moved = 21
    destroyed = 22
    somebody_couldnt_move = 23
    trap = 24
    trapped = 25
    trap_dodged = 26
    destroyed_district = 27
    monster_appeared = 28
    start_2 = 29
    monster_moved = 30
    monster_killed = 31
    somebody_died_of_infection = 32
    somebody_was_infected = 33
    attraction = 34
    somebody_got_cured = 35

    def __init__(self):
        pass

    def __getattr__(self, attr):
        return self[attr]
