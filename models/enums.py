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

    def __init__(self):
        pass

    def __getattr__(self, attr):
        return self[attr]


class SpecialType(object):
    infection_immunity = 1
    monster_immunity = 2
    injure_immunity = 3
    movement_boost = 4
    zombie_immunity = 5
    friendship_boost = 6

    def __init__(self):
        pass

    def __getattr__(self, attr):
        return self[attr]


class TweetType(object):
    start = 1
    winner_districts = 2
    introduce_players = 3
    winner = 5
    somebody_stole = 7
    somebody_stole_and_replaced = 8
    somebody_stole_and_threw = 9
    somebody_got_special = 10
    somebody_found_item = 12
    somebody_replaced_item = 13
    somebody_tied_and_became_friend = 15
    somebody_tied_and_was_friend = 16
    somebody_escaped = 17
    somebody_killed = 18
    somebody_revived = 19
    somebody_suicided = 20
    somebody_moved = 21
    destroyed = 22
    somebody_moved_together_with = 23
    trap = 24
    trapped = 25
    trap_dodged = 26
    destroyed_district = 27
    monster_appeared = 28
    start_2 = 29
    monster_moved = 30
    monster_took = 31
    somebody_died_of_infection = 32
    somebody_was_infected = 33
    attraction = 34
    somebody_got_cured = 35
    zombie_appeared = 36
    zombie_moved = 37
    zombie_killed = 38
    zombie_was_defeated = 39
    doctor_appeared = 40
    doctor_moved = 41
    doctor_cured = 42
    somebody_hurt = 43

    def __init__(self):
        pass

    def __getattr__(self, attr):
        return self[attr]
