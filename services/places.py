#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import sys
from models.tweet import Tweet
from models.tweet_type import Tweet_type
from services.simulation import write_tweet

from store import get_alive_players, place_list, move_player, kill_player, destroy_district_if_needed
from config import MAX_ITEMS, PROBAB_RARITY_1, PROBAB_RARITY_2, PROBAB_RARITY_3, ATRACT_RANGE, USE_DISTRICTS

def atract():
    loc_candidates = []
    action_number = random.randint(0, 100)

    for i, p in enumerate(place_list):
        if not p.destroyed:
            loc_candidates.append(p)

    place = random.choice(loc_candidates)
    atracted_players = []

    def append_players_from(location):
        for j, player in enumerate(location.players):
            if player.state == 1 and player not in atracted_players:
                atracted_players.append(player)

    append_players_from(place)
    for i, connection in enumerate(place.connections):
        append_players_from(connection)
        if ATRACT_RANGE > 1:
            for j, subconnection in enumerate(connection.connections):
                 append_players_from(subconnection)
                 if ATRACT_RANGE > 2:
                     for k, subsubconnection in enumerate(subconnection.connections):
                          append_players_from(subsubconnection)


    if len(atracted_players) > 0:
        alive_players = get_alive_players()
        for i, player in enumerate(alive_players):
            if player in atracted_players:
                move_player(player, place)

        tweet = Tweet()
        tweet.type = Tweet_type.atraction
        tweet.place = place
        tweet.player_list = atracted_players
        write_tweet(tweet)
        return True
    else:
        atract()

def trap():
    list = []
    for i, p in enumerate(place_list):
        if p.trap_by == None and len(p.players) > 0:
            any_alive = False
            for j, q in enumerate(p.players):
                if q.state == 1:
                    any_alive = True
            if any_alive:
                list.append(p)

    if len(list) > 0:
        candidates_list = []
        while len(candidates_list) == 0:
            place = random.choice(list)
            for i, p in enumerate(place.players):
                if p.state == 1:
                    candidates_list.append(p)

        player = random.choice(candidates_list)

        place.trap_by = player
        tweet = Tweet()
        tweet.type = Tweet_type.trap
        tweet.place = place
        tweet.player = player
        write_tweet(tweet)
        return True
    else:
        return False

def move():
    alive_players = get_alive_players()
    player = random.choice(alive_players)

    loc_candidates = []
    jump_candidates = []

    for i, l in enumerate(player.location.connections):
        if not l.destroyed:
            loc_candidates.append(l)

    if len(loc_candidates) == 0:
        for i, l in enumerate(player.location.connections):
            for j, sl in enumerate(l.connections):
                if not sl.destroyed:
                    loc_candidates.append(sl)
                    jump_candidates.append(l)

    if len(loc_candidates) == 0:
        return False

    new_location = random.choice(loc_candidates)
    jump = None
    if len(jump_candidates) > 0:
        jump = jump_candidates[loc_candidates.index(new_location)]
    action_number = random.randint(1, 100)

    if new_location.trap_by != None and new_location.trap_by != player:
        if action_number < 50:
            trapped_by = new_location.trap_by
            new_location.trap_by.kills = new_location.trap_by.kills + 1
            move_player(player, new_location)
            kill_player(player)
            tweet = Tweet()
            tweet.type = Tweet_type.trapped
            tweet.place = player.location
            tweet.player = player
            tweet.player_2 = trapped_by
            write_tweet(tweet)
            if USE_DISTRICTS:
                destroy_tweet = destroy_district_if_needed(player.district)
                if destroy_tweet != None:
                    write_tweet(destroy_tweet)
        else:
            trapped_by = new_location.trap_by
            new_location.trap_by = None

            move_player(player, new_location)
            tweet = Tweet()
            tweet.type = Tweet_type.trap_dodged
            tweet.place = player.location
            tweet.player = player
            tweet.player_2 = trapped_by
            write_tweet(tweet)
    else:
        old_location = player.location
        move_player(player, new_location)

        tweet = Tweet()
        tweet.type = Tweet_type.somebody_moved
        tweet.place = player.location
        tweet.place_2 = old_location
        tweet.player = player
        tweet.double = jump
        write_tweet(tweet)
    return True

def monster():
    place = None
    for i, p in enumerate(place_list):
        if p.monster:
            place = p

    if place != None:
        action_number = random.randint(1, 100)
        people_list = [x for x in place.players if x.state == 1 and not x.monster_immunity]

        if action_number > 50 and len(people_list) > 0:
            player = random.choice(people_list)
            kill_player(player)
            tweet = Tweet()
            tweet.type = Tweet_type.monster_killed
            tweet.place = player.location
            tweet.player = player
            write_tweet(tweet)
            if USE_DISTRICTS:
                destroy_tweet = destroy_district_if_needed(player.district)
                if destroy_tweet != None:
                    write_tweet(destroy_tweet)
        else:
            place.monster = False

            loc_candidates = []
            for i, l in enumerate(place.connections):
                if not l.destroyed:
                    loc_candidates.append(l)

            if len(loc_candidates) > 0 and action_number < 75:
                new_place = random.choice(loc_candidates)
                new_place.monster = True
                tweet = Tweet()
                tweet.type = Tweet_type.monster_moved
                tweet.place = new_place
                tweet.place_2 = place
                write_tweet(tweet)
            else:
                tweet = Tweet()
                tweet.type = Tweet_type.monster_disappeared
                tweet.place = place
                write_tweet(tweet)
    else:
        loc_candidates = []

        for i, p in enumerate(place_list):
            if not p.destroyed:
                loc_candidates.append(p)

        new_place = random.choice(loc_candidates)
        new_place.monster = True
    return True

def destroy():
    if USE_DISTRICTS:
        return False
    list = [x for x in place_list if not x.destroyed]
    place = random.choice(list)

    place.destroyed = True
    place.monster = False
    place.trap_by = None
    place.infected = False
    dead_list = []
    escaped_list = []
    route_list = []
    new_location = False

    for j, c in enumerate(place.connections):
        if not c.destroyed:
            route_list.append(c)

    if len(route_list) > 0:
        new_location = random.choice(route_list)

    for i, p in enumerate(place.players):
        if p.state == 1:
            if new_location and random.randint(0, 100) >= 75:
                move_player(p, new_location)
                escaped_list.append(p)
            else:
                kill_player(p)
                dead_list.append(p)

    tweet = Tweet()
    tweet.type = Tweet_type.destroyed
    tweet.place = place
    tweet.place_2 = new_location
    tweet.player_list = dead_list
    tweet.player_list_2 = escaped_list
    write_tweet(tweet)
    return True
