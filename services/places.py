#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import sys
from models.tweet import Tweet
from models.tweet_type import Tweet_type
from services.simulation import write_tweet

from store import *
from data.config import *

def atract():
    loc_candidates = []
    action_number = random.randint(0, 100)

    for i, p in enumerate(place_list):
        if not p.destroyed and not p.atracted and (MAX_ATRACTED_PLAYERS == 0 or len(p.players) <= MAX_ATRACTED_PLAYERS):
            loc_candidates.append(p)

    if len(loc_candidates) == 0:
        return False

    place = random.choice(loc_candidates)
    place.atracted = True
    atracted_players = []

    def append_players_from(location):
        for j, player in enumerate(location.players):
            if player.state == 1 and player not in atracted_players:
                atracted_players.append(player)

    atract_range = ATRACT_RANGE_LIST[hour_count]
    append_players_from(place)
    for i, connection in enumerate(place.connections):
        append_players_from(connection)
        if atract_range > 1:
            for j, subconnection in enumerate(connection.connections):
                 append_players_from(subconnection)
                 if atract_range > 2:
                     for k, subsubconnection in enumerate(subconnection.connections):
                          append_players_from(subsubconnection)

    if len(atracted_players) > 0:
        if MAX_ATRACTED_PLAYERS > 0 and len(atracted_players) > MAX_ATRACTED_PLAYERS:
            atracted_players = atracted_players[:MAX_ATRACTED_PLAYERS]
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

    for i, l in enumerate(player.location.connections):
        if not l.destroyed:
            loc_candidates.append(l)

    if len(loc_candidates) == 0:
        for j, c in enumerate(player.location.connections):
            for k, sc in enumerate(c.connections):
                if not sc.destroyed and sc.name != player.location.name:
                    loc_candidates.append(sc)

    if len(loc_candidates) == 0:
        for j, c in enumerate(player.location.connections):
            for k, sc in enumerate(c.connections):
                for l, ssc in enumerate(sc.connections):
                    if not ssc.destroyed and ssc.name != player.location.name:
                        loc_candidates.append(ssc)

    if len(loc_candidates) == 0:
        for j, c in enumerate(player.location.connections):
            for k, sc in enumerate(c.connections):
                for l, ssc in enumerate(sc.connections):
                    for m, sssc in enumerate(ssc.connections):
                        if not sssc.destroyed and sssc.name != player.location.name:
                            loc_candidates.append(sssc)

    if len(loc_candidates) == 0:
        candidates = [x for x in place_list if not x.destroyed and x.name != player.location.name]
        if len(candidates) == 0:
            return False
        else:
            new_location = random.choice()
    else:
        new_location = random.choice(loc_candidates)

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
        tweet = Tweet()
        print(action_number)
        if action_number > 90 and len(spare_powerup_list) > 0:
            powerup = random.choice(spare_powerup_list)
            player.powerup_list.append(powerup)
            tweet.item = powerup
        elif action_number > 80:
            player.attack = player.attack + 2
            tweet.double = True
        elif action_number > 70:
            player.defense = player.defense + 2
            tweet.double = True
            tweet.inverse = True
        elif action_number > 50 and not player.injure_immunity:
            injury = random.choice(injury_list)
            player.injury_list.append(injury)
            tweet.item = injury
            print(injury.name)

        old_location = player.location
        move_player(player, new_location)

        tweet.type = Tweet_type.somebody_moved
        tweet.place = player.location
        tweet.place_2 = old_location
        tweet.player = player
        write_tweet(tweet)
    return True

def monster():
    place = [x for x in place_list if x.monster]

    if len(place) > 0:
        place = place[0]
        action_number = random.randint(1, 100)
        people_list = [x for x in place.players if x.state == 1 and not x.monster_immunity]

        if action_number < 50 and len(people_list) > 0:
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
            loc_candidates = [x for x in place.connections if not x.destroyed]

            if len(loc_candidates) > 0 and action_number < 75:
                new_place = random.choice(loc_candidates)
                new_place.monster = True
                tweet = Tweet()
                tweet.type = Tweet_type.monster_moved
                tweet.place = new_place
                tweet.place_2 = place
                write_tweet(tweet)
            else:
                return False
    else:
        loc_candidates = [x for x in place_list if not x.destroyed]

        new_place = random.choice(loc_candidates)
        new_place.monster = True
        tweet = Tweet()
        tweet.type = Tweet_type.monster_appeared
        tweet.place = new_place
        write_tweet(tweet)
    return True

def destroy():
    if USE_DISTRICTS:
        return False
    list = [x for x in place_list if not x.destroyed]
    if len(list) == 0:
        sys.exit('Error: everything is destroyed')
    place = random.choice(list)

    place.destroyed = True
    place.monster = False
    place.trap_by = None
    place.infected = False
    dead_list = []
    escaped_list = []
    route_list = []
    new_location = None

    for j, c in enumerate(place.connections):
        if not c.destroyed:
            route_list.append(c)

    if len(route_list) > 0:
        new_location = random.choice(route_list)
    else:
        for j, c in enumerate(place.connections):
            for k, sc in enumerate(c.connections):
                if not sc.destroyed:
                    route_list.append(sc)

    if len(route_list) > 0:
        new_location = random.choice(route_list)
    else:
        for j, c in enumerate(place.connections):
            for k, sc in enumerate(c.connections):
                for k, ssc in enumerate(sc.connections):
                    if not ssc.destroyed:
                        route_list.append(ssc)

    new_location = random.choice(route_list)

    for i, p in enumerate(place.players):
        if p.state == 1:
            if random.randint(0, 100) >= 75:
                escaped_list.append(p)
            else:
                kill_player(p)
                dead_list.append(p)

    for i, p in enumerate(escaped_list):
        move_player(p, new_location)

    tweet = Tweet()
    tweet.type = Tweet_type.destroyed
    tweet.place = place
    tweet.place_2 = new_location
    tweet.player_list = dead_list
    tweet.player_list_2 = escaped_list
    write_tweet(tweet)
    return True
